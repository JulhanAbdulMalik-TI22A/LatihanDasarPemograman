# Deskriptif
# membuat Variabel nama barang
# membuat Variabel harga barang
# membuat Variabel persen barang
# input nama barang
# input harga Barangbarang
# menghitung harga barang
# harga barang * barang / 100
# print harga barang beserta nama barang

print("------------------------------------------------------")
print("----------- Latihan 4 - Julhan Abdul Malik -----------")
print("------------------------------------------------------")

while (True):
    print("-----------------------------------------")

    nama_barang = input("\nMasukan nama barang Pertama : ")
    harga_barang1 = int(input("Masukan harga barang : "))

    nama_barang = input("\nMasukan nama barang Kedua: ")
    harga_barang2 = int(input("Masukan harga barang : "))

    nama_barang = input("\nMasukan nama barang Kedua: ")
    harga_barang3 = int(input("Masukan harga barang : "))

    persen = 10

    total = harga_barang1 + harga_barang2 + harga_barang3

    hargapersen = int(total * persen / 100)

    print("\n========================================")
    print("========== S T R U K   B E L I =========")
    print("========================================")
    print("\nHarga persentase : ", hargapersen)
    print("Total Harga Barang :", total + hargapersen)
    print("\n--------------------------------------")

    apakahLanjut = input("Apakah ingin membeli barang lain? Y or N : ")
    if (apakahLanjut != 'y'):
        break
