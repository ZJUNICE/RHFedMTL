import numpy as np
from scipy.io import loadmat
import configparser


def load_data():
    config = configparser.ConfigParser()
    config.read("config.ini", encoding="utf-8")
    testRatio = float(config["global"]["testRatio"])
    log = int(config["global"]["log"])
    terminal_num = int(config["global"]["terminal_num"])
    task_num = int(config["global"]["task_num"])

    data = loadmat("./data/small.mat", mat_dtype=True)
    x = np.array(data["X"])
    y = np.array(data["Y"])
    dim = x[0, 0].shape[1]
    print("X:\n", x[0, 2].shape)
    print("Y:\n", y[0, 1].shape)
    X = []
    Y = []
    origin_tNum = x.shape[1]  # 29
    for t in range(origin_tNum):
        X.append(x[0, t])
        Y.append(y[0, t])
    X = np.vstack(X)
    Y = np.vstack(Y)

    num = X.shape[0]
    termData = int(num / (terminal_num * task_num))
    taskData = termData * terminal_num

    xTrain = [0 for i in range(task_num)]
    xTest = [0 for i in range(task_num)]
    yTrain = [0 for i in range(task_num)]
    yTest = [0 for i in range(task_num)]
    for i in range(task_num):
        idx_start = i * taskData
        idx_end = (i + 1) * taskData
        testIdx = (
            int((idx_end - idx_start) * (1 - testRatio) / terminal_num) * terminal_num
            + idx_start
        )

        xTrain[i] = X[idx_start:testIdx, :]
        yTrain[i] = Y[idx_start:testIdx, :]
        xTest[i] = X[testIdx:idx_end, :]
        yTest[i] = Y[testIdx:idx_end, :]

        if log:
            print("\nTask id: ", i)
            print("xTrain : ", xTrain[i].shape)
            print("yTrain : ", yTrain[i].shape)
            print("xTest  : ", xTest[i].shape)
            print("yTest  : ", yTest[i].shape)
    data = xTrain, yTrain, xTest, yTest
    return data


def compute_rmse(X, Y, W, all_error=1):
    """
    Computes RMSE for MTL
    X: m-length list of nxd features
    Y: m-length list of nx1 labels
    W: dxm weight matrix
    config:
      avg: compute avg (avg = 1) or total (avg = 0) rmse
      obj: 'R' for regression, 'C' for classification
    """
    config = configparser.ConfigParser()
    config.read("config.ini", encoding="utf-8")
    terminal_num = int(config["global"]["terminal_num"])
    task_num = int(config["global"]["task_num"])
    log = int(config["global"]["log"])

    Y_hat = [0 for t in range(task_num)]

    for t in range(task_num):
        Y_hat[t] = np.sign(X[t] * W[:, t])

    task_error = np.zeros((task_num, 1))
    for t in range(task_num):
        err_t = []
        for idx in range(Y_hat[t].shape[0]):
            err = 1 if Y_hat[t][idx, 0] != Y[t][idx, 0] else 0
            err_t.append(err)
        task_error[t, 0] = np.mean(err_t)
    err = np.mean(task_error)

    # print("YHat: ", Y_hat[0].T)
    # print("Y   : ", Y[0].T)
    if log:
        print("rmse    : ", err)
        print("Y hat[0]: \n", Y_hat[0].T)
        print("Y[0]    : \n", Y[0].T)

    if all_error:
        return err
    else:
        return task_error


