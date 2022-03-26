for tahun in range(1998, 2023):
    if (tahun % 4) == 0:
        if (tahun % 100) == 0:
            if (tahun % 400) == 0:
                print(tahun, "Tahun Kabisat")
            else:
                print(tahun, "Bukan Tahun Kabisat")
        else:
            print(tahun, "Tahun Kabisat")
    else:
        print(tahun, "Bukan Tahun Kabisat")
