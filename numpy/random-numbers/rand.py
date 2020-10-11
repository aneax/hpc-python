import numpy as np
import matplotlib.pyplot as plt

a = np.random.rand(1000)
m = np.mean(a)
st = np.std(m)

plt.hist(a)
plt.show()

k = np.random.beta(0.8,1.5, size=(100))
plt.hist(k)
plt.show()