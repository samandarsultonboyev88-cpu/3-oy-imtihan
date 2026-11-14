def natija(sonlar):

    juft_son = sum(x for x in sonlar if x % 2 == 0)
    toq_son = sum(x for x in sonlar if x % 2 != 0)
    katta_son = max(sonlar)

    print("SJuft sonlar yigindisi:", juft_son)
    print("Toq sonlar yigindisi:", toq_son)
    print("Eng katta son:", katta_son)

sonlar = [12, 7, 5, 18, 9, 4]

natija(sonlar)