if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    matrix = []
    # Conditional expression : nilai_jika_true if kondisi else nilai_jika_false
    # Filter condition : for ... if kondisi

    # this is trick question, it is said that NOT EQUAL TO n, the arithmetic can be more or 
    # less, the important thing is that it is not the same. not less than N
    matrix = [[i,j,k]  for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k!=n]
    
    print(matrix)