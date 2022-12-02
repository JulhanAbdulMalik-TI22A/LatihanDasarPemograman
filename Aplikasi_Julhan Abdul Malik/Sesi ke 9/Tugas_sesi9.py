print("------------------------------------------------------",
      "\n----------- Latihan 9 - Julhan Abdul Malik -----------",
      "\n------------------------------------------------------")

print("\n=================================================",
      "\n============ Program Array Sederhana ============",
      "\n=================================================")

print("\n========================================")

print("Menu Produk yang ada di Toko")
produk = ['Sabun', 'Sampo', 'Kopi']
for index, p in enumerate(produk):
    print(index+1, p)

while (True):
    print("\nMenu Fungsi")
    print('1. Menambahkan Produk menggunakan Append'
          '\n2. Menambahkan Produk menggunakan Insert'
          '\n3. Menghapus Produk menggunakan Remove'
          '\n4. Menghapus Produk menggunakan Pop'
          '\n5. Quit')

    print(" \n----------------------------------------")

    listMenu = input("Masukan Pilihan : ")

    if listMenu == "1":
        print("Menu -> Menambahkan Produk menggunakan Append")
        produk.append(input('\nMasukan nama Produk: '))

        print('\nMenu sudah di Update = ')
        for index, p in enumerate(produk):
            print(index+1, p)

        print("\n=== === === === ===")

    elif listMenu == "2":
        print("Menu -> Menambahkan Produk menggunakan Insert")
        produk.insert(int(input('\nMau memasukan ke Nomor berapa: ')) - 1,
                      input('Masukan nama Produk: '))
        print('\nMenu sudah di Update = ')

        for index, p in enumerate(produk):
            print(index+1, p)

        print("\n=== === === === ===")

    elif listMenu == "3":
        print("Menu -> Menghapus Produk menggunakan Remove")
        produk.remove(input('\nMasukan nama Produk: '))

        print('\nMenu sudah di Update = ')
        for index, p in enumerate(produk):
            print(index+1, p)

        print("\n=== === === === ===")

    elif listMenu == "4":
        print("Menu -> Menghapus Produk menggunakan Pop")
        produk.pop(int(input('\nMasukan nomor Produk: ')) - 1)

        print('\nMenu sudah di Update = ')
        for index, p in enumerate(produk):
            print(index+1, p)

        print("\n=== === === === ===")

    else:
        print("\nTerima kasih ... byJulhan")
        print("--- --- --- --- ---")
        break
