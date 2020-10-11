import numpy

def main():

    arr = numpy.arange(1000)
    dif = numpy.zeros(999, int)
    for i in range(1, len(arr)):
        dif[i-1] = arr[i] - arr[i-1]

def arr():
    arr = numpy.arange(1000)
    dif = arr[1:] - arr[:-1]    


a = numpy.array([[1,2,3],[4,5,6]])

print(a.shape)
print(a.reshape(3,2))

print(a.ravel())
print(a.flatten())
print(a.size)

a = numpy.array([[1, 2, 3], [4, 5, 6]])
b = numpy.array([[7, 8, 9], [10, 11, 12]])
c = numpy.concatenate((a, b))
print(c)

c = numpy.concatenate((a, b), axis=1)
print(c)

a = numpy.array([[1, 2, 3], [4, 5, 6]])
x = numpy.split(a, 2)
y = numpy.split(a, 3, axis=1)

print(x)
print(y)


a = numpy.arange(4*6).reshape(4,1,6)
b = numpy.arange(2*6).reshape(2,6)

print(a)
print("")
print(b)
c = a * b
print("")
print(c)