import numpy
# f(x) = x^2 + random noise (between 0,1)
x = numpy.linspace(-4, 4, 7)
f = x**2 + numpy.random.random(x.shape)

p = numpy.polyfit(x, f, 2)

print(p)
# output: [ 0.96869003  -0.01157275  0.69352514]
#   f(x) =  p[0] * x^2 + p[1] * x  + p[2]