import numpy as np

n_low= -100
n_high = 100
n = 2
A = np.random.randint(n_low, n_high, size=(n,n))
B = np.random.randint(n_low, n_high, size=(n,n))

Asym = (A + A.T)
C = A @ B
print(Asym)
print(C)
print(np.linalg.eigvals(C))