import numpy as np
import matplotlib.pyplot as plt


def plot_primal(results, intervals, names, label="Time"):
    num = len(names)
    fig = plt.figure(num="Primal Sub-Optimality", figsize=(5, 5))
    plt.grid(linestyle="--")
    ax = plt.gca()
    ax.spines["top"].set_visible(False)  # 去掉上边框
    ax.spines["right"].set_visible(False)  # 去掉右边框

    for i in range(num):
        rmse, primal, dual = results[i]
        interval = intervals[i]
        name = names[i]
        data_num = primal.shape[0]
        time = [interval * i for i in range(data_num)]
        pri = [primal[i, 0] for i in range(data_num)]
        plt.plot(time, pri, label=name)

    plt.xlabel(label)
    plt.ylabel("Primal Sub-Optimality")
    plt.legend()
    plt.savefig("./figure/Primal Sub-Optimality.jpg")


def plot_rmse(results, intervals, names, label="Resource"):
    num = len(names)
    fig = plt.figure(num="Accuracy", figsize=(5, 5))
    plt.grid(linestyle="--")
    ax = plt.gca()
    ax.spines["top"].set_visible(False)  # 去掉上边框
    ax.spines["right"].set_visible(False)  # 去掉右边框
    fw = open("figure/accuracy.txt", "w")
    len_list = [results[i][0].shape[0] for i in range(len(results))]
    length = np.min(len_list)
    print("length: ", length)
    for i in range(num):
        rmse, primal, dual = results[i]
        rmse = rmse[:length]
        dual = dual[:length]
        primal = primal[:length]
        interval = intervals[i]
        name = names[i]
        data_num = rmse.shape[0]
        # RHFedMTL primal 位置填的是budget
        if name == "RHFedMTL":
            time = primal
        else:
            time = [interval * i for i in range(data_num + 1)]
            print("rmse: ", rmse.shape)
            rmse_start = np.array([[1]])
            rmse = np.vstack((rmse_start, rmse))
        plt.plot(time, 1 - rmse, "-o", label=name)
        fw.write("======{}====== \n".format(name))
        fw.write("Accuracy \t Resource \n")
        for i in range(data_num):
            fw.write("{} \t {} \n".format(1 - rmse[i, 0], time[i]))
    fw.close()
    plt.xlabel(label)
    plt.ylabel("Accuracy")
    # plt.ylim(0.4, 0.85)
    plt.legend()
    plt.savefig("./figure/Accuracy.pdf")
    plt.savefig("./Accuracy.jpg")


def plot_rmse_t(results, intervals, names, H):
    num = len(names)
    fw = open("figure/accuracy.txt", "w")

    # task_rmse, primal, dual = results[0]

    # space = 4
    # t = []
    # points = task_rmse.shape[0]
    # r = np.zeros((int(points / space), task_rmse.shape[1]))
    # for i in range(len(time)):
    #     if i % space == 0:
    #         t.append(time[i])
    #         for t in range(5):
    #             r[int(i / space), t] = task_rmse[i, t][0]
    # time = t
    # task_rmse = r

    # 多少个算法
    for i in range(num):
        task_rmse, primal, dual = results[i]
        interval = intervals[i]
        name = names[i]
        data_num = task_rmse.shape[0]
        print("name: {} dataNum: {}".format(name, data_num))
        # RHFedMTL dual 位置填的是time
        if name == "RHFedMTL":
            interval = H
        time = [interval * i for i in range(data_num)]
        fw.write("======{}====== \n".format(name))

        # 每个不同的任务都要画
        for t in range(task_rmse.shape[1]):
            fw.write("Task {}====== \n".format(t))
            fw.write("Accuracy \t Time \n")
            for i in range(data_num):
                fw.write("{} \t {} \n".format(1 - task_rmse[i, t], time[i]))
    fw.close()


