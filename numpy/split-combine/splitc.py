import numpy as np

arr8 = np.random.randint(10,size=(8,8))

a = np.split(arr8,2)
print(a)

b = np.concatenate((a[0],a[1]))
print(b)

c = np.split(b,2, axis=1)
print(c)

d = np.concatenate((c[0],c[1]),axis=1)
print(d)

assert((b==d).all())
