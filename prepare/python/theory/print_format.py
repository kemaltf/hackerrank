# ===== FORMAT PRINT DI PYTHON =====

print("\n=== 1. Print Dasar ===")
# Print sederhana
print("Hello, World!")

# Print dengan multiple argumen (dipisahkan spasi secara default)
print("Nama:", "Budi", "Umur:", 25)

# Mengubah separator
print("Apel", "Jeruk", "Pisang", sep="-")

# Mengubah end character (default: \n)
print("Baris ini tidak diakhiri newline", end=" ")
print("sehingga teks ini muncul di baris yang sama")


print("\n=== 2. Format String dengan % (Cara Lama) ===")
# Format dengan %
nama = "Budi"
umur = 25
print("Nama: %s, Umur: %d" % (nama, umur))

# Format angka
pi = 3.14159
# - % adalah penanda awal format specifier
# - .2 menentukan presisi desimal (2 angka di belakang koma)
# - f menandakan bahwa nilai yang diformat adalah floating point (angka desimal)
print("Nilai Pi: %.2f" % pi)  # 2 desimal
print("Nilai Pi: %10.2f" % pi)  # Lebar 10, 2 desimal


print("\n=== 3. Format String dengan str.format() ===")
# Format dengan str.format()
print("Nama: {}, Umur: {}".format(nama, umur))

# Format dengan posisi indeks
print("Umur: {1}, Nama: {0}".format(nama, umur))

# Format dengan nama parameter
print("Halo, {nama}. Umur Anda {umur} tahun.".format(nama=nama, umur=umur))

# Format angka
print("Nilai Pi: {:.2f}".format(pi))  # 2 desimal
print("Nilai Pi: {:10.2f}".format(pi))  # Lebar 10, 2 desimal


print("\n=== 4. F-String (Python 3.6+) ===")
# Format dengan f-string (paling modern dan direkomendasikan)
print(f"Nama: {nama}, Umur: {umur}")

# Ekspresi dalam f-string
print(f"Tahun lahir: {2023 - umur}")

# Format angka dalam f-string
print(f"Nilai Pi: {pi:.2f}")  # 2 desimal
print(f"Nilai Pi: {pi:10.2f}")  # Lebar 10, 2 desimal

# Padding dan alignment
print(f"Kiri   : {nama:<10}")  # Left align, lebar 10
print(f"Tengah : {nama:^10}")  # Center align, lebar 10
print(f"Kanan  : {nama:>10}")  # Right align, lebar 10

# Format dengan ribuan separator
jumlah = 1000000
print(f"Jumlah: {jumlah:,}")  # Output: Jumlah: 1,000,000


print("\n=== 5. Format Khusus ===")
# Format bilangan biner, oktal, heksadesimal
angka = 42
print(f"Desimal: {angka}")
print(f"Biner  : {angka:b}")  # Output: 101010
print(f"Oktal  : {angka:o}")  # Output: 52
print(f"Heks   : {angka:x}")  # Output: 2a
print(f"Heks   : {angka:X}")  # Output: 2A (huruf besar)

# Format persen
persen = 0.75
print(f"Persentase: {persen:.1%}")  # Output: 75.0%


print("\n=== 6. Tabel dengan Format ===")
# Membuat tabel sederhana
print("| {:<10} | {:<8} | {:<5} |".format("Nama", "Jurusan", "Nilai"))
print("| {:<10} | {:<8} | {:<5} |".format("-" * 10, "-" * 8, "-" * 5))
print("| {:<10} | {:<8} | {:<5} |".format("Budi", "Teknik", 85))
print("| {:<10} | {:<8} | {:<5} |".format("Ani", "Ekonomi", 90))
print("| {:<10} | {:<8} | {:<5} |".format("Siti", "Hukum", 88))


print("\n=== 7. Debug dengan repr() ===")
# Menampilkan representasi string yang tepat (termasuk escape character)
teks = "Baris 1\nBaris 2\tTab"
print("Normal:", teks)
print("Repr  :", repr(teks))


print("\n=== 8. Print ke File ===")
# Menulis ke file (hanya contoh, tidak dijalankan)
print(
    """# Contoh menulis ke file
with open('output.txt', 'w') as f:
    print("Hello, File!", file=f)
    print(f"Nama: {nama}, Umur: {umur}", file=f)
"""
)


print("\n=== 9. Flush Output ===")
# Memaksa output segera ditampilkan (berguna untuk logging)
import time

print("Menghitung", end="", flush=True)
for i in range(3):
    time.sleep(0.5)  # Simulasi proses yang membutuhkan waktu
    print(".", end="", flush=True)
print(" Selesai!")
