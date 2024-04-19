import matplotlib.pyplot as plt
import numpy as np

# Prepare Data
H = [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    11,
    12,
    13,
    14,
    15,
    16,
    17,
    18,
    19,
    20,
    21,
    22,
    23,
    24,
    25,
    26,
    27,
    28,
    29,
    30,
    31,
    32,
    33,
    34,
    35,
    36,
    37,
    38,
    39,
    40,
    41,
    42,
    43,
    44,
    45,
]
K = [
    13,
    13,
    12,
    11,
    10,
    10,
    9,
    9,
    8,
    8,
    7,
    7,
    6,
    6,
    6,
    5,
    5,
    5,
    4,
    4,
    4,
    3,
    3,
    3,
    3,
    3,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
]
Cost = [
    1495.0,
    1690.0,
    1740.0,
    1760.0,
    1750.0,
    1900.0,
    1845.0,
    1980.0,
    1880.0,
    2000.0,
    1855.0,
    1960.0,
    1770.0,
    1860.0,
    1950.0,
    1700.0,
    1775.0,
    1850.0,
    1540.0,
    1600.0,
    1660.0,
    1290.0,
    1335.0,
    1380.0,
    1425.0,
    1470.0,
    1010.0,
    1040.0,
    1070.0,
    1100.0,
    1130.0,
    1160.0,
    1190.0,
    610.0,
    625.0,
    640.0,
    655.0,
    670.0,
    685.0,
    700.0,
    715.0,
    730.0,
    745.0,
    760.0,
    775.0,
]

x = H
y1 = K
y2 = Cost
mycolors = [
    "tab:red",
    "tab:blue",
    "tab:green",
    "tab:orange",
    "tab:brown",
    "tab:grey",
    "tab:pink",
    "tab:olive",
]
columns = ["psavert", "uempmed"]

# Draw Plot
fig, ax = plt.subplots(1, 1, figsize=(16, 9), dpi=80)
ax.fill_between(
    x, y1=y1, y2=0, label=columns[1], alpha=0.5, color=mycolors[1], linewidth=2
)
ax.fill_between(
    x, y1=y2, y2=0, label=columns[0], alpha=0.5, color=mycolors[0], linewidth=2
)

# Decorations
ax.set_title("Personal Savings Rate vs Median Duration of Unemployment", fontsize=18)
ax.set(ylim=[0, 30])
ax.legend(loc="best", fontsize=12)
plt.xticks(x[::50], fontsize=10, horizontalalignment="center")
plt.yticks(np.arange(2.5, 30.0, 2.5), fontsize=10)
plt.xlim(-10, x[-1])

# Draw Tick lines
for y in np.arange(2.5, 30.0, 2.5):
    plt.hlines(
        y, xmin=0, xmax=len(x), colors="black", alpha=0.3, linestyles="--", lw=0.5
    )

# Lighten borders
plt.gca().spines["top"].set_alpha(0)
plt.gca().spines["bottom"].set_alpha(0.3)
plt.gca().spines["right"].set_alpha(0)
plt.gca().spines["left"].set_alpha(0.3)
plt.show()
