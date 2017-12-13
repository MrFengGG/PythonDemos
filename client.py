import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect(("127.0.0.1",9999))

i = 0;
while True:
    i+=1;
    try:
        message = open("f:\\图片测试\\"+str(i)+".jpg","rb").read()

    except:
        print("yichang",i)
        break
    sock.send(message)
    print(message)
    if message == "q":
        break
    

        
             
