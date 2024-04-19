import matplotlib.pyplot as plt

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
    46,
    47,
    48,
    49,
    50,
    51,
    52,
    53,
    54,
    55,
    56,
    57,
    58,
    59,
    60,
    61,
    62,
    63,
    64,
    65,
    66,
    67,
    68,
]

K = [
    14,
    13,
    13,
    12,
    12,
    11,
    11,
    10,
    10,
    9,
    9,
    9,
    8,
    8,
    8,
    7,
    7,
    7,
    7,
    6,
    6,
    6,
    5,
    5,
    5,
    5,
    5,
    4,
    4,
    4,
    4,
    4,
    4,
    3,
    3,
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
    1,
    1,
    1,
    1,
    1,
    1,
]

Cost = [
    2940.0,
    2860.0,
    2990.0,
    2880.0,
    3000.0,
    2860.0,
    2970.0,
    2800.0,
    2900.0,
    2700.0,
    2790.0,
    2880.0,
    2640.0,
    2720.0,
    2800.0,
    2520.0,
    2590.0,
    2660.0,
    2730.0,
    2400.0,
    2460.0,
    2520.0,
    2150.0,
    2200.0,
    2250.0,
    2300.0,
    2350.0,
    1920.0,
    1960.0,
    2000.0,
    2040.0,
    2080.0,
    2120.0,
    1620.0,
    1650.0,
    1680.0,
    1710.0,
    1740.0,
    1770.0,
    1800.0,
    1220.0,
    1240.0,
    1260.0,
    1280.0,
    1300.0,
    1320.0,
    1340.0,
    1360.0,
    1380.0,
    1400.0,
    710.0,
    720.0,
    730.0,
    740.0,
    750.0,
    760.0,
    770.0,
    780.0,
    790.0,
    800.0,
    810.0,
    820.0,
    830.0,
    840.0,
    850.0,
    860.0,
    870.0,
    880.0,
]

# fig = plt.figure(figsize=(5, 5))
# 设置柱形的间隔
width = 0.4  # 柱形的宽度
x1_list = []
x2_list = []

for i in range(len(H)):
    x1_list.append(i)
    x2_list.append(i + width)


# 创建图层
fig, ax1 = plt.subplots()

# 设置左侧Y轴对应的figure
ax1.set_ylabel("$C_{j,tol}$")
ax1.set_xlabel("H")

# ax1.set_ylim(0, 1)
ax1.bar(
    x1_list, Cost, width=width, color="tab:green", align="edge", label="$C_{j,tol}$"
)

ax1.set_xticklabels(ax1.get_xticklabels())  # 设置共用的x轴

# 设置右侧Y轴对应的figure
ax2 = ax1.twinx()
ax2.set_ylabel("K")
# ax2.set_ylim(0, 0.5)
ax2.bar(x2_list, K, width=width, color="tab:blue", align="edge", label="K")

lines = []
labels = []
axes = [ax1, ax2]
for ax in axes:
    axLine, axLabel = ax.get_legend_handles_labels()
    lines.extend(axLine)
    labels.extend(axLabel)
fig.legend(
    lines, labels, loc="upper right", bbox_to_anchor=(0.9, 0.95)
)  # 图例的位置，bbox_to_anchor=(0.5, 0.92)

plt.tight_layout()
plt.savefig("BS=20.pdf")
plt.show()
