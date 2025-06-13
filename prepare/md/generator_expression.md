# Perbandingan Detail: Generator Expression vs List Comprehension

Generator Expression adalah fitur Python yang memungkinkan pembuatan generator secara ringkas tanpa perlu mendefinisikan fungsi generator lengkap dengan `def` dan `yield`. Ini diperkenalkan di Python 2.4.

Berikut adalah penjelasan lebih detail tentang perbedaan antara generator expression dan list comprehension beserta contoh-contoh yang bisa langsung Anda salin.

1. Sintaks dan Struktur

## List Comprehension

```python
[ekspresi for item in iterable if kondisi]
```

### List Comprehension

- Mengevaluasi seluruh ekspresi sekaligus
- Membuat dan menyimpan seluruh list di memori
- Akses elemen bisa dilakukan berulang kali
- Cocok untuk data kecil hingga menengah

## Generator Expression

```python
(ekspresi for item in iterable if kondisi)
```

### Generator Expression

- Menggunakan "lazy evaluation" (evaluasi saat diperlukan)
- Hanya menghasilkan satu nilai pada satu waktu saat diminta
- Tidak menyimpan seluruh hasil di memori
- Hanya bisa diiterasi sekali
- Cocok untuk data besar atau stream data
  Perbedaan utama terlihat pada penggunaan tanda kurung: [] untuk list comprehension dan () untuk generator expression.

### Contoh 1: Dasar

```python
# Data awal
data = range(1, 1000000)  # Rentang angka besar

# List comprehension - menyimpan semua nilai di memori
list_result = [x * x for x in data]  # Langsung membuat list dengan 1 juta item

# Generator expression - menghasilkan nilai saat diperlukan
gen_result = (x * x for x in data)  # Hanya membuat generator object, belum menghitung nilai

# Menggunakan list comprehension
print(list_result[0])  # Akses langsung elemen pertama
print(list_result[-1])  # Akses langsung elemen terakhir

# Menggunakan generator expression
first = next(gen_result)  # Menghasilkan nilai pertama
print(first)

# Untuk mendapatkan nilai terakhir, harus mengiterasi seluruh generator
# (yang akan menghabiskan generator)
for val in gen_result:
    last_val = val
print(last_val)  # Nilai terakhir

# Mencoba mengakses generator lagi setelah diiterasi
print(list(gen_result))  # Akan menghasilkan list kosong karena generator sudah habis
```

```python
# Data untuk diproses
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Dengan list comprehension
list_result = sum([x * x for x in data if x % 2 == 0])

# Dengan generator expression (lebih efisien)
gen_result = sum(x * x for x in data if x % 2 == 0)  # Perhatikan tidak perlu tanda kurung tambahan

print(f"Hasil list comprehension: {list_result}")
print(f"Hasil generator expression: {gen_result}")
```
