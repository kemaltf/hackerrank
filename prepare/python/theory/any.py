s = "qA2"

# Fungsi any() adalah fungsi bawaan Python yang menerima sebuah iterable (seperti list, tuple, atau generator) dan mengembalikan:

# - True jika setidaknya satu elemen dalam iterable bernilai True
# - False jika semua elemen dalam iterable bernilai False atau iterable kosong

# Fungsi any() memeriksa apakah setidaknya satu nilai True dalam hasil generator
print(any(c  for char in s))

# Generator Expression di Python
# char.isalpha() for char in s di Python disebut Generator Expression (ekspresi generator). 
# (ekspresi for item in iterable [if kondisi])
print(any(char.isalpha() for char in s))
print(any(char.isdigit() for char in s))
print(any(char.islower() for char in s))
print(any(char.isupper() for char in s))
