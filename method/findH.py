import numpy as np
from utils.function import *
import configparser
import random


def findH(budget):
    config = configparser.ConfigParser()
    config.read("config.ini", encoding="utf-8")
    task_num = int(config["global"]["task_num"])
    terminal_num = int(config["global"]["terminal_num"])
    lambda1 = float(config["global"]["lambda1"])
    lambda2 = float(config["global"]["lambda2"])
    lambda_sum = lambda1 + lambda2
    C_bud = budget
    C_dev = float(config["global"]["C_dev"])
    C_bs = float(config["global"]["C_bs"])
    rhfedmtl_server_iters = int(config["RHFedMTL"]["server_iters"])
    eD = 0.0001

    N_b = terminal_num
    T_star = terminal_num
    gamma = 100
    sigma = -1e100

    nb_sum = 1300
    local_data = nb_sum / task_num / terminal_num

    Kmin = 99999999999

    KList = []
    CList = []
    HList = []
    H = 1
    while True:
        # H 从1开始迭代
        K = int(np.log(nb_sum / (task_num * eD)) * np.power(1 - 1 / local_data, H))
        # K为0非物理解
        if int(K) == 0:
            break
        cost = (
            K
            * (task_num * terminal_num * H * C_dev + task_num * C_bs)
            * rhfedmtl_server_iters
        )

        KList.append(K)
        HList.append(H)
        CList.append(cost)
        H += 1
    # print(CList)
    # print(HList)
    # print(KList)

    # 排除掉一开始就递减的
    # 必须得经历过一次递减
    decre = False
    for i in range(len(CList) - 1):
        if CList[i] > CList[i + 1]:
            decre = True
        if decre and CList[i] < budget and CList[i + 1] > budget:
            return KList[i], i + 1, True  # index 0 H为1

    for i in range(len(CList) - 1):
        if CList[i] <= budget and CList[i + 1] > budget:
            return KList[i], i + 1, True  # index 0 H为1

    # 无论H怎么调都不满足，那就是取让整体资源最小的H
    index = np.argmin(CList)
    K = KList[index]
    H = index + 1
    print("current H", H)
    # 如果这样的H超出了资源限制，那么降低H
    cost = (
        K
        * (task_num * terminal_num * H * C_dev + task_num * C_bs)
        * rhfedmtl_server_iters
    )
    if cost > budget:
        K = 1
        H = (
            (budget / rhfedmtl_server_iters - task_num * C_bs)
            / task_num
            / terminal_num
            / C_dev
        )
        H = int(H)
        return K, H, False
    return K, H, False
