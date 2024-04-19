import matplotlib.pyplot as plt

resource = [400, 1400]


C = [0.07, 0.1, 0.12, 0.17, 0.2]

R = [
    [0.74, 0.7133333333333334, 0.7066666666666667, 0.72, 0.7266666666666667],
    [0.76, 0.7666666666666667, 0.76, 0.74, 0.72],
]
H = [
    [
        0.6533333333333333,
        0.6733333333333333,
        0.6533333333333333,
        0.7066666666666667,
        0.6933333333333334,
    ],
    [0.7, 0.6666666666666667, 0.72, 0.6666666666666666, 0.7000000000000001],
]
F = [
    [
        0.5866666666666667,
        0.6,
        0.5199999999999999,
        0.5266666666666666,
        0.48,
    ],
    [
        0.5866666666666667,
        0.5133333333333334,
        0.5200000000000001,
        0.6,
        0.5599999999999999,
    ],
]
P = [
    [
        0.56,
        0.5,
        0.5,
        0.5,
        0.5266666666666666,
    ],
    [
        0.5666666666666667,
        0.6,
        0.62,
        0.64,
        0.6533333333333333,
    ],
]

E = [
    [0.57, 0.56, 0.59, 0.52, 0.47],
    [0.57, 0.56, 0.55, 0.57, 0.57]
]

for i in range(len(resource)):
    plt.figure(figsize=(4, 4))
    plt.plot(
        C,
        R[i],
        color="red",
        linestyle="-",
        marker="v",
        linewidth=2,
        markersize=8,
        label="RHFedMTL",
    )

    plt.plot(
        C,
        H[i],
        color="blue",
        linestyle="--",
        marker="o",
        linewidth=2,
        markersize=8,
        label="HFedMTL",
    )
    plt.plot(
        C,
        P[i],
        color="purple",
        linestyle="-.",
        linewidth=2,
        markersize=8,
        marker="s",
        label="FedProx",
    )
    plt.plot(
        C,
        F[i],
        color="green",
        linestyle="-.",
        marker="^",
        linewidth=2,
        markersize=8,
        label="FedAvg",
    )
    plt.plot(
        C,
        E[i],
        color="darkorange",
        linestyle="-.",
        marker="^",
        linewidth=2,
        markersize=8,
        label="FedEM",
    )
    plt.xlabel("$C_{j,dev}$")
    plt.ylabel("Accuracy")
    plt.ylim(0.3, 0.8)
    # plt.xlim(1.2, 16)
    plt.legend(loc="lower left")
    plt.tight_layout()
    plt.savefig(str(resource[i]) + "C.pdf")
    plt.show()
