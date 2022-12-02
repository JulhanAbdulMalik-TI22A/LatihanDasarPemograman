print("------------------------------------------------------")
print("----------- Latihan 7 - Julhan Abdul Malik -----------")
print("------------------------------------------------------")

print("\n======================================================")
print("============ Program Kalkulator Sederhana ============")
print("======================================================")

while (True):
    print(" \n========================================")
    print("Menu")
    print(" 1. Hitung Luas Segitiga")
    print(" 2. Hitung Luas Persegi Panjang")
    print(" 3. Tentukan number ganjil genap")
    print(" 4. Quit")

    print(" \n----------------------------------------")

    listMenu = input("Masukan Pilihan : ")

    if listMenu == "1":
        print("Menu -- Hitung Luas Segitiga")
        alas = float(input("\nMasukan Panjang Alas : "))
        tinggi = float(input("Masukan Tinggi : "))

        rumus1 = 1/2 * alas * tinggi
        print("\nLuas Segitiga : ", rumus1)
        print("\n=== === === === ===")

    elif listMenu == "2":
        print("Menu -- Hitung Luas Persegi Panjang")
        panjang = float(input("\nMasukan Panjang : "))
        lebar = float(input("Masukan Lebar : "))

        rumus2 = panjang * lebar
        print("\nLuas Persegi Panjang : ", rumus2)
        print("\n=== === === === ===")

    elif listMenu == "3":
        print("Menu -- Tentukan number ganjil genap")
        angka = int(input("\nMasukan Angka : "))

        if (angka % 2 == 0):
            print("\nAngka", angka, "merupakan angka Genap.")
        else:
            print("\nAngka", angka, "merupakan angka Ganjil.")

        print("\n=== === === === ===")

    else:
        print("\nTerima kasih ... byJulhan")
        print("--- --- --- --- ---")
        break
