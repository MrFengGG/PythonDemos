import numpy
import operator
import os

def createDataSet():
    '''
    返回一个训练集和标签向量
    '''
    #训练集
    group = numpy.array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    #标签向量
    labels = ['A','A','B','B']
    return group,labels
def classify0(inX,dataSet,labels,k):
    '''
    用于实现k_近邻算法,接收输入一个向量,一个训练集,一个标签向量,一个K值
    判断向量所属的类别
    '''
    #读取矩阵第一维度的长度
    dataSetSize = dataSet.shape[0]
    #输入向量与训练集差值的数组
    diffMat = numpy.tile(inX,(dataSetSize,1)) - dataSet
    #计算各点与训练集的距离
    sqDiffMat = diffMat**2
    sqDistances = sqDiffMat.sum(axis=1)
    distance = sqDistances**0.5
    #将距离数组的下标按照距离大小排序
    sortedDistIndicies = distance.argsort()
    classCount = {}
    #在k的范围内,分别计算两类的数目
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel,0)+1
    #以k以内类别数目排序
    sortedClassCount = sorted(classCount.items(),key=operator.itemgetter(1),
                              reverse = True)
    #返回数目最多的类(即输入向量应该属于的类)
    return sortedClassCount[0][0]

def file2matrix(filename):
    '''
    用于解析训练集文件
    '''
    ValueOfClassLabel = {}
    Value = [1,2,3]
    def getValueOfClassLabel(ClassLabel):
        val = 1;
        if not ClassLabel in ValueOfClassLabel.keys():
            ValueOfClassLabel[ClassLabel] = Value.pop()
        return ValueOfClassLabel[ClassLabel]
            
    file = open(filename)
    arrayOLines = file.readlines()
    #文件的行数
    numberOfLines = len(arrayOLines)
    #返回创建的训练集
    returnMat = numpy.zeros((numberOfLines,3))
    classLabelVector = []
    index = 0
    for line in arrayOLines:
        line = line.strip()
        listFormLine = line.split('\t')
        returnMat[index,:] = listFormLine[0:3]
        classLabelVector.append(getValueOfClassLabel(str(listFormLine[-1])))
        index +=1
    return returnMat,classLabelVector
def autoNum(dataSet):
    '''
    用于将数据归一化
    '''
    #获取每一列的最小值
    minVals = dataSet.min(0)
    #获取每一列的最大值
    maxVals = dataSet.max(0)
    #最大值和最小值的差
    ranges = maxVals - minVals

    #将每一行归一化
    normDataSet = numpy.zeros(numpy.shape(dataSet))
    m = dataSet.shape[0]
    normDataSet = dataSet - numpy.tile(minVals,(m,1))
    normDataSet = normDataSet/numpy.tile(ranges,(m,1))
    return normDataSet,ranges,minVals
def datingClassTest():
    '''
    用于测试分类器
    '''
    hoRatio = 0.10
    datingDataMating,datingLabels = file2matrix('f:\\datingTestSet.txt')
    normMat,ranges,minVals = autoNum(datingDataMating)
    m = normMat.shape[0]
    numTestVecs = int(m*hoRatio)
    errorCount = 0.0
    for i in range(numTestVecs):
        classifierResult = classify0(normMat[i,:],normMat[numTestVecs:m,:],
                                     datingLabels[numTestVecs:m],3)
        print('the classifier came back with: %d,the real answer is:%d'%
              (classifierResult,datingLabels[i]))
        if(classifierResult != datingLabels[i]):errorCount += 1.0
    print('the total error rate is:%f'%(errorCount/float(numTestVecs)))
def img2Vector(filename):
    '''
    用于将图像文本文件转换成需要的格式
    '''
    returnVect = numpy.zeros((1,1024))
    fr = open(filename)
    for i in range(32):
        lineStr = fr.readline()
        for j in range(32):
            returnVect[0,32*i+j] = int(lineStr[j])
    return returnVect
def getSet(filename):
    hwLabels = []
    trainingFileList = os.listdir(filename)
    m = len(trainingFileList)
    trainingMat = numpy.zeros((m,1024))
    for i in range(m):
        fileNameStr = trainingFileList[i]
        fileStr = fileNameStr.split('.')[0]
        classNumStr = int(fileStr.split('_')[0])
        hwLabels.append(classNumStr)
        trainingMat[i,:] = img2Vector('f:\\trainingDigits\\%s'%fileNameStr)
    return trainingMat,hwLabels
def handwritingClassTest():
    hwLabels = []
    trainingFileList = os.listdir('f:\\trainingDigits')
    m = len(trainingFileList)
    trainingMat = numpy.zeros((m,1024))
    for i in range(m):
        fileNameStr = trainingFileList[i]
        fileStr = fileNameStr.split('.')[0]
        classNumStr = int(fileStr.split('_')[0])
        hwLabels.append(classNumStr)
        trainingMat[i,:] = img2Vector('f:\\trainingDigits\\%s'%fileNameStr)
    testFileList = os.listdir('f:\\testDigits')
    errorCount = 0.0
    mTest = len(testFileList)
    for i in range(mTest):
        fileNameStr = testFileList[i]
        fileStr = fileNameStr.split('.')[0]
        classNumStr = int(fileStr.split('_')[0])
        vectorUnderTest = img2Vector('f:\\testDigits\\%s'%fileNameStr)
        classifierResult = classify0(vectorUnderTest,trainingMat,hwLabels,3)
        print('the classifier came back with:%d,the real answer is :%d'%(classifierResult,classNumStr))
        if(classifierResult != classNumStr):errorCount += 1.0
    print('the total number of errors is:%d'%errorCount)
    print('the total error rate is :%f'%(errorCount/float(mTest)))
def test():
    t,b = getSet('f:\\trainingDigits')
if __name__ == '__main__':

    test()
