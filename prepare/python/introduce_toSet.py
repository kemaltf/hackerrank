def average(array):
    heightSet = set(array)
    heightLen = len(heightSet)
    heightSum = sum(heightSet)
    return heightSum / heightLen
    # your code goes here


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
