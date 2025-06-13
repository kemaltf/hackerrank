# Menggunakan sorted() pada list
angka = [3, 1, 4, 1, 5, 9]
angka_terurut = sorted(angka)
print(angka)         # Output: [3, 1, 4, 1, 5, 9] (tidak berubah)
print(angka_terurut) # Output: [1, 1, 3, 4, 5, 9] (list baru)

# Menggunakan sorted() pada tuple
tuple_angka = (3, 1, 4, 1, 5, 9)
tuple_terurut = sorted(tuple_angka)
print(tuple_angka)    # Output: (3, 1, 4, 1, 5, 9) (tidak berubah)
print(tuple_terurut)  # Output: [1, 1, 3, 4, 5, 9] (list baru)

# Menggunakan sorted() pada set
set_angka = {3, 1, 4, 5, 9}
set_terurut = sorted(set_angka)
print(set_angka)     # Output: {1, 3, 4, 5, 9} (tidak berubah, tapi set tidak berurutan)
print(set_terurut)   # Output: [1, 3, 4, 5, 9] (list baru)