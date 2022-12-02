print("------------------------------------------------------")
print("-------------- UTS - Julhan Abdul Malik --------------")

print("\n======================================================")
print("======= Program Mengitung Ruang Datar & Bangun =======")
print("======================================================")

while (True):
    print(" \n========================================")
    print("Menu")
    print(" 1. Ruang Datar")
    print(" 2. Ruang Bangun")

    print(" \n----------------------------------------")

    listMenu1 = input("Masukan Pilihan : ")
    if listMenu1 == "1":
        print("Menu -> Ruang Datar")

        print("\n 1. Persegi")
        print(" 2. Persegi Panjang")
        print(" 3. Jajar Genjang")
        print(" 4. Segitiga")
        print(" 5. Belah Ketupat")
        print(" 6. Layang-layang")
        print(" 7. Trapesium")
        print(" 8. Lingkaran")

        print(" \n----------------------------------------")

        listMenu2 = input("Masukan Pilihan : ")

        if listMenu2 == "1":
            print("Menu -> Ruang Datar -> Persegi")
            sisi = float(input("\nMasukan Sisi : "))

            ruangDatar_rumus1 = sisi ** 2
            ruangDatar_rumus1_keliling = 4 * sisi

            print("\nLuas Persegi : ", ruangDatar_rumus1)
            print("Keliling Persegi : ", ruangDatar_rumus1_keliling)
            print("\n=== === === === ===")

        elif listMenu2 == "2":
            print("Menu -> Ruang Datar -> Persegi Panjang")
            panjang = float(input("\nMasukan Panjang : "))
            lebar = float(input("Masukan Lebar : "))

            ruangDatar_rumus2 = panjang * lebar
            ruangDatar_rumus2_keliling = (2 * (panjang + lebar))

            print("\nLuas Persegi Panjang : ", ruangDatar_rumus2)
            print("keliling Persegi Panjang : ", ruangDatar_rumus2_keliling)
            print("\n=== === === === ===")

        elif listMenu2 == "3":
            print("Menu -> Ruang Datar -> Jajar Genjang")
            alas = float(input("\nMasukan Alas : "))
            tinggi = float(input("Masukan Tinggi : "))

            ruangDatar_rumus3 = alas * tinggi
            ruangDatar_rumus3_keliling = (2 * (alas + tinggi))

            print("\nLuas Jajar Genjang : ", ruangDatar_rumus3)
            print("Keliling Jajar Genjang : ", ruangDatar_rumus3_keliling)
            print("\n=== === === === ===")

        elif listMenu2 == "4":
            print("Menu -> Ruang Datar -> Segitiga")
            alas = float(input("\nMasukan Alas : "))
            tinggi = float(input("Masukan Tinggi : "))

            ruangDatar_rumus4 = 1/2 * alas * tinggi
            print("\nLuas Segitiga : ", ruangDatar_rumus4)
            print("\n=== === === === ===")

        elif listMenu2 == "5":
            print("Menu -> Ruang Datar -> Belah Ketupat")
            d1 = float(input("\nMasukan Diagonal 1 : "))
            d2 = float(input("Masukan Diagonal 2 : "))

            ruangDatar_rumus5 = 0.5 * d1 * d2
            print("\nLuas Belah Ketupat : ", ruangDatar_rumus5)
            print("\n=== === === === ===")

        elif listMenu2 == "6":
            print("Menu -> Ruang Datar -> Layang-layang")
            d1 = float(input("\nMasukan Diagonal 1 : "))
            d2 = float(input("Masukan Diagonal 2 : "))

            ruangDatar_rumus6 = 0.5 * d1 * d2
            print("\nLuas Layang-layang : ", ruangDatar_rumus6)
            print("\n=== === === === ===")

        elif listMenu2 == "7":
            print("Menu -> Ruang Datar -> Trapesium")
            alasA = float(input("\nMasukan Alas A : "))
            alasB = float(input("Masukan Alas B : "))
            tinggi = float(input("Masukan Tinggi : "))

            ruangDatar_rumus7 = (1/2 * (alasA + alasB) * tinggi)
            print("\nLuas Trapesium : ", ruangDatar_rumus7)
            print("\n=== === === === ===")

        elif listMenu2 == "8":
            print("Menu -> Ruang Datar -> Lingkaran")
            jariLingkaran = float(input("\nMasukan Jari-jari : "))

            ruangDatar_rumus8 = 3.14 * jariLingkaran * jariLingkaran
            ruangDatar_rumus8_keliling = 3.14 * jariLingkaran * 2

            print("\nLuas Lingkaran : ", ruangDatar_rumus8)
            print("Keliling Lingkaran : ", ruangDatar_rumus8_keliling)
            print("\n=== === === === ===")

        else:
            print("\nMaaf input anda Salah - By Julhan")

    elif listMenu1 == "2":
        print("Menu -> Ruang Bangun")

        print("\n 1. Kubus")
        print(" 2. Balok")
        print(" 3. Prisma Segitiga")
        print(" 4. Limas Segiempat")
        print(" 5. Limas Segitiga")
        print(" 6. Tabung")
        print(" 7. Kerucut")
        print(" 8. Bola")

        print(" \n----------------------------------------")

        listMenu2 = input("Masukan Pilihan : ")

        if listMenu2 == "1":
            print("Menu -> Ruang Bangun -> Kubus")
            sisi = float(input("\nMasukan Sisi : "))

            ruangBangun_rumus1 = 6 * sisi ** 2
            print("\nLuas Kubus : ", ruangBangun_rumus1)
            print("\n=== === === === ===")

        elif listMenu2 == "2":
            print("Menu -> Ruang Bangun -> Balok")
            panjang = float(input("\nMasukan Panjang : "))
            lebar = float(input("Masukan Lebar : "))
            tinggi = float(input("Masukan Tinggi : "))

            ruangBangun_rumus2 = (
                2 * ((panjang * lebar) + (panjang * tinggi) + (lebar * tinggi)))
            print("\nLuas Balok : ", ruangBangun_rumus2)
            print("\n=== === === === ===")

        else:
            print("\nMaaf input anda Salah - By Julhan")

    else:
        print("\nMaaf input anda Salah - By Julhan")

    apakahLanjut = input("\nApakah mau menghitung Kembali? Y or N : ")
    if (apakahLanjut != 'y'):

        print("\nTerima Kasih ... By Julhan :)")

        print("\n=== === === === ===")
        break
