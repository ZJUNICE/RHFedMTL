import matplotlib.pyplot as plt

l2 = ["$1x10^{-12}$", "$1x10^{-8}$", "$1x10^{-6}$", "$1x10^{-4}$", "$1x10^{-2}$"]

R = [
    0.7,
    0.74,
    0.7866666666666666,
    0.76,
    0.7533333333333334,
]

plt.figure(figsize=(4, 4))
plt.bar(range(len(R)), R, width=0.7, tick_label=l2)
# plt.xlabel("$\lambda_{2}$")
plt.ylabel("Accuracy")
plt.ylim(0.3, 0.85)
plt.savefig("lambda2.pdf")
plt.show()
