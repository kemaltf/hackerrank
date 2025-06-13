# string = "Www.HackerRank.com"
# print(string[1])

# array = []
# for i in string:
#     print (i.swapcase())
#     array.append(i.swapcase())

# print(''.join(array))

string = "Www.HackerRank.com"
swapped_string = string.swapcase()
print(swapped_string)  # Output: wWW.hACKERrANK.COM

string = "Www.HackerRank.com"

# Mengambil karakter dari index 0 sampai terakhir
print(string[0:])  # Output: Www.HackerRank.com
# atau cukup dengan
print(string[:])   # Output: Www.HackerRank.com

# Mengambil karakter dari index 1 sampai 3 (karakter di index 3 tidak termasuk)
print(string[1:3])  # Output: ww

# Mengambil 5 karakter pertama
print(string[:5])  # Output: Www.H

# Mengambil 5 karakter terakhir
print(string[-5:])  # Output: k.com

# Mengambil karakter dari index 4 sampai index 10
print(string[4:10])  # Output: Hacker