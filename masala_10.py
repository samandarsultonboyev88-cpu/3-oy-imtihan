import matplotlib.pyplot as plt

kunlar = ["Du", "Se", "Cho", "Pay", "Ju", "Sha", "Yak"]
daromad = [120, 150, 100, 180, 200, 240, 210]

plt.plot(kunlar, daromad, color="red", marker="o", linestyle="-")

plt.title("Bir haftalik daromatlar")

plt.xlabel("Kunlar")

plt.ylabel("Daromadlar")

plt.grid(True)

plt.savefig("daaromat.png")