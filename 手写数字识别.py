import numpy
import operator
import os
from PIL import Image

def classify(inX,dataSet,labels,k=3):
    '''
    算法的实现
    '''
    dataSetSize = dataSet.shape[0]

    diffMat = numpy.tile(inX,(dataSetSize,1)) - dataSet
    sqDiffMat = diffMat**2
    sqDistance = sqDiffMat.sum(axis=1)
    print(sqDistance)
    distance = sqDistance**0.5
    print(distance,labels)
    sortedDistIndicies = distance.argsort()

    classCount = {}

    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel,0)+1
    sortedClassCount = sorted(classCount.items(),key=operator.itemgetter(1),
                              reverse = True)
    print(sortedClassCount)
    return sortedClassCount[0][0]
def trainfiletovector(filename):
    '''
    将一个文本文件解析成向量,这是<<机器学习实战>>书中的例子
    他是将一个已经转换成字符文件的数字解析成向量的函数
    这里不用
    '''
    returnVector = numpy.zeros((1,1024))
    file = open(filename)
    for i in range(32):
        lineStr = file.readline()
        for j in range(32):
            returnVector[0,32*i+j] = int(lineStr[j])
    return returnVector
def getTrainSet(filename):
    '''
    根据一个字符串图片文件夹解析出训练集和标签列表
    同样来自<<机器学习实战>>这里也不用
    '''
    Labels = []
    trainingFileList = os.listdir(filename)
    m = len(trainingFileList)
    trainingMat = numpy.zeros((m,1024))
    for i in range(m):
        fileNameStr = trainingFileList[i]
        fileStr = fileNameStr.split('.')[0]
        NumStr = int(fileStr.split('_')[0])
        Labels.append(NumStr)
        trainingMat[i,:] = trainfiletovector(filename+'\\%s'%fileNameStr)
    return trainingMat,Labels    
def ImgToVector(picname):
    '''
    将一个图片转化成向量的函数
    '''
    #打开一张图片
    origimg = Image.open(picname)
    #将图片分辨率转化成32*32
    resizeimg = origimg.resize((32,32))
    #将图片二值化
    bimg = resizeimg.convert('1')
    #将二值化图片转化成数组
    imgarray = numpy.array(bimg)
    #图片向量
    formatarray = numpy.zeros((1,1024))
    #图片向量赋值
    for i in range(32):
        for j in range(32):
            if imgarray[i][j]:
                formatarray[0,i*32+j] = 0
            else:
                formatarray[0,i*32+j] = 1
    return formatarray
def getTrainSetByImg(filename):
    '''
    用一个图片文件夹获得训练集,标签向量
    '''
    Labels = []
    trainingFileList = os.listdir(filename)
    m = len(trainingFileList)
    trainingMat = numpy.zeros((m,1024))
    for i in range(m):
        fileNameStr = trainingFileList[i]
        fileStr = fileNameStr.split('.')[0]
        label = int(fileStr.split('_')[0])
        Labels.append(label)
        trainingMat[i,:] = ImgToVector(filename+'\\'+fileNameStr)
    return trainingMat,Labels
def Utis():
    '''
    用于判断属于哪个数字的函数
    '''
    trainingMat,Labels = getTrainSetByImg('F:\\train')
    inX = ImgToVector('F:\\test\\3_8.jpg')
    re = classify(inX,trainingMat,Labels,5)
    return re
def Test():
    print(Utis())
if __name__ == '__main__':
    Test()
    
