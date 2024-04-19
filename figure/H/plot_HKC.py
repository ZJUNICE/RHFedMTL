import matplotlib.pyplot as plt

resource = [0, 200, 400, 600, 800, 1000, 1200, 1400, 1600, 1800]
RH = [
    0,
    10,
    30,
    50,
    51,
    51,
    51,
    36,
    2,
    6,
]
RK = [
    0,
    1,
    1,
    1,
    1,
    1,
    1,
    3,
    13,
    11,
]

FH = [
    0,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
]
FK = [
    0,
    2,
    4,
    5,
    7,
    9,
    10,
    12,
    14,
    15,
]

# 创建图层
fig, ax1 = plt.subplots()

# 设置左侧Y轴对应的figure
ax1.set_ylabel("$H$")
ax1.set_xlabel("$C_{j,bud}$")


ax1.plot(
    resource,
    RH,
    color="red",
    linestyle="-",
    marker="v",
    label="RHFedMTL $H$",
)
ax1.plot(
    resource,
    FH,
    color="red",
    linestyle="--",
    marker="o",
    label="HFedMTL $H$",
)
ax1.set_xticklabels(ax1.get_xticklabels())  # 设置共用的X轴

# 设置右侧Y轴对应的figure
ax2 = ax1.twinx()
ax2.set_ylabel("K")

ax2.plot(
    resource,
    RK,
    color="blue",
    linestyle="-",
    marker="v",
    label="RHFedMTL $K$",
)
ax2.plot(
    resource,
    FK,
    color="blue",
    linestyle="--",
    marker="o",
    label="HFedMTL $K$",
)

lines = []
labels = []
axes = [ax1, ax2]
for ax in axes:
    axLine, axLabel = ax.get_legend_handles_labels()
    lines.extend(axLine)
    labels.extend(axLabel)
fig.legend(
    lines, labels, loc="upper left", bbox_to_anchor=(0.1, 0.95)
)  # 图例的位置，bbox_to_anchor=(0.5, 0.92)


plt.tight_layout()
plt.savefig("allH.pdf")
plt.show()
