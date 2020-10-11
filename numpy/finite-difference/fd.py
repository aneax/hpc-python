import numpy as np

dx = 0.1
f = lambda x: np.sin(x) 
x = np.arange(0, np.pi/2, 0.1)

## ~4.5 microseconds
dfe = (f(x+dx) - f(x-dx))/(2*dx)
print(dfe[1:-1])

## ~1.8 microseconds + 0.65 microseconds
df_1 = np.sin(x)
df = (df_1[2:] - df_1[:-2])/(2*dx)
print(df)

## ~0.8 microseconds
y = np.cos(x[1:-1])
print(y)

print(np.sum((np.abs(df - y))**2))