import re

def replaceWord(inputfilename,outputfilename,*words):
    '''
    用于替换一个文本中的所有词
    '''
    inputfile = open(inputfilename,encoding='utf-8').read()
    outputfile = open(outputfilename,'w')
    for i in words:
        inputfile = re.sub(i[0],i[1],inputfile)
    print(inputfile)
    outputfile.write(inputfile)
    outputfile.close()

def test():
    replaceWord('f:\\1.txt','f:\\1.txt',
                ['L_min_u','min_length_Str'],['L_max_u','max_length_Str'],['L_delt_u','inc_of_Str'],['a_string','String'])
if __name__ == '__main__':
    test()
    
        
    
