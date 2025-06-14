n = int(input())
s = set(map(int, input().split()))
numCommand = int(input())

for i in range(numCommand):
    command = input().split()
    commandText = command[0]
    if commandText == "pop":
        s.pop()
    if commandText == "remove":
        s.remove(int(command[1]))
    if commandText == "discard":
        s.discard(int(command[1]))
print(sum(s))
