import numpy
def lin_algebra(list1):
    arr = numpy.array(list1,dtype = float)
    a=round(numpy.linalg.det(arr),2)
    print(a)
    return a