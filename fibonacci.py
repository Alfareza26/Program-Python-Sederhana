n = int(input("Masukkan jumlah angka dalam deret Fibonacci: "))
a, b = 0, 1
print("Deret Fibonacci:")
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b