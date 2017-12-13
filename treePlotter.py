import matplotlib.pyplot as plt
from pylab import *

mpl.rcParams['font.sans-serif'] = ['SimHei']

#定义决策节点和叶节点的格式
decisionNode = dict(boxstyle = 'sawtooth',fc='0.8')
leafNode = dict(boxstyle = 'round4',fc = '0.8')
arrow_args = dict(arrowstyle = '<-')

def getNumnLeafs(MyTree):
    '''
    获得叶节点的数量
    '''
    numLeafs = 0
    firstStr = list(MyTree.keys())[0]
    secoundDict = MyTree[firstStr]
    for key in secoundDict.keys():
        if type(secoundDict[key]).__name__ == 'dict':
                numLeafs += getNumnLeafs(secoundDict[key])
        else:numLeafs += 1
    return numLeafs

def getTreeDepth(myTree):
    '''
    获取决策树的深度
    '''
    maxDepth = 0
    firstStr = list(myTree.keys())[0]
    secoundDict = myTree[firstStr]
    for key in secoundDict.keys():
        if type(secoundDict[key]).__name__ == 'dict':
            thisDepth = 1 + getTreeDepth(secoundDict[key])
        else:thisDepth = 1
        if thisDepth > maxDepth:maxDepth = thisDepth
    return maxDepth

def plotNode(nodeTxt, centerPt, parentPt, nodeType):
    createPlot.ax1.annotate(nodeTxt, xy=parentPt,  xycoords='axes fraction',
             xytext=centerPt, textcoords='axes fraction',
             va="center", ha="center", bbox=nodeType, arrowprops=arrow_args )
    
def retrieveTree(i):
    '''
    获得测试决策树
    '''
    listOfTree = [{'no surfacing':{0:'no',1:{'flippers':{0:'no',1:'yes'}}}},
                  {'no surfacing':{0:'no',1:{'flippers':{0:{'head':{0:'no',1:'yes'}},1:'no'}}}}]
    return listOfTree[i]

def plotMidText(cntrPt,parentPt,txtString):
    xMid = (parentPt[0] - cntrPt[0])/2.0 + cntrPt[0]
    yMid = (parentPt[0] - cntrPt[1])/2.0 + cntrPt[1]
    createPlot.ax1.text(xMid,yMid,txtString)

def plotTree(MyTree,parentPt,nodeTxt):
    numLeafs = getNumnLeafs(MyTree)
    depth = getTreeDepth(MyTree)
    firstStr = list(MyTree.keys())[0]
    cntrPt = (plotTree.x0ff + (1.0 + float(numLeafs))/2.0/plotTree.totalW,plotTree.y0ff)
    plotMidText(cntrPt,parentPt,nodeTxt)
    plotNode(firstStr,cntrPt,parentPt,decisionNode)
    secoundDict = MyTree[firstStr]
    plotTree.y0ff = plotTree.y0ff - 1.0/plotTree.totalD
    for key in secoundDict.keys():
        if type(secoundDict[key]).__name__ == 'dict':
            plotTree(secoundDict[key],cntrPt,str(key))
        else:
            plotTree.x0ff = plotTree.x0ff + 1.0/plotTree.totalW
            plotNode(secoundDict[key],(plotTree.x0ff,plotTree.y0ff),cntrPt,leafNode)
            plotMidText((plotTree.x0ff,plotTree.y0ff),cntrPt,str(key))
        plotTree.y0ff = plotTree.y0ff + 1.0/plotTree.totalD

def createPlot(inTree):
    fig = plt.figure(1,facecolor = 'white')
    fig.clf
    axprops = dict(xticks=[],yticks=[])
    createPlot.ax1 = plt.subplot(111,frameon=False,**axprops)
    plotTree.totalW = float(getNumnLeafs(inTree))
    plotTree.totalD = float(getTreeDepth(inTree))
    plotTree.x0ff = -0.5/plotTree.totalW
    plotTree.y0ff = 1.0
    plotTree(inTree,(0.5,1.0),'')
    plt.show()

def test():
    '''
    测试函数
    '''
    listofTree = retrieveTree(1)
    listofTree0 = retrieveTree(0)
    createPlot(listofTree0)
if __name__ == '__main__':
    test()
    
