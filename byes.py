import numpy
import re
import random
import codecs
from math import log
from pymongo import mongo_client

def loadDataSet():
    '''
    用于产生训练用的文本和相关的标签
    '''
    postingList = [['my','dog','has','flea','problems','help','please'],
                   ['maybe','not','take','him','to','dog','park','stupid'],
                   ['my','dalmation','is','so','cute','I','love','him'],
                   ['stop','posting','stupid','worthless','garbage'],
                   ['mr','licks','ate','my','steak','how','to','stop','him'],
                   ['quit','buying','worthless','dog','food','stupid']]
    classVec = [0,1,0,1,0,1] #1代表侮辱性文字,0代表正常言论
    return postingList,classVec

def createVocabList(dataSet):
    '''
    用于将训练用的文本转化为一个不重复的词汇表
    :param dataSet: 要转换的训练文本
    :return: 一个不重复的词汇表
    '''
    vocabSet = set([])
    for document in dataSet:
        vocabSet = vocabSet | set(document)
    return list(vocabSet)

def setOfWords2Vcc(vocabList,inputSet):
    '''
    用于将需要测试的文本转换为一个词集向量
    :param vocabList: 训练用的词集
    :param inputSet: 需要转换的文本
    :return: 词集向量
    '''
    returnVec = [0] * len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] = 1
        else:print('the word:%s is not in my Vocabulary!'%word)
    return returnVec

def setOfWords2VecMN(vocabList,inputSet):
    '''
    用于将一个文本转换为需要的词袋向量
    :param vocabList: 训练用的词汇表
    :param inputSet: 需要转换的文本
    :return: 词袋向量
    '''
    returnVec = [0]*len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)]+=1
    return returnVec

def trainNB0(trainMatrix,trainCategory):
    '''
    计算每个词对应在两个结果中的条件概率,结果的概率,
    :param trainMatrix: 训练用的向量
    :param trainCategory: 训练用的标签列表
    :return: 每个词在某一结果中的条件概率
    '''
    numTrainDocs = len(trainMatrix)
    numWords = len(trainMatrix[0])
    pAbusive = sum(trainCategory)/float(numTrainDocs)
    p0Num = numpy.ones(numWords)
    p1Num = numpy.ones(numWords)
    p0Denom = 2.0
    p1Denom = 2.0
    for i in range(numTrainDocs):
        if trainCategory[i] == 1:
            p1Num += trainMatrix[i]
            p1Denom += sum(trainMatrix[i])
        else:
            p0Num += trainMatrix[i]
            p0Denom += sum(trainMatrix[0])
        p1Vect = numpy.log(p1Num/p1Denom)
        p0Vect = numpy.log(p0Num/p0Denom)
    return p0Vect,p1Vect,pAbusive

def classfyNB(vec2Classify,p0Vec,p1Vec,pClass1):
    '''
    计算输入的文本属于两个结果中的概率
    :param vec2Classify: 待检测的文本
    :param p0Vec: 在结果0中每个词汇的条件概率
    :param p1Vec: 在结果1中每个词汇的条件概率
    :param pClass1: 结果1的概率
    :return: 文本属于某一结果概率最大对对应结果
    '''
    p1 = sum(vec2Classify*p1Vec)+log(pClass1)
    p0 = sum(vec2Classify*p0Vec)+log(pClass1)
    if(p1>p0):
        return 1
    else:
        return 0

def textParse(bigString):
    '''
    解析文件
    :param bigString: 需要解析的字符串
    :return: 解析完成的文本
    '''
    listOfTokens = re.split(r'\W*',bigString)
    return [tok.lower() for tok in listOfTokens if len(tok) > 2]

def spamTest():
    docList = []
    classList = []
    fullText = []
    for i in range(1,26):
        wordList = textParse(open('f:\\email\\spam\\%d.txt' % i).read())
        docList.append(wordList)
        fullText.extend(wordList)
        classList.append(1)
        wordList = textParse(open('f:\\email\\ham\\%d.txt' % i).read())
        docList.append(wordList)
        fullText.extend(wordList)
        classList.append(0)
    vocabList = createVocabList(docList)
    trainingSet = list(range(50))
    testSet = []
    for i in range(10):
        randIndex = int(random.uniform(0,len(trainingSet)))
        testSet.append(trainingSet[randIndex])
        del(trainingSet[randIndex])
    trainMat = [];trainClasses = []
    for docIndex in trainingSet:
        trainMat.append(setOfWords2Vcc(vocabList,docList[docIndex]))
        trainClasses.append(classList[docIndex])
    p0V,p1V,pSpam = trainNB0(trainMat,trainClasses)
    errorCount = 0
    print(testSet)
    for docIndex in testSet:
        wordVector = setOfWords2VecMN(vocabList,docList[docIndex])
        print(docList[docIndex])
        print(wordVector)
        if classfyNB(wordVector,p0V,p1V,pSpam) != classList[docIndex]:
            print('error',docIndex,classList[docIndex],'to',classfyNB(wordVector,p0V,p1V,pSpam))
            errorCount+=1
    print('the error rate is :',float(errorCount/len(testSet)))

def test():
    '''
    测试函数
    '''
    spamTest()
if __name__ == '__main__':
    test()

