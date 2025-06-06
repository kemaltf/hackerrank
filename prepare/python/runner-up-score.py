if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arrList = list(arr)
    
    unique = [] 
    # Exclude the duplicate
    for i in arrList:
        if i not in unique:
            unique.append(i)


    sort = []
    for i in range(len(unique)):
        for j in range(0,len(unique)-i-1):
            if unique[j] > unique[j + 1]:
                unique[j], unique[j + 1] = unique[j + 1], unique[j]
                
            
    print(unique[len(unique)-2])


# CARA CEPAT
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    
    unique = list(set(arr))        # Hilangin duplikat
    unique.sort()                  # Urutkan
    print(unique[-2])              # Ambil runner-up
