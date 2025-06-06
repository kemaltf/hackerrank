if __name__ == '__main__':
    n = int(input()) # NUMBER STUDENT
    student_marks = {} # name + mark object
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
       
    query_name = input()
    
    x = 0
    for i in student_marks[query_name]:
        x = x + i
        
    average = x / len(student_marks[query_name])    
    print("%.2f" % average)
