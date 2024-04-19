import matplotlib.pyplot as plt

resource = [0, 200, 400, 600, 800, 1000, 1200, 1400, 1600]
R1 = [
    0,
    0.686666667,
    0.726666667,
    0.706666667,
    0.746666667,
    0.753333333,
    0.74,
    0.746666667,
    0.726666667,
]
H1 = [
    0,
    0.673333333,
    0.686666667,
    0.713333333,
    0.68,
    0.746666667,
    0.686666667,
    0.72,
    0.733333333,
]
F1 = [
    0,
    0.473333333,
    0.506666667,
    0.533333333,
    0.586666667,
    0.566666667,
    0.573333333,
    0.6,
    0.586666667,
]

R2 = [
    0,
    0.706666667,
    0.726666667,
    0.693333333,
    0.72,
    0.746666667,
    0.726666667,
    0.76,
    0.733333333,
]
H2 = [
    0,
    0.68,
    0.686666667,
    0.686666667,
    0.693333333,
    0.713333333,
    0.7,
    0.74,
    0.726666667,
]
F2 = [
    0,
    0.493333333,
    0.553333333,
    0.593333333,
    0.553333333,
    0.58,
    0.6,
    0.58,
    0.58,
]

R3 = [
    0,
    0.726666667,
    0.726666667,
    0.7,
    0.693333333,
    0.746666667,
    0.726666667,
    0.753333333,
    0.74,
]
H3 = [
    0,
    0.653333333,
    0.7,
    0.706666667,
    0.693333333,
    0.713333333,
    0.68,
    0.753333333,
    0.72,
]
F3 = [
    0,
    0.486666667,
    0.466666667,
    0.54,
    0.56,
    0.553333333,
    0.58,
    0.613333333,
    0.606666667,
]

plt.figure()
plt.plot(
    resource,
    R1,
    color="red",
    linestyle="-",
    marker="v",
    label="RHFedMTL $C_{j,dev}$=0.05",
)
plt.plot(
    resource,
    R2,
    color="red",
    linestyle="--",
    marker="o",
    label="RHFedMTL $C_{j,dev}$=0.1",
)
plt.plot(
    resource,
    R3,
    color="red",
    linestyle="-.",
    marker="^",
    label="RHFedMTL $C_{j,dev}$=0.2",
)

plt.plot(
    resource,
    H1,
    color="blue",
    linestyle="-",
    marker="v",
    label="HFedMTL $C_{j,dev}$=0.05",
)
plt.plot(
    resource,
    H2,
    color="blue",
    linestyle="--",
    marker="o",
    label="HFedMTL $C_{j,dev}$=0.1",
)
plt.plot(
    resource,
    H3,
    color="blue",
    linestyle="-.",
    marker="^",
    label="HFedMTL $C_{j,dev}$=0.2",
)

plt.plot(
    resource,
    F1,
    color="green",
    linestyle="-",
    marker="v",
    label="FedAVG $C_{j,dev}$=0.05",
)
plt.plot(
    resource,
    F2,
    color="green",
    linestyle="--",
    marker="o",
    label="FedAVG $C_{j,dev}$=0.1",
)
plt.plot(
    resource,
    F3,
    color="green",
    linestyle="-.",
    marker="^",
    label="FedAVG $C_{j,dev}$=0.2",
)

plt.xlabel("Resource Budget")
plt.ylabel("Accuracy")
plt.legend()
plt.tight_layout()
plt.savefig("all_Cdev_acc.pdf")
plt.show()
