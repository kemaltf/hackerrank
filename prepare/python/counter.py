from collections import Counter

# the number of shoes
x = int(input())

# the number of shoe size
y = list(map(int, input().split()))
yCount = Counter(y) # pair size and stock

# the number of customer
n = int(input())

totalReveneu = 0
for i in range(n):
    size, price = Counter(list(map(int, input().split())))
    
    if yCount[size] > 0:
        yCount[size] -= 1
        totalReveneu += price
        
print(totalReveneu)
    
