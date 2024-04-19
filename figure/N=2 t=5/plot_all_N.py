import matplotlib.pyplot as plt

resource = [400, 1400]


N = [2, 5, 8, 12, 15]

R = [
    [
        0.6266666666666667,
        0.74,
        0.63125,
        0.6444444444444444,
        0.6466666666666666,
    ],
    [0.64, 0.76, 0.6125, 0.6222222222222222, 0.6733333333333333],
]
H = [
    [0.6, 0.6533333333333333, 0.5875, 0.6277777777777778, 0.6333333333333334],
    [0.6066666666666667, 0.7, 0.5875, 0.5944444444444443, 0.6266666666666667],
]
F = [
    [
        0.6466666666666666,
        0.5866666666666667,
        0.51875,
        0.5611111111111111,
        0.62,
    ],
    [
        0.5733333333333334,
        0.5866666666666667,
        0.58125,
        0.5888888888888888,
        0.5866666666666667,
    ],
]
P = [
    [
        0.6333333333333333,
        0.56,
        0.50625,
        0.5666666666666667,
        0.6333333333333333,
    ],
    [
        0.6933333333333334,
        0.5666666666666667,
        0.6375,
        0.6388888888888888,
        0.6466666666666666,
    ],
]
E = [
    [
        0.6,
        0.5933333333333334,
        0.525,
        0.6055555555555556,
        0.6055555555555556
    ],
    [
        0.68,
        0.6266666666666667,
        0.5687500000000001,
        0.6055555555555556,
        0.6055555555555556
    ]
]

for i in range(len(resource)):
    plt.figure(figsize=(4, 4))
    plt.plot(
        N,
        R[i],
        color="red",
        linestyle="-",
        linewidth=2,
        markersize=8,
        marker="v",
        label="RHFedMTL",
    )

    plt.plot(
        N,
        H[i],
        color="blue",
        linestyle="--",
        marker="o",
        linewidth=2,
        markersize=8,
        label="HFedMTL",
    )
    plt.plot(
        N,
        P[i],
        color="purple",
        linestyle="-.",
        linewidth=2,
        markersize=8,
        marker="s",
        label="FedProx",
    )
    plt.plot(
        N,
        F[i],
        color="green",
        linestyle="-.",
        marker="^",
        linewidth=2,
        markersize=8,
        label="FedAvg",
    )
    # plt.plot(
    #     N,
    #     E[i],
    #     color="darkorange",
    #     linestyle="-.",
    #     marker="^",
    #     linewidth=2,
    #     markersize=8,
    #     label="FedEM",
    # )
    plt.xlabel("$N$")
    plt.ylabel("Accuracy")
    plt.ylim(0.35, 0.8)
    plt.xlim(1.2, 16)
    plt.legend(loc="lower left")
    plt.tight_layout()
    plt.savefig(str(resource[i]) + "N.pdf")
    plt.show()
