import numpy as np

xy = np.loadtxt('xy-coordinates.dat')

print(xy)

xy[:,1] += 2.5

args = {
  'header': 'XY coordinates',
  'fmt': '%7.3f',
  'delimiter': ','
}
xy = np.savetxt('modified-coordinates.txt', xy, **args)

yz = np.loadtxt('modified-coordinates.txt', skiprows=0, dtype=float, delimiter=',')

print(yz)