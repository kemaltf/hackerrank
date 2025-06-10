from collections import Counter

# myList = [1,1,2,3,4,5,3,2,3,4,2,1,2,3]
# print(Counter(myList))
# print(Counter(myList).items())
# print(Counter(myList).keys())
# print(Counter(myList).values())
# Output: Counter({2: 4, 3: 4, 1: 3, 4: 2, 5: 1})

from collections import Counter

# n = int(input())
# Contoh input: "2 3 4 5 6 8 7 6 5 18"
# Hasil: user_input = "2 3 4 5 6 8 7 6 5 18" (string)

# Hasil: user_input = ["2", "3", "4", "5", "6", "8", "7", "6", "5", "18"]
# (list berisi string)

user_input = map(int, input().split())
# Hasil: user_input = map object yang mengubah setiap string jadi integer
# Isinya seperti: 2, 3, 4, 5, 6, 8, 7, 6, 5, 18 (tapi masih map object) <map object at 0x0000024462B0C370>
print(user_input)

shoe_sizes = list(map(int, input().split()))
# Hasil: shoe_sizes = [2, 3, 4, 5, 6, 8, 7, 6, 5, 18]
# (list berisi integer)
shoe_sizes = list(map(int, input().split()))
print(shoe_sizes)
m = int(input())