import numpy as np
import matplotlib.pyplot as plt

field = np.loadtxt('points_circle.dat')
plt.plot(field[:,0], field[:,1], 'ko')

field = np.array([2.1,1.1]) + field
plt.plot(field[:,0], field[:,1], 'ro')
plt.show()