from turtle import width


alphabet = "abcdefghijklmnopqrstuvwxyz"
# print(alphabet[1:3])

# size 3
# 1: c [2:3]
# 2: cb [1:3]
# 3: cba [0:3]
# 4: cb [1:3]
# 5: c [2:3]


def print_rangoli(size):
    for i in range(size, 0, -1):
        pattern1 = alphabet[i - 1 : size][::-1]
        pattern2 = alphabet[i:size]
        finalPattern = "-".join("".join([pattern1, pattern2]))
        widthAlphabet = (size * 2) - 1
        widthAllChars = widthAlphabet + (widthAlphabet - 1)
        print(finalPattern.center(widthAllChars, "-"))

    for i in range(1, size, 1):
        pattern1 = alphabet[i:size][::-1]
        pattern2 = alphabet[i + 1 : size]
        finalPattern = "-".join("".join([pattern1, pattern2]))
        widthAlphabet = (size * 2) - 1
        widthAllChars = widthAlphabet + (widthAlphabet - 1)
        print(finalPattern.center(widthAllChars, "-"))


if __name__ == "__main__":
    n = int(input())
    print_rangoli(n)
