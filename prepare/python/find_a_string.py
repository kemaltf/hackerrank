def count_substring(string, sub_string):
    count = 0
    for i in range(len(string)):
        for j in range(len(string), i, -1):
            var = string[i:j]
            if(var == sub_string):
                count+=1
    return count

if __name__ == '__main__':
    string = "ABCDCDC"
    sub_string = "CDC"
    count = count_substring(string, sub_string)
    print(count)