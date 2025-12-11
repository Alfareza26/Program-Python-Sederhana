kondisi = True
while kondisi:
    try:
        input_pengguna = input("Masukkan bilangan untuk dicek: ")
        angka = int(input_pengguna)

        if angka % 2 == 0:
            print(f"{angka} adalah bilangan GENAP.")
        else:
            print(f"{angka} adalah bilangan GANJIL.")
        
        kondisi = False

    except ValueError:
        print("Not Found. Try Again")

print("\nCheck complete.")