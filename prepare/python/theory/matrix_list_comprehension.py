# Cara baru dengan list comprehension
matrix = [[0 for j in range(2)] for i in range(2)]
#         j = 0, kemudian j = 1
#         │ │      │          │   │ │
#         │ │      │          │   │ └── range untuk baris (0, 1)
#         │ │      │          │   └────── variabel baris (i)
#         │ │      │          └────────── kurung siku untuk setiap baris
#         │ │      └───────────────────── range untuk kolom (0, 1)
#         │ └──────────────────────────── variabel kolom (j)
#         └─────────────────────────────── nilai yang dimasukkan (0)

# [baris , kolom]
# Iterasi 1: i = 0 (baris pertama)
# Jalankan: [0 for j in range(2)]
# j = 0 → masukkan 0
# j = 1 → masukkan 0
# Hasil: [0, 0]

# Iterasi 2: i = 1 (baris kedua)
# Jalankan: [0 for j in range(2)]
# j = 0 → masukkan 0
# j = 1 → masukkan 0
# Hasil: [0, 0]

# Hasil akhir: [[0, 0], [0, 0]]
print(matrix)
# Output: [[0, 0], [0, 0]]

# Matrix dengan nilai genap/ganjil
matrix = [['genap' if (i+j) % 2 == 0 else 'ganjil' for j in range(3)] for i in range(3)]\
#             ↑           ↑                ↑
#             │           │                └── nilai jika kondisi FALSE
#             │           └─────────────────── kondisi yang dicek
#             └─────────────────────────────── nilai jika kondisi TRUE
print(matrix)
# Output: [['genap', 'ganjil', 'genap'], ['ganjil', 'genap', 'ganjil'], ['genap', 'ganjil', 'genap']]

# Matrix dengan filter nilai
matrix = [[i*j if i*j > 2 else 0 for j in range(1, 4)] for i in range(1, 4)]
print(matrix)
# Output: [[0, 0, 3], [0, 4, 6], [3, 6, 9]]

# n = 2
# batas koordinatnya
# [1,1,2]
# [i,j,k]
# Semua kemungkinan kombinasi:
# i: 0 atau 1
# j: 0 atau 1
# k: 0, 1, atau 2

i = 0
j = 0
k = 0
x = 1
y = 1
z = 2
n = 2

# Untuk setiap pilihan i:
#   Untuk setiap pilihan j:
#     Untuk setiap pilihan k:
#       Buat kombinasi [i,j,k]

matrix = []
for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            if i+j+k<=n:
                baris= [i,j,k]
                matrix.append(baris)

print(matrix)

matrix = []
# Conditional expression : nilai_jika_true if kondisi else nilai_jika_false
# Filter condition : for ... if kondisi
matrix = [[i,j,k]  for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k<=n]


# - [0,0,0] → 0+0+0 = 0 ≤ 2 ✅ MASUK
# - [0,0,1] → 0+0+1 = 1 ≤ 2 ✅ MASUK
# - [0,1,0] → 0+1+0 = 1 ≤ 2 ✅ MASUK

# - [0,1,1] → 0+1+1 = 2 ≤ 2 ✅ MASUK ❌ (seharusnya tidak)
# - [1,0,0] → 1+0+0 = 1 ≤ 2 ✅ MASUK
# - [1,0,1] → 1+0+1 = 2 ≤ 2 ✅ MASUK ❌ (seharusnya tidak)
# - [1,1,0] → 1+1+0 = 2 ≤ 2 ✅ MASUK ❌ (seharusnya tidak)
# - [1,1,1] → 1+1+1 = 3 ≤ 2 ❌ TIDAK MASUK ❌ (seharusnya masuk)

# ### Dengan i+j+k != 2 (yang benar):
# - [0,0,0] → 0+0+0 = 0 ≠ 2 ✅ MASUK
# - [0,0,1] → 0+0+1 = 1 ≠ 2 ✅ MASUK
# - [0,1,0] → 0+1+0 = 1 ≠ 2 ✅ MASUK

# - [0,1,1] → 0+1+1 = 2 ≠ 2 ❌ TIDAK MASUK ✅
# - [1,0,0] → 1+0+0 = 1 ≠ 2 ✅ MASUK
# - [1,0,1] → 1+0+1 = 2 ≠ 2 ❌ TIDAK MASUK ✅
# - [1,1,0] → 1+1+0 = 2 ≠ 2 ❌ TIDAK MASUK ✅
# - [1,1,1] → 1+1+1 = 3 ≠ 2 ✅ MASUK