from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D
import numpy

fig = pyplot.figure()

ax = Axes3D(fig)

X = numpy.arange(-2,2,0.01)
Y = numpy.arange(-2,2,0.01)
X,Y = numpy.meshgrid(X,Y)

Z = abs(X)*numpy.e**(-X**2-(4*Y/3)**2)
ax.plot_surface(X,Y,Z,rstride=1,cstride=1,cmap='rainbow')

pyplot.show()
