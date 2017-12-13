import copy

def get_data(filename):
    data = []
    file = open(filename)
    datas = file.readlines()
    file.close()
    for number in datas:
        data.append(int(number))
    return data


def get_distance(data1,data2):
    dis1 = 0
    dis2 = 0 
    for i in range(len(data1)):
        dis1 += data1[i]
        dis2 += data2[i]
    dis = dis1/len(data1) - dis2/len(data2)
    return dis
def count_bad_number(data,bad_num=60000):
    count=0
    for num in data:
        if num == bad_num:
            count+=1
    return count

def index_good_number(data,good_num=60000):
    index = []
    for i in range(len(data)):
        if data[i]==good_num:
            index.append(i)
    return index

def change_bad_data(data):
    fir_temp=[]
    las_temp = []
    re_number=[]
    for i in range(len(data)):
        if i < 2190:
            if data[i] !=60000 and data[i+1]==60000:
                fir_temp.append(i)
            if data[i] == 60000 and data[i+1]!=60000:
                las_temp.append(i+1)
            
    for i in range(len(las_temp)):
        #print(fir_temp[i],"is",numbers[fir_temp[i]],las_temp[i],"is",numbers[las_temp[i]])

        dis = las_temp[i]-fir_temp[i]
        dis_num = abs(data[las_temp[i]] - data[fir_temp[i]])
        sum_num = dis_num/dis
        for one in range(dis-1):
            if(data[las_temp[i]] > data[fir_temp[i]]):
                re_number.append([fir_temp[i]+one+1,data[fir_temp[i]]+(one+1)*sum_num])
            if(data[las_temp[i]] < data[fir_temp[i]]):
                re_number.append([fir_temp[i]+one+1,data[fir_temp[i]]-(one+1)*sum_num])
            
    for i in range(len(re_number)):
        nu = re_number[i][0]
        data[nu] = round(re_number[i][1])
    data[-1]=1210
    return data

def data2_to_data1(data1,data2):
    data2 = copy.deepcopy(data2)
    index2 = index_good_number(data2)
    index1 = index_good_number(data1)
    for i in index2:
        if i not in index1:
            data2[i] = data1[i]
    return data2


def add_good_num(data,index,good_num=60000):
    temp_data = copy.deepcopy(data)
    for i in index:
        temp_data[i] = good_num
    return temp_data

def save_data(data,filename):
    file = open(filename,"w")
    for i in data:
        file.write(str(i)+"\n")
    file.close()

if __name__ =="__main__":
    '''
    data1 = get_data("F:/工作/错误数据/20170630020730872.txt")
    good_data = get_data("F:/工作/正常.txt")
    data1 = data2_to_data1(good_data,data1)
    data1 = change_bad_data(data1)
    index = index_good_number(good_data)
    data1 = add_good_num(data1,index)
    print(get_distance(data1,good_data))
    save_data(data1,"F:/工作/转换数据/20170630020730872.txt")
    '''
    data1 = get_data("F:/工作/转换数据/20170630020730872.txt")
    data2 = get_data("F:/工作/正常.txt")
    print("平均数的差为",get_distance(data1,data2))
