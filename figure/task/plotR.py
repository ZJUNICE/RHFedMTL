import matplotlib.pyplot as plt

time = [
    0,
    51,
    102,
    153,
    204,
    255,
    306,
    357,
    408,
    459,
]

a1 = [
    0,
    0.63,
    0.7,
    0.7,
    0.8,
    0.833,
    0.83,
    0.93,
    0.9,
    0.93,
]

a2 = [
    [0.0],
    [0.6],
    [0.63333333],
    [0.7],
    [0.76666667],
    [0.66666667],
    [0.76666667],
    [0.66666667],
    [0.73333333],
    [0.76666667],
]

a3 = [
    [0.0],
    [0.63333333],
    [0.6],
    [0.6],
    [0.66666667],
    [0.66666667],
    [0.66666667],
    [0.66666667],
    [0.63333333],
    [0.63333333],
]

a4 = [
    [0.0],
    [0.86666667],
    [0.9],
    [0.86666667],
    [0.86666667],
    [0.86666667],
    [0.86666667],
    [0.86666667],
    [0.86666667],
    [0.86666667],
]

a5 = [
    [0.0],
    [0.7],
    [0.7],
    [0.7],
    [0.7],
    [0.7],
    [0.7],
    [0.7],
    [0.7],
    [0.76666667],
]

a = [a1, a2, a3, a4, a5]

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
plt.savefig("RHFedMTL_task.pdf")
plt.show()