# def plot_figure(
#     rhfedmtl_result,
#     rhfedmtl_interval,
#     hfedmtl_result,
#     hfedmtl_interval,
#     sgd_result,
#     sgd_interval,
# ):
#     rmse_rhfedmtl, primal_rhfedmtl, dual_rhfedmtl = rhfedmtl_result
#     rmse_hfedmtl, primal_hfedmtl, dual_hfedmtl = hfedmtl_result
#     rmse_sgd, primal_sgd = sgd_result
#     print("rmse rhfedmtl shape: ", rmse_rhfedmtl.shape)
#     print("rmse hfedmtl shape: ", rmse_hfedmtl.shape)
#     print("rmse sgd shape: ", rmse_sgd.shape)
#     optimal = np.min(
#         [np.min(primal_rhfedmtl), np.min(primal_hfedmtl), np.min(primal_sgd)]
#     )

#     # calculate time based on flops and communication cost
#     # comm_cost = 100  # communication cost: Wifi=10, LTE=100, 3G=1000
#     rhfedmtl_time = range(
#         0, (rhfedmtl_interval) * len(primal_rhfedmtl), rhfedmtl_interval
#     )
#     hfedmtl_time = range(0, (hfedmtl_interval) * len(primal_hfedmtl), hfedmtl_interval)
#     sgd_time = range(0, sgd_interval * len(primal_sgd), sgd_interval)

#     step = 1

#     # plt.switch_backend("agg")

#     fig = plt.figure(num="Primal Sub-Optimality", figsize=(5, 5))
#     plt.grid(linestyle="--")
#     ax = plt.gca()
#     ax.spines["top"].set_visible(False)  # 去掉上边框
#     ax.spines["right"].set_visible(False)  # 去掉右边框
#     min_interval = min(rhfedmtl_interval, hfedmtl_interval, sgd_interval)
#     idx_bound_hfedmtl = int(min_interval / hfedmtl_interval * len(primal_hfedmtl))
#     idx_bound_rhfedmtl = int(min_interval / rhfedmtl_interval * len(primal_rhfedmtl))
#     idx_bound_sgd = int(min_interval / sgd_interval * len(primal_hfedmtl))
#     plt.plot(
#         rhfedmtl_time[0:idx_bound_rhfedmtl:step],
#         primal_rhfedmtl[0:idx_bound_rhfedmtl:step] - optimal,
#         label="RHFedMTL",
#     )
#     plt.plot(
#         hfedmtl_time[0:idx_bound_hfedmtl:step],
#         primal_hfedmtl[0:idx_bound_hfedmtl:step] - optimal,
#         label="HFedMTL",
#     )
#     plt.plot(
#         sgd_time[0:idx_bound_sgd:step],
#         primal_sgd[0:idx_bound_sgd:step] - optimal,
#         label="SGD",
#     )
#     plt.xlabel("Time")
#     plt.ylabel("Primal Sub-Optimality")
#     plt.legend()
#     # plt.title("Primal Sub-Optimality")
#     plt.savefig("./figure/Primal Sub-Optimality.jpg")

#     plt.figure(num="rmse", figsize=(5, 5))
#     plt.grid(linestyle="--")
#     ax = plt.gca()
#     ax.spines["top"].set_visible(False)  # 去掉上边框
#     ax.spines["right"].set_visible(False)  # 去掉右边框
#     plt.plot(
#         rhfedmtl_time[0:idx_bound_rhfedmtl:step],
#         rmse_rhfedmtl[0:idx_bound_rhfedmtl:step],
#         label="RHFedMTL",
#     )
#     plt.plot(
#         hfedmtl_time[0:idx_bound_hfedmtl:step],
#         rmse_hfedmtl[0:idx_bound_hfedmtl:step],
#         label="HFedMTL",
#     )
#     plt.plot(
#         sgd_time[0:idx_bound_sgd:step], rmse_sgd[0:idx_bound_sgd:step], label="SGD"
#     )
#     plt.xlabel("Time")
#     plt.ylabel("RMSE")
#     plt.ylim(0.1, 0.6)
#     plt.legend()

#     # plt.title("RMSE")
#     plt.savefig("./figure/RMSE.jpg")
