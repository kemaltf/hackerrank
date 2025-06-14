# STDIN       Function
# -----       --------
# 4           set a size M = 4
# 2 4 5 9     a = {2, 4, 5, 9}
# 4           set b size N = 4
# 2 4 11 12   b = {2, 4, 11, 12}


# m = int(input())
a = {8, -10}

# n = int(input())
b = {5, 6, 7}

difference_sm = a ^ b
print(difference_sm)
for i in sorted(difference_sm):
    print(i)
