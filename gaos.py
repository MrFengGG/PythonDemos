from matplotlib import pyplot
import pylab
import numpy
import math

def draw_gauss(start,end,step,theta,miu):
    x = numpy.linspace(start,end,1/step)
    A = 1/((2*math.pi)**1/2)*theta
    MI = -(x - miu)**2/2*theta**2
    y = A*math.e**MI
    pyplot.plot(x,y)

def draw_uniform(start,end,step):
    x = numpy.linspace(start,end,1/step)
    length = x.shape[-1]
    y = [1/(end-start) for i in range(length)]
    pyplot.plot(x,y)
    pyplot.plot([x[0],x[0]],[y[0],0])
    pyplot.plot([x[-1],x[-1]],[y[-1],0])
    
if __name__ == "__main__":
    pyplot.figure()
    draw_gauss(-10,10,0.001,1,0)
    draw_gauss(-10,10,0.001,2,0)
    draw_gauss(-10,10,0.001,3,0)
    draw_gauss(-10,10,0.001,4,0)
    pyplot.figure()
    draw_uniform(-10,10,0.001)
    pyplot.show()
