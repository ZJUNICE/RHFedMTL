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
    280.0,
    390.0,
    520.0,
    600.0,
    720.0,
    770.0,
    880.0,
    900.0,
    1000.0,
    990.0,
    1080.0,
    1170.0,
    1120.0,
    1200.0,
    1280.0,
    1190.0,
    1260.0,
    1330.0,
    1400.0,
    1260.0,
    1320.0,
    1380.0,
    1200.0,
    1250.0,
    1300.0,
    1350.0,
    1400.0,
    1160.0,
    1200.0,
    1240.0,
    1280.0,
    1320.0,
    1360.0,
    1050.0,
    1080.0,
    1110.0,
    1140.0,
    1170.0,
    1200.0,
    1230.0,
    840.0,
    860.0,
    880.0,
    900.0,
    920.0,
    940.0,
    960.0,
    980.0,
    1000.0,
    1020.0,
    520.0,
    530.0,
    540.0,
    550.0,
    560.0,
    570.0,
    580.0,
    590.0,
    600.0,
    610.0,
    620.0,
    630.0,
    640.0,
    650.0,
    660.0,
    670.0,
    680.0,
    690.0,
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
ax1.set_ylabel("Cost")
ax1.set_xlabel("H")

# ax1.set_ylim(0, 1)
ax1.bar(x1_list, Cost, width=width, color="tab:green", align="edge", label="Cost")

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
plt.savefig("BS=1.pdf")
plt.show()
