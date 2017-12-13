
def reverse(string):
    '''
    折半查找法迭代实现
    '''
    for i in range(1,len(string)+1):
        print(string[-i])

def printa(string,num):
    '''
    折半查找法递归实现
    '''
    str = string[num]
    if str!="0":
        printa(string,num+1)
    if str!="0":
        print(string[num])

def search_diedai(arrays,num):
    '''
    折半查找法迭代实现
    '''
    lo = 0
    hi = len(arrays)
    while(lo<hi):
        mid = int(lo+(hi-lo)/2)
        if num == arrays[mid]:
            return mid
        elif num > arrays[mid]:
            lo = mid+1
        elif num < arrays[mid]:
            hi = mid-1
    return -1

def search_digui(arrays,lo,hi,num):
    '''
    折半查找法递归实现
    '''
    if lo > hi:
        return -1
    mid = int(lo+(hi-lo)/2)
    if num == arrays[mid]:
        return mid
    elif num > arrays[mid]:
        return search_digui(arrays,mid+1,hi,num)
    else:
        return search_digui(arrays,lo,mid-1,num)

def hanno_tower(n,x,y,z):
    '''
    汉诺塔问题
    '''
    if n == 1:
        print("%s-->%s"%(x,z)) #将x的最后一个盘子直接移动到z上
    else:
        hanno_tower(n-1,x,z,y) #将n-1个盘子借助z移动到y上
        print("%s-->%s"%(x,z)) #将x的最后一个盘子移动到z上
        hanno_tower(n-1,y,x,z) #将已经移动到y上的n-1个盘子移动到z上
        
    
    
if __name__=="__main__":
    hanno_tower(2,"x","y","z")
