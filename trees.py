from math import log
import operator
import treePlotter
import pickle

def calcShannoEnt(dataSet):
    '''
    根据一个给定的数据集求香农熵,这里开始没搞懂,后来复习了一下信息论与编码总算是搞明白了
    例如这个数据集,我们需要了解的信息是"是否为水生生物",而描述一个信息的信息量的大小是取决于他的不确定度(即这个信息出现的概率)
    为什么这么理解,例如,一个生物是水生生物的概率为2/5,即不确定度为2/5,那么当我们知道这个动物属于水生生物时,2/5的不确定度就被消除了,可以理解为消除的不确定度就是我们获得的信息
    一个信息所含有的信息量我们用自信息量来衡量,它的
    计算公式是I = -log('一事件出现的概率',2),其中2代表对数以2为底,比如这里我们假设是水生生物的概率为2/5,不是水生生物的概率为3/5,那么他们的信息量分别为-log(2/5,2),-log(3/5,2)
    熵(这本书上说得是香农熵)其实就是信息的平均不确定度,数值上等于平均信息量,即当我们知道一个动物是水生生物或者不是水生生物所获得的平均信息量,计算公式为
    某事件的概率*某事件的自信息量求和,例如是否为水生生物的熵为(2/5)*(-log(2/5,2))+(3/5)*(-log(3/5,2))
    信息增益在网上查阅了一些资料也能理解了
    例如我们要判断在一群人中一个人的性别是男是女,判断成功的概率为1/2,是男是女事件分别对应的自信息量为1,平均信息量为0.5
    而人有如下特点1:是否有喉结,2:头发长短
    当我们用特征值1,即有无喉结来划分这一群人,数据集就被我们划分成了两波人,有喉结的人和无喉结的人
    当我们在有喉结的人中判断是男人还是女人的时候,判断成功的概率为1,自信息量和平均信息量都是0
    信息增益就等于未划分之前的平均信息量-划分之后的平均信息量
    简单理解,信息增益就是我们用一个特征(有无喉结)将一个数据集(人类)划分之后,对我们判断某一事物(男人还是女人)的帮助是多大
    比如有无喉结和头发长短,基本上有喉结的肯定是男人,而长头发的不一定肯定是女人,那么有无喉结的特征对我们判断性别的信息增益就比头发长短要大
    '''
    numEntries = len(dataSet)

    labelCounts = {}
    for featVec in dataSet:
        currentLabel = featVec[-1]
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1
    shannonEnt = 0.0
    for key in labelCounts:
        prob = float(labelCounts[key])/numEntries
        shannonEnt -= prob*log(prob,2)
    return shannonEnt

def splitDataSet(dataSet,axis,value):
    '''
    根据给定的数据集,划分数据集的特征,特征的返回值来划分数据集
    '''
    returnSet = []
    for featVec in dataSet:
        if featVec[axis] == value:
            reducedFeatVec = featVec[:axis]
            reducedFeatVec.extend(featVec[axis+1:])
            returnSet.append(reducedFeatVec)
    return returnSet

def createTestSet():
    dataSet = [[1,1,'yes'],
               [1,1,'yes'],
               [1,0,'no' ],
               [0,1,'no' ],
               [0,1,'no' ]]
    labels = ['no surfacing','flippers']
    return dataSet,labels

def chooseBestFeatureToSplit(dataSet):
    '''
    选择最好的划分特征,即最大的信息增益
    '''
    numFeatures = len(dataSet[0]) - 1
    baseEntropy = calcShannoEnt(dataSet)
    bestInfoGain = 0.0
    bestFeature = -1
    for i in range(numFeatures):
        featList = [example[i] for example in dataSet]
        #value去重
        uniqueVals = set(featList)
        newEntropy = 0.0
        for value in uniqueVals:
            subDataSet = splitDataSet(dataSet,i,value)
            prob = len(subDataSet)/float(len(dataSet))
            newEntropy += prob * calcShannoEnt(subDataSet)
        infoGain = baseEntropy - newEntropy
        if infoGain > bestInfoGain:
            bestInfoGain = infoGain
            bestFeature = i
    return bestFeature

def majorityCnt(classList):
    '''
    在一个列表中返回最多的值
    '''
    classCount = {}
    for vote in classList:
        if vote not in classCount.keys():
            classCount[vote] = 0
        classCount[vote] += 1
    sortedClassCount = sorted(classCount.item(),key = operator.itemgetter(1),reverse = True)
    return sortedClassCount[0][0]

