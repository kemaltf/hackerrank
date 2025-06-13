# Data untuk diproses
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Dengan list comprehension
list_result = sum([x * x for x in data if x % 2 == 0])

# Dengan generator expression (lebih efisien)
gen_result = sum(x * x for x in data if x % 2 == 0)  # Perhatikan tidak perlu tanda kurung tambahan

print(f"Hasil list comprehension: {list_result}")
print(f"Hasil generator expression: {gen_result}")