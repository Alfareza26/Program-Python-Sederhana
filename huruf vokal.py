kalimat = input("Masukkan sebuah kalimat: ")
vokal = "aeiouAEIOU"
jumlah = 0
for char in kalimat:
    if char in vokal:
        jumlah += 1
print(f"Jumlah huruf vokal: {jumlah}")