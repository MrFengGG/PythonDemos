import numpy
from matplotlib import pyplot

x = numpy.linspace(0,20,1000)
y = x**(1/2)

pyplot.plot(x,y)
pyplot.show()
