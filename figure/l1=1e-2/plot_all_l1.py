import matplotlib.pyplot as plt

l1 = ["$1x10^{-8}$", "$1x10^{-6}$", "$1x10^{-4}$", "$1x10^{-2}$", "$1x10^{0}$"]

R = [
    0.7066666666666667,
    0.7266666666666667,
    0.7866666666666666,
    0.7466666666666667,
    0.5599999999999999,
]


plt.figure(figsize=(4, 4))
plt.bar(range(len(R)), R, width=0.7, tick_label=l1)
# plt.xlabel("$\lambda_{1}$")
plt.ylabel("Accuracy")
plt.ylim(0.3, 0.85)
plt.savefig("lambda1.pdf")
plt.show()
