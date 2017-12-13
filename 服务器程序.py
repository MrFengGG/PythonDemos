import socket
s = socket.socket()

host = socket.gethostname()
port = 1234

s.bind(('localhost',port))

s.listen(5)
while True:
    c,addr= s.accept()
    print('获得一个连接',addr)
    c.send('你好客户端'.encode())
    c.close()
