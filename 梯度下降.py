import numpy as np
import random

def gettheta2(x,y,times,step):
    '''
    随机梯度下降算法
    '''
    a, b = np.shape(x)
    train = np.ones((a, b + 1))
    m, n = np.shape(train)
    train[:, 1:] = x
    theta = np.zeros(n)
    for i in range(times):
        a = random.randint(0,m-1)
        randm_train = train[a]
        randm_label = y[a]
        hp = np.dot(randm_train,theta.transpose())
        error = randm_label - hp
        grand = np.dot(randm_train.transpose(),error)
        theta = theta+grand*step
    return theta


def gettheta1(x,y,times,step):
    '''
    批量梯度下降算法
    '''
    a,b = np.shape(x)
    train = np.ones((a,b+1))
    m, n = np.shape(train)
    train[:,1:] = x
    theta = np.zeros(n)
    for i in range(times):
        hp = np.dot(train,theta.transpose())
        error = hp - y
        grand = np.dot(train.transpose(),error)/m
        theta = theta- step*grand
    return train,theta

def liner(x,labe,times,step,input):
    theta = gettheta2(x,labe,times,step)
    result = np.dot(input,theta)


if __name__ == "__main__":
    input = np.array([1,3.1,5.5])
    liner(x,y,1000,0.01,input)