import csv 

mahsulotlar = [
    ["Olma", 8000, 12],
    ["Non", 4000, 20],
    ["Sut", 14000, 5]
]

with open("products.csv", "a", newline="") as f:
    writer = csv.writer(f, delimiter=",")

    writer.writerow(["nom", "narx", "son"])

    writer.writerows(mahsulotlar)
    
    print("Maxsulotlar saqlandi")