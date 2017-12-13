def lines(file):
    for line in file:
        yield line
        yield '\n'
def blocks(file):
    block=[]
    for line in lines(file):
        if line.strip():
            block.append(line)
        elif block:
            yield ''.join(block).strip()
            block=[]
def test():
    for block in blocks(open('f:\\python.txt')):
        print(block)
if __name__ == '__main__':
    test()
