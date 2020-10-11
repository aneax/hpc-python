import numpy as np

num = [1,2.0,3,4.0]
print(repr(num))
nump = np.array(num)
print(repr(nump))

arr = np.arange(-2.0,2.0,0.2)
print(arr)

rsv = np.linspace(0.5,1.5,11)
print(rsv)

ran = "RandomStringCheck"
ranarr = np.array(ran, dtype='c')
print(ranarr)