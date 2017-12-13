import util
from util import*
import re

fileinput = open('f:\\python.txt')
fileoutput = open(fileinput.name.split('.')[0]+'.html','w')
print(fileinput.name.split('.')[1]+'.html')
fileoutput.write('<html><head><title>...</title><body>')
title = True
for block in blocks(fileinput):
    block = re.sub(r'\*(.*?)\*',r'<em>\1</em>',block)
    if title:
        fileoutput.write('<h1>')
        fileoutput.write(block)
        fileoutput.write('</h1>')
        title = False
    else:
        fileoutput.write('<p>')
        fileoutput.write(block)
        fileoutput.write('</p>')
fileoutput.write('</body></html>')
print('替换标记成功')
fileinput.close()
fileoutput.close()
