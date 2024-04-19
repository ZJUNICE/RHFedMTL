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
    [0.7],
    [0.6],
    [0.6],
    [0.6],
    [0.63333333],
    [0.63333333],
    [0.63333333],
    [0.63333333],
    [0.63333333],
    [0.63333333],
    [0.73333333],
]

a2 = [
    [0.0],
    [0.7],
    [0.63333333],
    [0.76666667],
    [0.6],
    [0.56666667],
    [0.63333333],
    [0.56666667],
    [0.63333333],
    [0.56666667],
    [0.6],
    [0.6],
]

a3 = [
    [0.0],
    [0.6],
    [0.5],
    [0.73333333],
    [0.7],
    [0.66666667],
    [0.66666667],
    [0.63333333],
    [0.7],
    [0.7],
    [0.66666667],
    [0.63333333],
]

a4 = [
    [0.0],
    [0.86666667],
    [0.8],
    [0.86666667],
    [0.8],
    [0.86666667],
    [0.83333333],
    [0.86666667],
    [0.86666667],
    [0.86666667],
    [0.86666667],
    [0.83333333],
]

a5 = [
    [0.0],
    [0.63333333],
    [0.73333333],
    [0.7],
    [0.73333333],
    [0.73333333],
    [0.7],
    [0.66666667],
    [0.66666667],
    [0.66666667],
    [0.66666667],
    [0.7],
]


plt.figure(figsize=(4, 4))
plt.grid(linestyle="--")
plt.plot(time, a1, markersize=6, marker="v", label="Task {}".format(1))
plt.plot(time, a2, markersize=6, marker="^", label="Task {}".format(2))
plt.plot(time, a3, markersize=6, marker="o", label="Task {}".format(3))
plt.plot(time, a4, markersize=6, marker="x", label="Task {}".format(4))
plt.plot(time, a5, markersize=6, marker="s", label="Task {}".format(5))
plt.legend()
plt.xlabel("Time")
plt.ylabel("Accuracy")
plt.ylim(0.2, 1)
plt.savefig("HFedMTL_task.pdf")
plt.show()
