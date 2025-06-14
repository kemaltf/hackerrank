# Enter your code here. Read input from STDIN. Print output to STDOUT
numA = int(input())
setA = set(map(int, input().split()))
numCmd = int(input())

for i in range(numCmd):
    command = input().split()
    operation = command[0]  # Nama operasi (intersection_update, update, dll)
    setB = set(map(int, input().split()))
    
    # Menjalankan operasi set yang sesuai
    if operation == "intersection_update":
        setA.intersection_update(setB)
    elif operation == "update":
        setA.update(setB)
    elif operation == "symmetric_difference_update":
        setA.symmetric_difference_update(setB)
    elif operation == "difference_update":
        setA.difference_update(setB)

# Mencetak jumlah elemen dalam set setelah semua operasi
print(sum(setA))
