import re
import os

PATH = "F:/工作/grm/grm/classes.src/com"

def process(filename,savefilename):
    filesave = open(savefilename,"w")
    reg = re.compile("/\*.*\*/")
    reg2 = re.compile("\n\n")
    file = open(filename,encoding="utf-8").read()
    text = reg.sub("",file)
    filesave.write(text)
    filesave.close()

def parse_dir(dirname):
    '''
    列出一个文件夹下的所有文件夹和文件
    '''
    dirs=[]
    files=[]
    temps = os.listdir(dirname)
    for dir in temps:
        dir = dirname+"/"+dir
        if os.path.isdir(dir):
            dirs.append(dir)
            dirs,files=parse_dir(dir)
            files.extend(files)
        else:
            files.append(dir)
    return dirs,files

if __name__=="__main__":
    java = ""
    dir,files = parse_dir(PATH+"/haut")
    reg = re.compile("/\*.*\*/")
    reg2 = re.compile("\n\n")
    for file in files:
        text = open(file,encoding="utf-8").read()
        
        text = reg.sub("",text)
        text = reg2.sub("",text)
        java+=text
    savefile = open("f://1.txt","w")
    savefile.write(java)
    savefile.close()
