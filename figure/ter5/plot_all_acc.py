import matplotlib.pyplot as plt

resource = [0, 200, 400, 600, 800, 1000, 1200, 1400, 1600]
R5 = [
    0,
    0.7,
    0.733333333,
    0.72,
    0.72,
    0.733333333,
    0.773333333,
    0.78,
    0.74,
]
H5 = [
    0,
    0.68,
    0.62,
    0.633333333,
    0.713333333,
    0.653333333,
    0.68,
    0.74,
    0.7,
]
F5 = [
    0,
    0.54,
    0.58,
    0.546666667,
    0.613333333,
    0.586666667,
    0.56,
    0.553333333,
    0.546666667,
]

R10 = [
    0,
    0.706666667,
    0.72,
    0.713333333,
    0.72,
    0.726666667,
    0.733333333,
    0.746666667,
    0.713333333,
]
H10 = [
    0,
    0.653333333,
    0.673333333,
    0.72,
    0.7,
    0.713333333,
    0.673333333,
    0.726666667,
    0.72,
]
F10 = [
    0,
    0.546666667,
    0.573333333,
    0.533333333,
    0.526666667,
    0.546666667,
    0.54,
    0.573333333,
    0.6,
]

R15 = [
    0,
    0.68,
    0.68,
    0.706666667,
    0.706666667,
    0.713333333,
    0.713333333,
    0.72,
    0.68,
]
H15 = [
    0,
    0.666666667,
    0.686666667,
    0.7,
    0.713333333,
    0.68,
    0.706666667,
    0.666666667,
    0.686666667,
]
F15 = [
    0,
    0.586666667,
    0.6,
    0.64,
    0.626666667,
    0.62,
    0.64,
    0.7,
    0.72,
]


# fig = plt.figure(figsize=(5, 5))
# 设置柱形的间隔
width = 0.3  # 柱形的宽度
x1_list = []
x2_list = []
x3_list = []

plt.figure()
plt.plot(resource, R5, color="red", linestyle="-", marker="v", label="RHFedMTL $N_b$=5")
plt.plot(
    resource, R10, color="red", linestyle="--", marker="o", label="RHFedMTL $N_b$=10"
)
plt.plot(
    resource, R15, color="red", linestyle="-.", marker="^", label="RHFedMTL $N_b$=15"
)

plt.plot(resource, H5, color="blue", linestyle="-", marker="v", label="HFedMTL $N_b$=5")
plt.plot(
    resource, H10, color="blue", linestyle="--", marker="o", label="HFedMTL $N_b$=10"
)
plt.plot(
    resource, H15, color="blue", linestyle="-.", marker="^", label="HFedMTL $N_b$=15"
)

plt.plot(resource, F5, color="green", linestyle="-", marker="v", label="FedAVG $N_b$=5")
plt.plot(
    resource, F10, color="green", linestyle="--", marker="o", label="FedAVG $N_b$=10"
)
plt.plot(
    resource, F15, color="green", linestyle="-.", marker="^", label="FedAVG $N_b$=15"
)

plt.xlabel("Resource Budget")
plt.ylabel("Accuracy")
plt.legend()
plt.tight_layout()
plt.savefig("all_acc.pdf")
plt.show()
