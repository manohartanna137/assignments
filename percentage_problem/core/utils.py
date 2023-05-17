def percentage_calculation(student_mark,name):
    n = len(student_mark[name])
    sum_=0
    for i in range(n):
        sum_=sum_+student_mark[name][i]
    avg = sum_/n
    return avg





