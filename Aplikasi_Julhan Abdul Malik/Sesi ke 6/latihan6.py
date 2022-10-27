print("------------------------------------------------------")
print("----------- Latihan 6 - Julhan Abdul Malik -----------")
print("------------------------------------------------------")

print("\n======================================================")
print("=========== Program menentukan Grade Nilai ===========")
print("======================================================")

while (True):
    nama = input("\nMasukan nama Mahasiswa : ")
    nilai = input("Inputkan nilai akhir   : ")

    if (nilai.isnumeric() == True):
        nilai_int = int(nilai)
        if nilai_int >= 90:
            grade = "A"
            predikat = "Dengan Pujian"

        elif nilai_int >= 80:
            grade = "B"
            predikat = "Sangat Memuaskan"

        elif nilai_int >= 70:
            grade = "C"
            predikat = "Memuaskan"

        elif nilai_int >= 60:
            grade = "D"
            predikat = "Tidak Memuaskan"

        elif nilai_int >= 0:
            grade = "E"
            predikat = "Tidak Lulus"

        print("\n------------------------")
        print("Nama Mahasiswa : ", nama)
        print("Grade Anda     : ", grade)
        print("Predikat Anda  : ", predikat)

    else:
        print("\nMaaf input anda Salah")

    apakahLanjut = input("\nApakah menentukan Kembali? Y or N : ")
    if (apakahLanjut != 'y'):
        break

print("\n======================================================")
