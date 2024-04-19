import matplotlib.pyplot as plt

resource = [0, 200, 400, 600, 800, 1000, 1200, 1400, 1600]
R2 = [
    0,
    0.606666667,
    0.626666667,
    0.633333333,
    0.626666667,
    0.653333333,
    0.653333333,
    0.66,
    0.66,
]
H2 = [
    0,
    0.646666667,
    0.593333333,
    0.58,
    0.626666667,
    0.613333333,
    0.606666667,
    0.613333333,
    0.593333333,
]
F2 = [
    0,
    0.586666667,
    0.393333333,
    0.566666667,
    0.686666667,
    0.473333333,
    0.606666667,
    0.566666667,
    0.626666667,
]

R5 = [
    0,
    0.673333333,
    0.733333333,
    0.733333333,
    0.726666667,
    0.746666667,
    0.733333333,
    0.746666667,
    0.746666667,
]
H5 = [
    0,
    0.653333333,
    0.706666667,
    0.673333333,
    0.693333333,
    0.673333333,
    0.693333333,
    0.66,
    0.713333333,
]
F5 = [
    0,
    0.526666667,
    0.533333333,
    0.573333333,
    0.586666667,
    0.613333333,
    0.646666667,
    0.573333333,
    0.586666667,
]

R15 = [
    0,
    0.653333333,
    0.646666667,
    0.64,
    0.66,
    0.653333333,
    0.666666667,
    0.633333333,
    0.66,
]
H15 = [
    0,
    0.64,
    0.546666667,
    0.666666667,
    0.626666667,
    0.64,
    0.653333333,
    0.666666667,
    0.64,
]
F15 = [
    0,
    0.493333333,
    0.553333333,
    0.553333333,
    0.586666667,
    0.54,
    0.56,
    0.58,
    0.613333333,
]


# fig = plt.figure(figsize=(5, 5))
# 设置柱形的间隔
width = 0.3  # 柱形的宽度
x1_list = []
x2_list = []
x3_list = []

plt.figure()
plt.plot(resource, R2, color="red", linestyle="-", marker="v", label="RHFedMTL $N$=2")
plt.plot(resource, R5, color="red", linestyle="--", marker="o", label="RHFedMTL $N$=5")
plt.plot(
    resource, R15, color="red", linestyle="-.", marker="^", label="RHFedMTL $N$=15"
)

plt.plot(resource, H2, color="blue", linestyle="-", marker="v", label="HFedMTL $N$=2")
plt.plot(resource, H5, color="blue", linestyle="--", marker="o", label="HFedMTL $N$=5")
plt.plot(
    resource, H15, color="blue", linestyle="-.", marker="^", label="HFedMTL $N$=15"
)

plt.plot(resource, F2, color="green", linestyle="-", marker="v", label="FedAVG $N$=2")
plt.plot(resource, F5, color="green", linestyle="--", marker="o", label="FedAVG $N$=5")
plt.plot(
    resource, F15, color="green", linestyle="-.", marker="^", label="FedAVG $N$=15"
)

plt.xlabel("Resource Budget")
plt.ylabel("Accuracy")
plt.legend()
plt.tight_layout()
plt.savefig("all_N_acc.pdf")
plt.show()
