# Membuat matrix 2x2 kosong
matrix = []

# Loop untuk baris
for i in range(2):
    baris = []  # Buat baris kosong
    # Loop untuk kolom
    for j in range(2):
        baris.append(0)  # Isi dengan 0
    matrix.append(baris)  # Tambahkan baris ke matrix

print(matrix)
# Output: [[0, 0], [0, 0]]

# Matrix 3x3 dengan angka berurutan
matrix = []
nilai = 1

for i in range(3):  # 3 baris
    baris = []
    for j in range(3):  # 3 kolom
        baris.append(nilai)
        nilai += 1  # Increment nilai
    matrix.append(baris)

print(matrix)
# Output: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]