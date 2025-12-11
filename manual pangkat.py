base = int(input("Masukkan basis (angka): "))
exponent = int(input("Masukkan eksponen (pangkat): "))
hasil = 1
i = 0
while i < exponent:
    hasil *= base
    i += 1
print(f"{base} pangkat {exponent} adalah {hasil}")