def compute_rmse_task(X, Y, W, all_error=1):
    """
    Computes RMSE for MTL
    X: m-length list of nxd features
    Y: m-length list of nx1 labels
    W: dxm weight matrix
    config:
      avg: compute avg (avg = 1) or total (avg = 0) rmse
      obj: 'R' for regression, 'C' for classification
    """
    config = configparser.ConfigParser()
    config.read("config.ini", encoding="utf-8")
    terminal_num = int(config["global"]["terminal_num"])
    task_num = int(config["global"]["task_num"])
    log = int(config["global"]["log"])

    Y_hat = [0 for t in range(task_num)]

    for t in range(task_num):
        Y_hat[t] = np.sign(X[t] * W[:, t])

    task_error = np.zeros((task_num, 1))
    for t in range(task_num):
        err_t = []
        for idx in range(Y_hat[t].shape[0]):
            err = 1 if Y_hat[t][idx, 0] != Y[t][idx, 0] else 0
            err_t.append(err)
        task_error[t, 0] = np.mean(err_t)
    # err = np.mean(task_error)
    return task_error


def compute_primal(XX, YY, W, r, lambda1, lambda2):
    """
    Inputs
      Xtrain: input training data (m-length list)
      Ytrain: output training data (m-length list)
      W: current models (d x m)
      Sigma: precision matrix (m x m)
      lambda: regularization parameter
    Output
      primal objective
    """
    X = np.copy(XX)
    Y = np.copy(YY)
    config = configparser.ConfigParser()
    config.read("config.ini", encoding="utf-8")
    task_num = int(config["global"]["task_num"])
    log = int(config["global"]["log"])

    total_loss = 0
    for t in range(task_num):
        preds = np.multiply(Y[t], X[t] * W[:, t])
        total_loss += np.mean(np.minimum(np.maximum(0.0, 1.0 - preds), 2)) / task_num
    primal_obj = (
        total_loss
        + lambda1 / 2 * np.trace(W * W.T) / task_num
        + lambda2 / 2 * np.trace((W - r) * (W - r).T) / task_num
    )
    if log:
        print("prim: ", primal_obj)
        print(np.trace(W * W.T))
        print(np.trace((W - r) * (W - r).T))
    return primal_obj


def compute_primal_task(XX, YY, W, r, lambda1, lambda2):
    """
    Inputs
      Xtrain: input training data (m-length list)
      Ytrain: output training data (m-length list)
      W: current models (d x m)
      Sigma: precision matrix (m x m)
      lambda: regularization parameter
    Output
      primal objective
    """
    X = np.copy(XX)
    Y = np.copy(YY)
    config = configparser.ConfigParser()
    config.read("config.ini", encoding="utf-8")
    task_num = int(config["global"]["task_num"])
    log = int(config["global"]["log"])

    total_loss = 0
    for t in range(task_num):
        preds = np.multiply(Y[t], X[t] * W[:, t])
        total_loss += np.mean(np.minimum(np.maximum(0.0, 1.0 - preds), 2)) / task_num
    primal_obj = (
        total_loss
        + lambda1 / 2 * np.trace(W * W.T) / task_num
        + lambda2 / 2 * np.trace((W - r) * (W - r).T) / task_num
    )
    if log:
        print("prim: ", primal_obj)
        print(np.trace(W * W.T))
        print(np.trace((W - r) * (W - r).T))
    return primal_obj


def compute_dual(alpha_o, YY, W, r, lambda1, lambda2):
    """
    Inputs
      alpha: dual variables (m-length list)
      Y: output training data (m-length list)
      W: current models (d x m)
      lambda: regularization parameter
    Output
      primal objective
    """
    config = configparser.ConfigParser()
    config.read("config.ini", encoding="utf-8")
    log = int(config["global"]["log"])

    alpha = np.copy(alpha_o)
    Y = np.copy(YY)

    total_alpha = 0
    task_num = len(Y)
    for tt in range(task_num):
        total_alpha += np.mean(-1.0 * np.multiply(alpha[tt], Y[tt]))
    dual_obj = -total_alpha + (
        lambda2**2 * r * r.T
        - np.trace(W * W.T) / task_num
        - 2 * lambda2 * np.mean(W.T * r)
    ) / (2 * (lambda1 + lambda2))
    if log:
        print("dual: ", dual_obj)
    return dual_obj
