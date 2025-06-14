# Enter your code here. Read input from STDIN. Print output to STDOUT

studentEngNum = int(input())
studentEngSet = set(map(int, input().split()))
studentFrNum = int(input())
studentFrSet = set(map(int, input().split()))


print(
    len(studentEngSet | studentFrSet)
)  # Menampilkan jumlah total siswa yang mengambil bahasa Inggris ATAU Prancis (union)
print(
    len(studentEngSet ^ studentFrSet)
)  # Menampilkan jumlah siswa yang mengambil bahasa Inggris ATAU Prancis tapi tidak keduanya (symmetric difference)
print(
    len(studentEngSet - studentFrSet)
)  # Menampilkan jumlah siswa yang hanya mengambil bahasa Inggris saja (difference)
print(
    len(studentEngSet & studentFrSet)
)  # Menampilkan jumlah siswa yang mengambil kedua bahasa Inggris DAN Prancis (intersection)
