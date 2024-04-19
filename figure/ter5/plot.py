import matplotlib.pyplot as plt

resource = [0, 200, 400, 600, 800, 1000, 1200, 1400, 1600, 1800]
R = [
    0,
    0.7333333333333334,
    0.7133333333333334,
    0.7266666666666667,
    0.7266666666666667,
    0.7133333333333333,
    0.7466666666666667,
    0.7466666666666667,
    0.7133333333333334,
    0.7533333333333333,
]
H = [
    0,
    0.6333333333333333,
    0.6333333333333333,
    0.6333333333333333,
    0.6866666666666666,
    0.6866666666666666,
    0.6866666666666666,
    0.68,
    0.68,
    0.68,
]
F = [
    0,
    0.5,
    0.5,
    0.5,
    0.5133333333333334,
    0.5133333333333334,
    0.5133333333333334,
    0.5333333333333334,
    0.5333333333333334,
    0.5333333333333334,
]

# fig = plt.figure(figsize=(5, 5))
# 设置柱形的间隔
width = 0.3  # 柱形的宽度
x1_list = []
x2_list = []
x3_list = []

for i in range(len(H)):
    x1_list.append(i)
    x2_list.append(i + width)
    x3_list.append(i + 2 * width)

# 创建图层
fig, ax1 = plt.subplots()

# 设置左侧Y轴对应的figure
ax1.set_ylabel("Cost")
ax1.set_xlabel("H")

# ax1.set_ylim(0, 1)
plt.bar(x1_list, R, width=width, color="tab:blue", align="edge", label="RHFedMTL")
plt.bar(
    x2_list,
    H,
    width=width,
    color="tab:green",
    align="edge",
    label="HFedMTL",
    tick_label=resource,
)
plt.bar(x3_list, F, width=width, color="tab:brown", align="edge", label="FedAVG")

# lines = []
# labels = []
# axes = [ax1, ax2]
# for ax in axes:
#     axLine, axLabel = ax.get_legend_handles_labels()
#     lines.extend(axLine)
#     labels.extend(axLabel)
# fig.legend(
#     lines, labels, loc="upper right", bbox_to_anchor=(0.9, 0.95)
# )  # 图例的位置，bbox_to_anchor=(0.5, 0.92)
plt.legend()
plt.tight_layout()
plt.savefig("BS=20.pdf")
plt.show()
