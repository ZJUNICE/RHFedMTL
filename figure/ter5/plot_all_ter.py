import matplotlib.pyplot as plt

resource = [400, 1400]


ter = [5, 8, 10, 12, 15]

R = [
    [0.74, 0.675, 0.74, 0.6888888888888889, 0.7333333333333333],
    [0.76, 0.71875, 0.7533333333333333, 0.7222222222222222, 0.7333333333333333],
]
H = [
    [0.65, 0.68125, 0.66, 0.6722222222222223, 0.6733333333333333],
    [0.7, 0.68125, 0.7133333333333334, 0.6722222222222223, 0.6666666666666667],
]
F = [
    [0.58, 0.5875, 0.5133333333333334, 0.5722222222222222, 0.62],
    [0.58, 0.59375, 0.5533333333333335, 0.611111111111111, 0.6799999999999999],
]
P = [
    [0.56, 0.59375, 0.5399999999999999, 0.6222222222222222, 0.6133333333333333],
    [0.56, 0.61875, 0.5599999999999999, 0.6111111111111112, 0.72],
]
E = [
    [0.5933333333333334, ],
    [0.6266666666666667, ]
]

for i in range(len(resource)):
    plt.figure(figsize=(4, 4))
    plt.plot(
        ter,
        R[i],
        color="red",
        linestyle="-",
        linewidth=2,
        marker="v",
        markersize=8,
        label="RHFedMTL",
    )

    plt.plot(
        ter,
        H[i],
        color="blue",
        linestyle="--",
        linewidth=2,
        markersize=8,
        marker="o",
        label="HFedMTL",
    )

    plt.plot(
        ter,
        P[i],
        color="purple",
        linestyle="-.",
        linewidth=2,
        markersize=8,
        marker="s",
        label="FedProx",
    )
    plt.plot(
        ter,
        F[i],
        color="green",
        linestyle="-.",
        linewidth=2,
        markersize=8,
        marker="^",
        label="FedAvg",
    )
    plt.xlabel("$N_b$")
    plt.ylabel("Accuracy")
    plt.ylim(0.35, 0.8)
    plt.legend()
    plt.tight_layout()
    plt.savefig(str(resource[i]) + "ter.pdf")
    plt.show()