def createTree(dataSet,labels):
    '''
    构建决策树
    决策树递归过程:开始一直无法理解迭代过程中有一个if-return语句,如果直接满足条件不是直接会退出程序吗?
    在网上找到一个非常好的答案帮我解决了这个问题,一句话就是return之前需要将程序运行完毕,例如如下函数
        def fact(n):
          if n==1:
            return 1
          return n * fact(n - 1)
    迭代过程如下:
        ===> fact(5)
        ===> 5 * fact(4)
        ===> 5 * (4 * fact(3))
        ===> 5 * (4 * (3 * fact(2)))
        ===> 5 * (4 * (3 * (2 * fact(1))))
    在return之前,n * fact(n - 1)必须要计算完毕
    本程序中的createTree(dataSet,labels)函数与之类似,在return之前,myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet,bestFeat,value),subLabels)必须计算完毕
    设dataSet为create为:
    [[1,1,'yes'],    lebels为['no surfacing','flippers']
     [1,1,'yes'],
     [1,0,'no' ],
     [0,1,'no' ],
     [0,1,'no' ]]
    第一次迭代有两个分支1:MyTree['no surfacing'][0] = createTree([[1,'no'],[1,'no'])
                        2:MyTree['no surfacing'][1] = createTree([[1,'yes'],[1,'yes'],[0,'no'])
    分支1进入一次迭代直接满足条件classList.count(classList[0]) == len(classList),直接等于'no'
    分支2进入一次迭代后有两个分支2_1:MyTree['no surfacing'][1]['flippers'][0] = createTree([['no']])
                                 2_1:MyTree['no surfacing'][1]['flippers'][1] = createTree([['yes'],['yes]])
    2_1,2_2满足第一条语,2_1返回'no',2_2返回'yes',最后计算结果
    MyTree['no surfacing'][0] = 'no'
    MyTree['no surfacing'][1]['flippers'][0] = 'no'
    MyTree['no surfacing'][1]['flippers'][1] = 'yes'
    即{'no surfacing'{0:'no',1:{'flippers':{0:'no',1:'yes'}}}}
    
                        
    '''
    #dataSet的'yes' or 'no'集合,在本书中的测试例子中第一次迭代时classList = ['yes','yes','no','no']
    classList = [example[-1] for example in dataSet]
    #如果集合全部一样,返回这个值
    if classList.count(classList[0]) == len(classList):
        return classList[0]
    #如果特征值消耗完,返回最多的值
    if len(dataSet[0]) == 1:
        return majorityCnt(classList)
    #首先使用信息增益值最大的特征值进行分类
    bestFeat = chooseBestFeatureToSplit(dataSet)
    #该特征值的标签
    bestFeatLabel = labels[bestFeat]
    #用字典来表示决策树
    myTree = {bestFeatLabel:{}}
    #将该特征值的标签从标签列表中删除
    del(labels[bestFeat])
    #求出特征值在每组数据中的值
    featValues = [example[bestFeat] for example in dataSet]
    uniqueVals = set(featValues)
    #依据特征值的值来划分数据集
    for value in uniqueVals:
        subLabels = labels[:]
        myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet,bestFeat,value),subLabels)
    return myTree 

def classify(inputTree,featLabels,testVec):
    '''
    利用决策树对给定的特征值的对象进行分类
    '''
    #树的一号决策点,测试决策树中是'no surfacing'
    firstStr = list(inputTree.keys())[0]

    #测试决策树中是{0:'no',1:{'flippers':{0:'no',1:'yes'}}}
    secoundDict = inputTree[firstStr]
    #返回'no sufacing'在标签列表中的位置
    featIndex = featLabels.index(firstStr)

    #进入循环,如果到达叶节点,返回分类,如果没有到达,迭代
    for key in secoundDict.keys():
        if testVec[featIndex] == key:
            if type(secoundDict[key]).__name__ == 'dict':
                classLabel = classify(secoundDict[key],featLabels,testVec)
            else:classLabel = secoundDict[key]
    return classLabel

def storeTree(inputTree,filename):
    '''
    用于将构造好的决策树存储到文件中
    '''
    fw = open(filename,'wb')
    pickle.dump(inputTree,fw)
    fw.close()

def grabTree(filename):
    '''
    用于获取文件中存储的决策树
    '''
    fr = open(filename,'rb')
    return pickle.load(fr)
    
def test():
    fr = open('f:\\lenses.txt')
    lenses = [inst.strip().split('\t') for inst in fr.readlines()]
    lenselabels = ['age','prescript','astigmatic','tearRate']
    lenseTree = createTree(lenses,lenselabels)
    print(lenseTree)

if __name__ == '__main__':
    test()

'''
决策树很好的匹配了实验数据,但是匹配选项可能太多了,我们将这种问题称为过度匹配
为了减少过度匹配,可以裁剪决策树,去掉一些不必要的叶子节点,如果叶子节点只能增加
少许信息,可以删除该节点
决策树就像带有终止模块的流程图,终止块表示分类结果,处理数据集时
首先要测量集合中数据的熵
然后选择最优方案划分数据集,直到数据集中的所有数据属于同一分类

'''
