import re
m = re.search("a","aaaacdfdfdfsfaaaaadsdwaa")
for a in m.group(0):
    print(a)
    
