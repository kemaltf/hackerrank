# Buat dictionary dari input
students = {'Alice': 85.5, 'Bob': 85.5, 'Fufufafa': 78.5,'Charlie': 78.5, 'David': 85.5}

print("Original:", students)
# sorted() mengurutkan tuple berdasarkan elemen pertama (key/nama) secara default:

# Step 1: Ambil items
print(students.items)
items_list = list(students.items())
print("Step 1:", items_list)
# [('Alice', 85.5), ('Bob', 85.5), ('Charlie', 78.5), ('David', 85.5)]

# Step 2: Terapkan lambda ke setiap item
sorting_keys = []
for item in items_list:
    x = item  # ('Alice', 85.5)
    key = (x[1], x[0])  # (85.5, 'Alice')
    sorting_keys.append((key, item)) # [(key, item), (key, item), ...]
    # print(f"Item: {item} → Key: {key}")

# Step 3: Sort berdasarkan key
print("sorting_keys",sorting_keys)


# Lambda di Python
# fungsi = lambda parameter: hasil
# Contoh sederhana
# tambah = lambda a, b: a + b
# kuadrat = lambda x: x * x
sorting_keys.sort(key=lambda pair: pair[0])
# Tambahkan setelah baris 29
for pair in sorting_keys:
    print(f"pair: {pair}, pair[0]: {pair[0]}")
print("\nSetelah sorting:")
print("sorting_keys",sorting_keys)
print(sorting_keys[1])

# for key, item in sorting_keys:
#     print(f"Key: {key} → Item: {item}")

# # Step 4: Ambil item yang sudah terurut
# sorted_items = [item for key, item in sorting_keys]
# result = dict(sorted_items)
# print("\nHasil akhir:", result)