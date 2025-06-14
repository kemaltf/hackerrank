buah = ["apel", "jeruk", "pisang"]
print(enumerate(buah))

# Tanpa enumerate
for i in range(len(buah)):
    print(i, buah[i])

# Dengan enumerate
for index, nilai in enumerate(buah):
    print(index, nilai)

# Output keduanya sama:
# 0 apel
# 1 jeruk
# 2 pisang
