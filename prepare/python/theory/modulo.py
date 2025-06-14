# Contoh penggunaan operator modulo (%) di Python

# 1. Dasar-dasar modulo
print("=== Dasar Modulo ===")
print("10 % 3 =", 10 % 3)  # Output: 1 (sisa pembagian 10 dibagi 3)
print("10 % 2 =", 10 % 2)  # Output: 0 (tidak ada sisa, berarti habis dibagi)
print("10 % 5 =", 10 % 5)  # Output: 0 (tidak ada sisa)
print("7 % 3 =", 7 % 3)  # Output: 1 (sisa pembagian 7 dibagi 3)

# 2. Mengecek bilangan genap/ganjil
print("\n=== Cek Bilangan Genap/Ganjil ===")
angka = 10
if angka % 2 == 0:
    print(f"{angka} adalah bilangan genap")
else:
    print(f"{angka} adalah bilangan ganjil")

# 3. Mengecek apakah suatu bilangan habis dibagi bilangan lain
print("\n=== Cek Habis Dibagi ===")
a = 15
b = 5
if a % b == 0:
    print(f"{a} habis dibagi {b}")
else:
    print(f"{a} tidak habis dibagi {b}, sisa {a % b}")

# 4. Aplikasi modulo dalam looping (untuk membuat pola berulang)
print("\n=== Aplikasi Modulo dalam Looping ===")
for i in range(1, 11):
    if i % 3 == 0:
        print(f"{i} adalah kelipatan 3")
    else:
        print(f"{i} bukan kelipatan 3, sisa {i % 3}")

# 5. Modulo dengan angka negatif
print("\n=== Modulo dengan Angka Negatif ===")
print(
    "-10 % 3 =", -10 % 3
)  # Output: 2 (di Python, hasil modulo selalu mengikuti tanda divisor)
print("10 % -3 =", 10 % -3)  # Output: -2

# 6. Aplikasi praktis: Pembagian waktu
print("\n=== Aplikasi Praktis: Konversi Detik ===")
total_detik = 3665

jam = total_detik // 3600
sisa_detik = total_detik % 3600
menit = sisa_detik // 60
detik = sisa_detik % 60

print(f"{total_detik} detik = {jam} jam, {menit} menit, {detik} detik")
