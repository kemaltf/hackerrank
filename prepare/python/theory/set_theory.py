buah_dict = {"apel": 5, "jeruk": 3, "pisang": 2}
print(
    f"Dictionary buah: {buah_dict}"
)  # Output: Dictionary buah: {'apel': 5, 'jeruk': 3, 'pisang': 2}

# Set Theory di Python

# 1. Membuat Set
print("=== Membuat Set ===")
# Set dengan kurung kurawal
buah = {"apel", "jeruk", "pisang", "apel"}  # Duplikat akan dihapus otomatis
print(f"Set buah: {buah}")

# Set kosong (harus menggunakan set(), karena {} adalah dictionary kosong)
set_kosong = set()
print(f"Set kosong: {set_kosong}")

# Membuat set dari list
angka_list = [1, 2, 3, 2, 1, 4, 5, 4]
angka_set = set(angka_list)
print(f"List: {angka_list}")
print(f"Set dari list: {angka_set}")  # Duplikat dihapus

# Membuat set dari string
karakter_set = set("mississippi")
print(f"Set dari string 'mississippi': {karakter_set}")  # Karakter unik saja

# 2. Operasi Dasar Set
print("\n=== Operasi Dasar Set ===")
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

# Menambah elemen
set_a.add(6)  # Menambah satu elemen
print(f"Set A setelah add(6): {set_a}")

set_a.update([7, 8, 9])  # Menambah beberapa elemen
print(f"Set A setelah update([7, 8, 9]): {set_a}")

# Menghapus elemen
set_a.remove(9)  # Menghapus elemen (error jika tidak ada)
print(f"Set A setelah remove(9): {set_a}")

set_a.discard(10)  # Menghapus elemen (tidak error jika tidak ada)
print(f"Set A setelah discard(10): {set_a}")

pop_item = set_a.pop()  # Menghapus dan mengembalikan elemen acak
print(f"Item yang di-pop: {pop_item}")
print(f"Set A setelah pop(): {set_a}")

set_a.clear()  # Menghapus semua elemen
print(f"Set A setelah clear(): {set_a}")

# 3. Operasi Matematika Set
print("\n=== Operasi Matematika Set ===")
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

# Union (Gabungan) - semua elemen dari kedua set
union_set = set_a.union(set_b)  # atau set_a | set_b
print(f"Union A ∪ B: {union_set}")

# Intersection (Irisan) - elemen yang ada di kedua set
intersection_set = set_a.intersection(set_b)  # atau set_a & set_b
print(f"Intersection A ∩ B: {intersection_set}")

# Difference (Selisih) - elemen di set_a tapi tidak di set_b
difference_set = set_a.difference(set_b)  # atau set_a - set_b
print(f"Difference A - B: {difference_set}")

# Symmetric Difference - elemen yang ada di salah satu set tapi tidak di keduanya
sym_diff_set = set_a.symmetric_difference(set_b)  # atau set_a ^ set_b
print(f"Symmetric Difference A △ B: {sym_diff_set}")

# 4. Subset, Superset, dan Disjoint
print("\n=== Subset, Superset, dan Disjoint ===")
set_c = {1, 2}
set_d = {1, 2, 3, 4, 5}
set_e = {6, 7, 8}

# Subset - semua elemen set_c ada di set_d
is_subset = set_c.issubset(set_d)  # atau set_c <= set_d
print(f"Apakah C subset dari D? {is_subset}")

# Superset - set_d memiliki semua elemen set_c
is_superset = set_d.issuperset(set_c)  # atau set_d >= set_c
print(f"Apakah D superset dari C? {is_superset}")

# Disjoint - tidak ada elemen yang sama
is_disjoint = set_c.isdisjoint(set_e)
print(f"Apakah C dan E disjoint? {is_disjoint}")

# 5. Frozen Set (Immutable Set)
print("\n=== Frozen Set ===")
regular_set = {1, 2, 3}
frozen = frozenset([1, 2, 3])

print(f"Regular set: {regular_set}")
print(f"Frozen set: {frozen}")

try:
    regular_set.add(4)  # Ini berhasil
    print(f"Regular set setelah add(4): {regular_set}")

    frozen.add(4)  # Ini akan error karena frozenset tidak bisa diubah
except AttributeError as e:
    print(f"Error: {e}")

# 6. Aplikasi Praktis Set
print("\n=== Aplikasi Praktis Set ===")

# Menghapus duplikat dari list
list_dengan_duplikat = [1, 2, 2, 3, 4, 4, 5]
list_tanpa_duplikat = list(set(list_dengan_duplikat))
print(f"List tanpa duplikat: {list_tanpa_duplikat}")

# Mencari elemen unik di dua list
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
elemen_unik = set(list1).symmetric_difference(set(list2))
print(f"Elemen unik di salah satu list: {elemen_unik}")

# Mencari elemen yang ada di semua list
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
list3 = [4, 5, 9, 10]
elemen_di_semua = set(list1).intersection(set(list2), set(list3))
print(f"Elemen yang ada di semua list: {elemen_di_semua}")

# Mengecek jika semua elemen list1 ada di list2
list1 = [1, 2]
list2 = [1, 2, 3, 4]
semua_ada = set(list1).issubset(set(list2))
print(f"Semua elemen list1 ada di list2? {semua_ada}")

# Membuat set angka
angka_set = {10, 20, 30, 40, 50}

# Menghitung jumlah elemen
jumlah_elemen = len(angka_set)
print(f"Set berisi {jumlah_elemen} angka")

# Menjumlahkan semua angka
total = sum(angka_set)
print(f"Total dari semua angka: {total}")

# Menghitung rata-rata
rata_rata = total / jumlah_elemen
print(f"Rata-rata: {rata_rata}")
