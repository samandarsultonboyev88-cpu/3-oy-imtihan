mahsulotlar = {"non": 4000, "sut": 12000, "olma": 8000}

nomi = input("Mahsulotlar nomi: ").strip().lower()
yangi_narx = int(input("yangi narh: "))

if nomi in mahsulotlar:
    mahsulotlar[nomi] = yangi_narx
    print("Narx yangilandi:")
    print(mahsulotlar)
else:
    print("Bunday maxsulot mavjud emas")