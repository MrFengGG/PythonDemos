import re

def process(filename,encod = "utf-8"):
    file = open(filename).readlines()
    reg = re.compile("/\*.*\*/")
    for line in file:
        line = reg.sub("",line)
        print(line)

if __name__ =="__main__":
    process("f://java/MessageProducer.java")
    print("||||||||||||||||||||||||||||||||||||||||||||||||||")
