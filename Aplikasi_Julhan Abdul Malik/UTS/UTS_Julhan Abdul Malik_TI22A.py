print("------------------------------------------------------")
print("-------------- UTS - Julhan Abdul Malik --------------")

print("\n======================================================")
print("====== Program Menghitung dengan Cepat dan Mudah =====")
print("======================================================")

while (True):
    print(" \n========================================")
    print("Menu")
    print(" 1. Menghitung umur saat ini")
    print(" 2. Menghitung sisa tahun cicilan")
    print(" 3. Menghitung BMI berat badan")
    print(" 4. Quit")

    print(" \n----------------------------------------")

    listMenu = input("Masukan Pilihan : ")

    if listMenu == "1":
        print("Menu -> Menghitung umur saat ini")
        from datetime import datetime, date
        print("\nPerhatikan!")
        print("Format input tanggal lahir wajib 'dd mm yyyy', contoh '01 01 2000' ")
        tanggal_lahir = datetime.strptime(
            input("\nMasukan tanggal lahir anda : "), "%d %m %Y")

        def jul_calculation_age(born):
            today = date.today()
            return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

        umur = jul_calculation_age(tanggal_lahir)

        print("\nUmur anda saat ini adalah :", umur, "Tahun")

        print("\n*Selamat, semoga panjang umur dan berkah .. byJulhan :)")

        print("=== === === === ===")

    elif listMenu == "2":
        print("Menu -> Menghitung sisa tahun cicilan")

        print("\nBarang-barang Kredit")
        print(" 1. Laptop = Rp.10.000.000,-")
        print(" 2. Motor = Rp.20.000.000,-")
        print(" 3. Mobil = Rp.100.000.000,-")
        print(" 4. Quit")

        print(" \n----------------------------------------")

        listMenu2 = input("Masukan Pilihan : ")

        if listMenu2 == "1":
            print("Menu -> Menghitung sisa tahun cicilan -> Laptop = Rp.10.000.000,-")

            print("\nPerhatian!")
            print("Angsuran perbulan-Nya adalah Rp.833.333,- selama 12 bulan ")

            listMenu3 = input("\nBerapa bulan yang sudah dibayar : ")

            if listMenu3 == "1":
                sisa = 833.333 * 11

                print("\nAngsuran anda masih kurang Rp.", sisa, "untuk 11 bulan")
                print("\n=== === === === ===")

            elif listMenu3 == "2":
                sisa = 833.333 * 10

                print("\nAngsuran anda masih kurang Rp.", sisa, "untuk 10 bulan")
                print("\n=== === === === ===")

            elif listMenu3 == "3":
                sisa = 833.333 * 9

                print("\nAngsuran anda masih kurang Rp.", sisa, "untuk 9 bulan")
                print("\n=== === === === ===")

            elif listMenu3 == "4":
                sisa = 833.333 * 8

                print("\nAngsuran anda masih kurang Rp.", sisa, "untuk 8 bulan")
                print("\n=== === === === ===")

            elif listMenu3 == "5":
                sisa = 833.333 * 7

                print("\nAngsuran anda masih kurang Rp.", sisa, "untuk 7 bulan")
                print("\n=== === === === ===")

            elif listMenu3 == "6":
                sisa = 833.333 * 6

                print("\nAngsuran anda masih kurang Rp.", sisa, "untuk 6 bulan")
                print("\n=== === === === ===")

            elif listMenu3 == "7":
                sisa = 833.333 * 5

                print("\nAngsuran anda masih kurang Rp.", sisa, "untuk 5 bulan")
                print("\n=== === === === ===")

            elif listMenu3 == "8":
                sisa = 833.333 * 4

                print("\nAngsuran anda masih kurang Rp.", sisa, "untuk 4 bulan")
                print("\n=== === === === ===")

            elif listMenu3 == "9":
                sisa = 833.333 * 3

                print("\nAngsuran anda masih kurang Rp.", sisa, "untuk 3 bulan")
                print("\n=== === === === ===")

            elif listMenu3 == "10":
                sisa = 833.333 * 2

                print("\nAngsuran anda masih kurang Rp.", sisa, "untuk 2 bulan")
                print("\n=== === === === ===")

            elif listMenu3 == "11":
                sisa = 833.333 * 1

                print("\nAngsuran anda masih kurang Rp.", sisa, "untuk 1 bulan")
                print("\n=== === === === ===")

            else:
                print("\nMaaf input anda Salah, Terima kasih ... byJulhan")
                print("--- --- --- --- ---")

        elif listMenu2 == "2":
            print("Menu -> Menghitung sisa tahun cicilan -> Motor = Rp.20.000.000,-")

            print("\nPerhatian!")
            print("Angsuran perbulan-Nya adalah Rp.1.666.666,- selama 12 bulan ")

            listMenu3 = input("\nBerapa bulan yang sudah dibayar : ")

            if listMenu3 == "1":
                sisa = 1.666666 * 11

                print("\nAngsuran anda masih kurang Rp.", sisa, "untuk 11 bulan")
                print("\n=== === === === ===")

            elif listMenu3 == "2":
                sisa = 1.666666 * 10

                print("\nAngsuran anda masih kurang Rp.", sisa, "untuk 10 bulan")
                print("\n=== === === === ===")

            elif listMenu3 == "3":
                sisa = 1.666666 * 9

                print("\nAngsuran anda masih kurang Rp.", sisa, "untuk 9 bulan")
                print("\n=== === === === ===")

            elif listMenu3 == "4":
                sisa = 1.666666 * 8

                print("\nAngsuran anda masih kurang Rp.", sisa, "untuk 8 bulan")
                print("\n=== === === === ===")

            elif listMenu3 == "5":
                sisa = 1.666666 * 7

                print("\nAngsuran anda masih kurang Rp.", sisa, "untuk 7 bulan")
                print("\n=== === === === ===")

            elif listMenu3 == "6":
                sisa = 1.666666 * 6

                print("\nAngsuran anda masih kurang Rp.", sisa, "untuk 6 bulan")
                print("\n=== === === === ===")

            elif listMenu3 == "7":
                sisa = 1.666666 * 5

                print("\nAngsuran anda masih kurang Rp.", sisa, "untuk 5 bulan")
                print("\n=== === === === ===")

            elif listMenu3 == "8":
                sisa = 1.666666 * 4

                print("\nAngsuran anda masih kurang Rp.", sisa, "untuk 4 bulan")
                print("\n=== === === === ===")

            elif listMenu3 == "9":
                sisa = 1.666666 * 3

                print("\nAngsuran anda masih kurang Rp.", sisa, "untuk 3 bulan")
                print("\n=== === === === ===")

            elif listMenu3 == "10":
                sisa = 1.666666 * 2

                print("\nAngsuran anda masih kurang Rp.", sisa, "untuk 2 bulan")
                print("\n=== === === === ===")

            elif listMenu3 == "11":
                sisa = 1.666666 * 1

                print("\nAngsuran anda masih kurang Rp.", sisa, "untuk 1 bulan")
                print("\n=== === === === ===")

            else:
                print("\nMaaf input anda Salah, Terima kasih ... byJulhan")
                print("--- --- --- --- ---")

        elif listMenu2 == "3":
            print("Menu -> Menghitung sisa tahun cicilan -> Mobil = Rp.100.000.000,-")

            print("\nPerhatian!")
            print("Angsuran perbulan-Nya adalah Rp.8.333.333,- selama 12 bulan ")

            listMenu3 = input("\nBerapa bulan yang sudah dibayar : ")

            if listMenu3 == "1":
                sisa = 8.333333 * 11

                print("\nAngsuran anda masih kurang Rp.", sisa, "untuk 11 bulan")
                print("\n=== === === === ===")

            elif listMenu3 == "2":
                sisa = 8.333333 * 10

                print("\nAngsuran anda masih kurang Rp.", sisa, "untuk 10 bulan")
                print("\n=== === === === ===")

            elif listMenu3 == "3":
                sisa = 8.333333 * 9

                print("\nAngsuran anda masih kurang Rp.", sisa, "untuk 9 bulan")
                print("\n=== === === === ===")

            elif listMenu3 == "4":
                sisa = 8.333333 * 8

                print("\nAngsuran anda masih kurang Rp.", sisa, "untuk 8 bulan")
                print("\n=== === === === ===")

            elif listMenu3 == "5":
                sisa = 8.333333 * 7

                print("\nAngsuran anda masih kurang Rp.", sisa, "untuk 7 bulan")
                print("\n=== === === === ===")

            elif listMenu3 == "6":
                sisa = 8.333333 * 6

                print("\nAngsuran anda masih kurang Rp.", sisa, "untuk 6 bulan")
                print("\n=== === === === ===")

            elif listMenu3 == "7":
                sisa = 8.333333 * 5

                print("\nAngsuran anda masih kurang Rp.", sisa, "untuk 5 bulan")
                print("\n=== === === === ===")

            elif listMenu3 == "8":
                sisa = 8.333333 * 4

                print("\nAngsuran anda masih kurang Rp.", sisa, "untuk 4 bulan")
                print("\n=== === === === ===")

            elif listMenu3 == "9":
                sisa = 8.333333 * 3

                print("\nAngsuran anda masih kurang Rp.", sisa, "untuk 3 bulan")
                print("\n=== === === === ===")

            elif listMenu3 == "10":
                sisa = 8.333333 * 2

                print("\nAngsuran anda masih kurang Rp.", sisa, "untuk 2 bulan")
                print("\n=== === === === ===")

            elif listMenu3 == "11":
                sisa = 8.333333 * 1

                print("\nAngsuran anda masih kurang Rp.", sisa, "untuk 1 bulan")
                print("\n=== === === === ===")

            else:
                print("\nMaaf input anda Salah, Terima kasih ... byJulhan")
                print("--- --- --- --- ---")

        else:
            print("\nTerima kasih ... byJulhan")
            print("--- --- --- --- ---")
            break

    elif listMenu == "3":
        print("Menu -> Menghitung BMI berat badan")

        berat = float(input("\nMasukan Berat badan (Kg) : "))
        tinggi = float(input("Masukan Tinggi badan (M) : "))

        def jul_BMI(berat, tinggi):

            BMI = berat / (tinggi * tinggi)
            print("\nNilai BMI anda:", BMI)

            if BMI > 22.9:
                return "Berat badan Lebih"
            elif BMI < 18.5:
                return "Berat badan Kurang"
            else:
                return "Berat badan Normal"

        hasil_BMI = jul_BMI(berat, tinggi)
        print("Status BMI anda saat ini :", hasil_BMI)

        print("=== === === === ===")

    else:
        print("\nTerima kasih ... byJulhan")
        print("--- --- --- --- ---")
        break
