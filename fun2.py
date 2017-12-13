from matplotlib import pyplot
import numpy
from mpl_toolkits.mplot3d import Axes3D

fig = pyplot.figure()

X = numpy.arange(0.01,4,0.01)
Y = 1.5*X*numpy.log(X)-1/36*numpy.e**(-(36*X-36/2.7183)**4)

pyplot.plot(Y,X)

pyplot.show()
