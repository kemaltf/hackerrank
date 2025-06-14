# Contoh shorthand conditionals di Python


# 1. Ternary operator
def get_status(age):
    return "dewasa" if age >= 18 else "anak-anak"


print(get_status(20))  # Output: dewasa
print(get_status(15))  # Output: anak-anak


# 2. Return kondisi langsung
def is_even(num):
    return num % 2 == 0


print(is_even(4))  # Output: True
print(is_even(5))  # Output: False


# 3. Logical operators shorthand
def has_permission(user):
    # Tidak perlu menulis "== True"
    return user.is_admin


# 4. Pengecekan nilai dengan bool()
def is_valid(value):
    return bool(value)  # True jika value bukan 0, "", [], None, False


print(is_valid(0))  # Output: False
print(is_valid([1, 2]))  # Output: True


# 5. Shorthand dengan and/or
def get_username(user):
    # Jika user.name ada (tidak None dan tidak kosong), gunakan itu
    # Jika tidak, gunakan "Anonymous"
    return user.name or "Anonymous"


# 6. Shorthand untuk list comprehension dengan kondisi
numbers = [1, 2, 3, 4, 5]
even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers)  # Output: [2, 4]

# 7. Shorthand untuk dictionary comprehension dengan kondisi
squares = {x: x**2 for x in range(6) if x % 2 == 0}
print(squares)  # Output: {0: 0, 2: 4, 4: 16}
