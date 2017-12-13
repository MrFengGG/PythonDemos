file = open("F:/工作/正常.txt")
text = file.readlines()
file.close()
numbers = []
fir_temp = []
las_temp = []
re_number=[]
file = open("f:/工作/正常格式化2.txt","w")

for number in text:
    numbers.append(int(number))

for i in range(len(numbers)):
    if i < 2190:
        if numbers[i] !=60000 and numbers[i+1]==60000:
            fir_temp.append(i)
        if numbers[i] == 60000 and numbers[i+1]!=60000:
            las_temp.append(i+1)
            
for i in range(len(las_temp)):
    #print(fir_temp[i],"is",numbers[fir_temp[i]],las_temp[i],"is",numbers[las_temp[i]])

    dis = las_temp[i]-fir_temp[i]
    dis_num = abs(numbers[las_temp[i]] - numbers[fir_temp[i]])
    sum_num = dis_num/dis
    for one in range(dis-1):
        if(numbers[las_temp[i]] > numbers[fir_temp[i]]):
            re_number.append([fir_temp[i]+one+1,numbers[fir_temp[i]]+(one+1)*sum_num])
        if(numbers[las_temp[i]] < numbers[fir_temp[i]]):
            re_number.append([fir_temp[i]+one+1,numbers[fir_temp[i]]-(one+1)*sum_num])
            
for i in range(len(re_number)):
    nu = re_number[i][0]
    numbers[nu] = re_number[i][1]

for i in range(len(numbers)):
    print(round(numbers[i]))
    file.write(str(round(numbers[i]))+"\n")
file.close()
        
    
