import numpy as np

n = 10000
a = 0
b = np.pi/2

dx = (b-a)/n

x = np.arange(a, b, dx)
x_b = (x[1:] +x[:-1])*0.5

sum = np.sum(np.sin(x_b)*dx)

diff = (1-sum)
print(sum)
print(diff)
