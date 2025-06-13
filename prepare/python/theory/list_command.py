N = 12

array = []
for _ in range(N):
    command = input().split()
    print(command)

    command_type = command[0]
    if(command_type == "print"):
        print(array)

    if(command_type == "insert"):
        array.insert(int(command[1]),int(command[2]))

    if(command_type == "remove"):
        # remove will remove the first VALUE not index
        array.remove(int(command[1]))

    if(command_type == "append"):
        array.append(int(command[1]))

    if(command_type == "sort"):
        array.sort()
    
    if(command_type == "pop"):
        array.pop()

    if(command_type == "reverse"):
        array.reverse()
    
    