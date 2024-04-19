import numpy as np
from utils.function import *
from scipy.linalg import sqrtm
import configparser
import random


def rhfedmtl(data, budget, K, H, ok):
    print("Running RHFedMTL , budget=", budget)

    config = configparser.ConfigParser()
    config.read("config.ini", encoding="utf-8")
    log = int(config["global"]["log"])
    task_num = int(config["global"]["task_num"])
    terminal_num = int(config["global"]["terminal_num"])

    lambda1 = float(config["RHFedMTL"]["lambda1"])
    lambda2 = float(config["RHFedMTL"]["lambda2"])

    rhfedmtl_server_iters = int(config["RHFedMTL"]["server_iters"])
    rhfedmtl_base_iters = int(config["RHFedMTL"]["base_iters"])
    # H = int(config["RHFedMTL"]["local_iters"])
    C_dev = float(config["global"]["C_dev"])
    C_bs = float(config["global"]["C_bs"])
    C_bud = float(config["global"]["C_bud"])

    Xtrain, Ytrain, Xtest, Ytest = data

    # print("Xtrain[0]: ", Xtrain[0].shape)
    # print("Ytrain[0]: ", Ytrain[0].shape)
    # print("Xtest[0]: ", Xtest[0].shape)
    # print("Ytest[0]: ", Ytest[0].shape)

    dim = Xtrain[0].shape[1]
    # 每一个task终端本地数据数量（数据在所有终端均匀分布，数据量一样）
    task_local_data = int(Xtrain[0].shape[0] / terminal_num)

    W = np.matrix(np.zeros((dim, task_num)))  # 所有task按列拼接的model
    r = np.matrix(np.zeros((dim, 1)))  # 平均的model

    alpha = []
    X = []
    Y = []
    for t in range(task_num):
        alpha.append(np.zeros((terminal_num, task_local_data, 1)))
        X.append(Xtrain[t].reshape(terminal_num, task_local_data, -1))
        Y.append(Ytrain[t].reshape(terminal_num, task_local_data, -1))
    if log or True:
        print(X[0].shape)
        print(Y[0].shape)
        print(alpha[0][0].shape)

    iterNum = rhfedmtl_server_iters * K
    rmse = np.zeros((iterNum, 1))
    dual_objs = np.zeros((iterNum, 1))
    primal_objs = np.zeros((iterNum, 1))
    H_num = np.zeros((iterNum, 1))

    if ok:
        rhfedmtl_base_iters = int(K)
    else:
        rhfedmtl_base_iters = int(
            np.ceil(
                C_bud
                / rhfedmtl_server_iters
                / rhfedmtl_base_iters
                / (task_num * C_bs + task_num * terminal_num * H)
            )
        )
    print("server iter: ", rhfedmtl_server_iters)
    print("base iter: ", rhfedmtl_base_iters)
    print("H: ", H)
    for h in range(rhfedmtl_server_iters):
        for hh in range(rhfedmtl_base_iters):
            np.random.seed(hh * 1000)

            deltaW = np.zeros((task_num, dim, terminal_num))  # local terminal
            deltaB = np.zeros((dim, task_num))  # BS

            for b in range(task_num):
                alpha_b = alpha[b]  # copy the alpha of task
                nb = task_local_data * terminal_num
                for t in range(terminal_num):
                    for s in range(H):
                        lambda_sum = lambda1 + lambda2
                        local_w = (
                            W[:, [b]] + lambda2 * r / lambda_sum + deltaW[b][:, [t]]
                        )

                        idx = random.randint(0, task_local_data - 1)

                        alpha_old = alpha_b[t, idx, 0]
                        curr_y = Y[b][t, idx, 0]
                        curr_x = np.matrix(X[b][t, [idx], :])

                        update = curr_y * (curr_x * local_w)
                        grad = lambda_sum * (1.0 - update) / (curr_x * curr_x.T)
                        grad = grad * (
                            1 - lambda1 * (curr_x * local_w) - lambda2 * (curr_x * r)
                        )
                        grad += alpha_old * curr_y

                        alpha_b[t, idx, 0] = curr_y * max(0.0, min(1.0, grad[0, 0]))

                        deltaW[b][:, [t]] += (
                            (alpha_b[t, idx, 0] - alpha_old)
                            * curr_x.T
                            / (lambda_sum * nb)
                        )
                        deltaB[:, [b]] += (
                            (alpha_b[t, idx, 0] - alpha_old)
                            * curr_x.T
                            / (lambda_sum * nb)
                        )
                        alpha[b] = alpha_b

            # BS aggregate
            # 不能让r迭代到W中，否则过了几轮，W会越来越大，最后爆炸
            for b in range(task_num):
                W[:, [b]] += deltaB[:, [b]]

            iter = h * rhfedmtl_base_iters + hh
            rmse[iter] = compute_rmse(Xtest, Ytest, W)
            # print("rmse: ", rmse[iter])
            primal_objs[iter] = compute_primal(Xtrain, Ytrain, W, r, lambda1, lambda2)
            # dual_objs[iter] = compute_dual(alpha, Ytrain, W, r, lambda1, lambda2)
            H_num[iter] = H

        # Server aggregate
        r[...] = 0
        for b in range(task_num):
            r[:, [0]] += W[:, [b]]
        r = r / task_num
        # print("regulation :\n", r)

    # print("alpha\n", alpha[0][0])
    return (rmse, primal_objs, dual_objs), H
