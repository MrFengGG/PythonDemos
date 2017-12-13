import jieba
import re
import os
import numpy
from collections import Counter
from math import log

def get_cut_word(sentence):
    '''
    用于对一个字符串进行分词
    '''
    sentence = re.sub("[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？、~@#￥%……&*（）]+","",sentence)
    sentence = re.sub(" ","",sentence)
    word_list = jieba.cut(sentence,cut_all=True)
    return [word for word in word_list if word != ""]

def load_train_word(dir):
    '''
    从一个文件加获取训练集
    '''
    train_label = []
    train_dataset = []
    for filename in os.listdir(dir):
        classify = filename.split("_")[0]
        filename = dir+"\\"+filename
        str = open(filename).read()
        str = str.strip()
        train_dataset.append(get_cut_word(str))
        train_label.append(float(classify))
    return train_dataset,train_label

def process_train(train_dataset,train_label,times):
    '''
    处理训练集,包括去除出现次数前times此的元素,并将其转化为numpy数组
    :param dataset: 
    :return: 
    '''
    return_dataset = []
    for i in train_dataset:
        res = Counter(i)
        res = res.most_common(times)
        for re in res:
            while re[0] in i:
                i.remove(re[0])
        return_dataset.append(i)
    return numpy.array(return_dataset),numpy.array(train_label)

def sent_to_vec(vocablist,input):
    return_vec = [0]*len(vocablist)
    for word in input:
        if word in vocablist:
            return_vec[vocablist.index(word)] += 1
        else:
            print("词集中没有该词")
    return return_vec

def createVocabList(dataSet):
    '''
    构造词集
    :param dataSet: 
    :return: 
    '''
    vocabSet = set([])
    for document in dataSet:
        vocabSet = vocabSet | set(document)
    return list(vocabSet)

def train(train_set,train_label):
    '''
    计算P(Wi|C1)矩阵的函数
    :param train_set: 
    :param train_label: 
    :return: 
    '''
    train_num = len(train_set)
    p_calss1 = sum(train_label)/float(train_num)
    num_word = len(train_set[0])
    p_word_0 = numpy.ones(num_word)
    p_word_1 = numpy.ones(num_word)
    p0_word_count = 2
    p1_word_count = 2
    for i in range(train_num):
        if train_label[i] == 0:
            p_word_0 += train_set[i]
            p0_word_count += sum(train_set[i])
        else:
            p_word_1 += train_set[i]
            p1_word_count += sum(train_set[i])
    p1_vec = numpy.log(p_word_1/p1_word_count)
    p0_vec = numpy.log(p_word_0/p0_word_count)
    return p0_vec,p1_vec,p_calss1

def classify(dir):
    train_set,train_label = load_train_word(dir)
    train_set, train_label = process_train(train_set,train_label,5)
    Vocablist = createVocabList(train_set)
    train_mat = []
    for doc in train_set:
        train_mat.append(sent_to_vec(Vocablist,doc))
    p0v,p1v,p1 = train(train_mat,train_label)
    input = train_mat[0]
    print(p0v)

    print(input)
    print(p0v,p1v)
    p0 = sum(input*p1v) + numpy.log(1-p1)
    p1 = sum(input*p1v) + numpy.log(p1)
    print(p0,p1)


if __name__ == "__main__":
    classify("f:\\凤凰传奇")