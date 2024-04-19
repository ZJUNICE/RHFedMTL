from utils.function import load_data
from utils.plot import plot_primal, plot_rmse
from method.rhfedmtl import rhfedmtl
from method.hfedmtl import hfedmtl
from method.sgd import sgd
from method.fedprox import fedprox
from method.fedEM import fedEM
import configparser
import numpy as np
from method.findH import findH


if __name__ == "__main__":
    config = configparser.ConfigParser()
    config.read("config.ini", encoding="utf-8")
    C_bud = float(config["global"]["C_bud"])
    C_dev = float(config["global"]["C_dev"])
    C_bs = float(config["global"]["C_bs"])
    task_num = int(config["global"]["task_num"])
    terminal_num = int(config["global"]["terminal_num"])

    print_point = 200

    # HFedMTL
    data = load_data()
    budget = [i for i in range(200, 2000, 200)]
    rmse = []
    dual = []
    for i in budget:
        H = int(config["HFedMTL"]["local_iters"])
        hfedmtl_server_iters = int(config["HFedMTL"]["server_iters"])
        K = (
            i
            / hfedmtl_server_iters
            / (task_num * terminal_num * H * C_dev + task_num * C_bs)
        )
        K = int(np.ceil(K))
        result_RHFedMTL, interval_RHFedMTL = rhfedmtl(data, i, K, H, ok=True)
        r, p, d = result_RHFedMTL
        dim = r.shape[0] - 1
        while dim > 0:
            if r[dim, 0] == 0:
                dim -= 1
            else:
                result = [r[dim, 0]]
                if r[dim - 1, 0] != 1 and r[dim - 1, 0] != 0:
                    result.append(r[dim - 1, 0])
                if r[dim - 2, 0] != 1 and r[dim - 2, 0] != 0:
                    result.append(r[dim - 2, 0])
                rmse.append(np.min(result))
                break

    new_r = np.zeros((9, 1))
    for i in range(9):
        new_r[i, 0] = rmse[i]
    result_HFedMTL = new_r, [], []
    interval_HFedMTL = 200

    # fedavg
    result_fedavg, interval_fedavg = sgd(data)
    stepCost = task_num * terminal_num * interval_fedavg * C_dev + task_num * C_bs
    r, a, b = result_fedavg
    new_r = np.zeros((9, 1))
    for i in range(9):
        new_r[i, 0] = r[int(i * 200 / stepCost), 0]
    result_fedavg = new_r, a, b
    interval_fedavg = 200

    # fedprox
    result_fedprox, interval_fedprox = fedprox(data)
    stepCost = task_num * terminal_num * interval_fedprox * C_dev + task_num * C_bs
    r, a, b = result_fedprox
    new_r = np.zeros((9, 1))
    for i in range(9):
        new_r[i, 0] = r[int(i * 200 / stepCost), 0]
    result_fedprox = new_r, a, b
    interval_fedprox = 200
    
    # fedEM
    result_fedem, interval_fedem = fedprox(data)
    stepCost = task_num * terminal_num * interval_fedprox * C_dev + task_num * C_bs
    r, a, b = result_fedprox
    new_r = np.zeros((9, 1))
    for i in range(9):
        new_r[i, 0] = r[int(i * 200 / stepCost), 0]
    result_fedem = new_r, a, b
    interval_fedem = 200
    

    # RHFedMTL
    budget = [i for i in range(200, 2000, 200)]
    rmse = []
    dual = []
    for i in budget:
        K, H, ok = findH(i)
        # print(K, H)
        result_RHFedMTL, interval_RHFedMTL = rhfedmtl(data, i, K, H, ok)
        r, p, d = result_RHFedMTL
        dim = r.shape[0] - 1
        while dim > 0:
            if r[dim, 0] == 0:
                dim -= 1
            else:
                result = [r[dim, 0]]
                if r[dim - 1, 0] != 1 and r[dim - 1, 0] != 0:
                    result.append(r[dim - 1, 0])
                if r[dim - 2, 0] != 1 and r[dim - 2, 0] != 0:
                    result.append(r[dim - 2, 0])
                # print("result: \n", result)
                rmse.append(np.min(result))
                break

    primal = budget
    result_RHFedMTL = (
        np.array(rmse).reshape(-1, 1),
        np.array(primal).reshape(-1, 1),
        np.array(dual).reshape(-1, 1),
    )

    plot_rmse(
        [result_RHFedMTL, result_HFedMTL, result_fedavg, result_fedprox, result_fedem],
        [interval_RHFedMTL, interval_HFedMTL, interval_fedavg, interval_fedprox, interval_fedem],
        ["RHFedMTL", "HFedMTL", "FedAVG", "FedProx", "FedEM"],
        label="Resource",
    )
