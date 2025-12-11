def deret_fibonacci():
    """Menampilkan deret Fibonacci sebanyak n angka."""
    print("\n--- Program Deret Fibonacci ---")
    try:
        n = int(input("Masukkan jumlah angka dalam deret Fibonacci: "))
        if n <= 0:
            print("Jumlah angka harus lebih dari 0.")
            return
        
        a, b = 0, 1
        print("Deret Fibonacci:")
        for i in range(n):
            print(a, end=" ")
            a, b = b, a + b
        print()
    except ValueError:
        print("Input tidak valid. Harap masukkan angka bulat.")

def cek_ganjil_genap():
    """Memeriksa apakah sebuah bilangan ganjil atau genap."""
    print("\n--- Program Cek Bilangan Ganjil/Genap ---")
    try:
        angka = int(input("Masukkan sebuah bilangan untuk diperiksa: "))
        if angka % 2 == 0:
            print(f"Hasil: {angka} adalah bilangan GENAP.")
        else:
            print(f"Hasil: {angka} adalah bilangan GANJIL.")
    except ValueError:
        print("Input tidak valid. Harap masukkan angka.")

def cek_bilangan_prima():
    """Menentukan apakah sebuah bilangan adalah bilangan prima."""
    print("\n--- Program Cek Bilangan Prima ---")
    try:
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
    except ValueError:
        print("Input tidak valid. Harap masukkan angka.")

def hitung_vokal():
    """Menghitung jumlah huruf vokal dalam sebuah kalimat."""
    print("\n--- Program Hitung Huruf Vokal ---")
    kalimat = input("Masukkan sebuah kalimat: ")
    vokal = "aeiouAEIOU"
    jumlah = 0
    for char in kalimat:
        if char in vokal:
            jumlah += 1
    print(f"Jumlah huruf vokal dalam kalimat tersebut adalah: {jumlah}")

def hitung_pangkat_manual():
    """Menghitung hasil pangkat dari sebuah bilangan secara manual."""
    print("\n--- Program Hitung Pangkat Manual ---")
    try:
        base = int(input("Masukkan basis (angka): "))
        exponent = int(input("Masukkan eksponen (pangkat): "))
        
        if exponent < 0:
            print("Program ini hanya mendukung pangkat non-negatif.")
            return

        hasil = 1
        i = 0
        while i < exponent:
            hasil *= base
            i += 1
        print(f"Hasil: {base} pangkat {exponent} adalah {hasil}")
    except ValueError:
        print("Input tidak valid. Harap masukkan angka.")

def main():
    """Fungsi utama yang menampilkan menu dan menjalankan program."""
    while True:
        print("\n" + "="*35)
        print("     PROGRAM PYTHON SEDERHANA")
        print("="*35)
        print("1. Fibonacci")
        print("2. Bilangan Ganjil/Genap")
        print("3. Bilangan Prima")
        print("4. Hitung Huruf Vokal")
        print("5. Hitung Pangkat Manual")
        print("6. Keluar")
        print("="*35)

        pilihan = input("Masukkan pilihan (1-6): ")

        if pilihan == '1':
            deret_fibonacci()
        elif pilihan == '2':
            cek_ganjil_genap()
        elif pilihan == '3':
            cek_bilangan_prima()
        elif pilihan == '4':
            hitung_vokal()
        elif pilihan == '5':
            hitung_pangkat_manual()
        elif pilihan == '6':
            print("\nTerima kasih telah menggunakan program ini. Sampai jumpa!")
            break 
        else:
            print("\nPilihan tidak valid. Silakan masukkan angka antara 1 hingga 6.")
                
        input("\nTekan Enter untuk kembali ke menu utama...")

if __name__ == "__main__":
    main()