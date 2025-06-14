# Enter your code here. Read input from STDIN. Print output to STDOUT

from typing import Counter


sizeEachGroup = int(input())
roomNumber = list(map(int, input().split()))

frekuensi = Counter(roomNumber)
# Output dari Counter adalah sebuah objek subclass dari dictionary ( dict ) yang menyimpan elemen sebagai kunci dan frekuensi kemunculannya sebagai nilai.
print(frekuensi)
print(frekuensi.most_common())
print(frekuensi.items())
for room, count in frekuensi.items():
    if count == 1:
        print(room)
        break
