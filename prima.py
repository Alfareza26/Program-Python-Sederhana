angka = int(input("Masukkan sebuah angka: "))
if angka <= 1:
    print(f"{angka} bukan bilangan prima.")
else:
    is_prima = True
    for i in range(2, int(angka**0.5) + 1):
        if angka % i == 0:
            is_prima = False
            break
    if is_prima:
        print(f"{angka} adalah bilangan prima.")
    else:
        print(f"{angka} bukan bilangan prima.")