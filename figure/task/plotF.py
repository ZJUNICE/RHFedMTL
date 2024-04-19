import matplotlib.pyplot as plt

time = [
    0,
    4,
    8,
    12,
    16,
    20,
    24,
    28,
    32,
    36,
    40,
    46,
]

a1 = [
    [0.0],
    [0.43333333],
    [0.36666667],
    [0.36666667],
    [0.5],
    [0.56666667],
    [0.66666667],
    [0.83333333],
    [0.6],
    [0.5],
    [0.46666667],
    [0.46666667],
]

a2 = [
    [0.0],
    [0.46666667],
    [0.4],
    [0.4],
    [0.5],
    [0.43333333],
    [0.33333333],
    [0.43333333],
    [0.43333333],
    [0.5],
    [0.36666667],
    [0.43333333],
]

a3 = [
    [0.0],
    [0.36666667],
    [0.3],
    [0.36666667],
    [0.5],
    [0.43333333],
    [0.26666667],
    [0.23333333],
    [0.2],
    [0.33333333],
    [0.36666667],
    [0.43333333],
]

a4 = [
    [0.0],
    [0.7],
    [0.86666667],
    [0.9],
    [0.9],
    [0.76666667],
    [0.86666667],
    [0.9],
    [0.9],
    [0.86666667],
    [0.86666667],
    [0.83333333],
]

a5 = [
    [0.0],
    [0.53333333],
    [0.63333333],
    [0.56666667],
    [0.53333333],
    [0.56666667],
    [0.7],
    [0.7],
    [0.66666667],
    [0.66666667],
    [0.7],
    [0.66666667],
]


plt.figure(figsize=(4, 4))
plt.grid(linestyle="--")
plt.plot(time, a1, markersize=4, marker="v", label="Task {}".format(1))
plt.plot(time, a2, markersize=4, marker="^", label="Task {}".format(2))
plt.plot(time, a3, markersize=4, marker="o", label="Task {}".format(3))
plt.plot(time, a4, markersize=4, marker="x", label="Task {}".format(4))
plt.plot(time, a5, markersize=4, marker="s", label="Task {}".format(5))
plt.legend(loc="lower right")
plt.xlabel("Time")
plt.ylabel("Accuracy")
plt.ylim(0.2, 1)
plt.savefig("FedAVG_task.pdf")
plt.show()
