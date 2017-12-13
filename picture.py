#自变量
x = [[1.0,1.5],[1.3,1.9],[1.5,2.3],[1.7,2.7],[1.9,3.1],[2.1,3.5].[2.3,3.9],[2.5,4.3],[2.7,4.7],[2.9,5.1]]
#因变量
y = [2.5,3.2,3.9,4.6,5.3,6,6.7,7.4,8.1,8.8]

#训练集的长度
m = len(x)
#参数数量
n = len(x[-1])
#循环的次数
times = 1000
theta = []
#将参量初始化为0
for i in n:
    theta.append(0)
for i in range(times):
    error=[]
    grand = []
    for b in range(m):
        error.append(0)
    for c in range(n):
        grand.append(0)
    for j in range(m):
        hp = 0
        for k in range(n):
            #将x带入参数计算值
            hp += theta[k]*x[j][k]
        error[j] = y[j] - hp
        for l in range(n):
            grand[l] = sum([num[l] for num in x])
    for i in range(n):
        theta[i] = theta[i] - grand[l]
print(theta)
        

    
