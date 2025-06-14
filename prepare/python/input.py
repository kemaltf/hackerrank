x, k = map(int, input().split())

# Membaca formula sebagai string dari input berikutnya
formula = input().replace("x", str(x))  # Mengganti semua 'x' dengan nilai x

# Mengevaluasi formula
count = eval(formula)
print(count)
print(count == k)
