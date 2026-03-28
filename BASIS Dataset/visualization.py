import matplotlib.pyplot as plt

nodes = [10, 25, 50, 75, 100]

basis = [25, 45, 70, 85, 95]
mlbsa = [20, 35, 48, 55, 60]
biim = [18, 30, 42, 50, 54]
cbipf = [22, 38, 52, 58, 63]

plt.plot(nodes, basis, label="BASIS")
plt.plot(nodes, mlbsa, label="MLBSA")
plt.plot(nodes, biim, label="BIIM")
plt.plot(nodes, cbipf, label="CBIPF")

plt.xlabel("IoT Nodes")
plt.ylabel("TPS")
plt.legend()
plt.savefig("../results/tps.png")
plt.show()