from collections import namedtuple

def calculate_average_mark(students_data):
    N = int(students_data[0])
    Students = namedtuple('students', students_data[1])
    total = 0

    for i in range(N):
        student = Students(*students_data[i+2].split())
        total += int(student.mark)

    average_mark = total / N
    return '{0:.2f}'.format(average_mark)
students_data = ['3','name mark','John 80','Emily 90','Michael 75']

