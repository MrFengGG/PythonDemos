import numpy
import kNN
import matplotlib
import matplotlib.pyplot as plt

fig = plt.figure()
ax1 = fig.add_subplot(311)
datingDataMat,datingLabels = kNN.file2matrix('f:\\datingTestSet.txt')
ax1.scatter(datingDataMat[:,0],datingDataMat[:,1],
           15.0*numpy.array(datingLabels),15.0*numpy.array(datingLabels))
ax1.set_xlabel('fly')
ax2 = fig.add_subplot(312)
ax2.scatter(datingDataMat[:,0],datingDataMat[:,2],
           15.0*numpy.array(datingLabels),15.0*numpy.array(datingLabels))
ax2 = fig.add_subplot(313)
ax2.scatter(datingDataMat[:,1],datingDataMat[:,2],
           15.0*numpy.array(datingLabels),15.0*numpy.array(datingLabels))
plt.show()
