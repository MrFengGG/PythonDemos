import cv2
import time
import socket
from PIL import Image
from io import StringIO
import numpy

'''
视频摄像头的发送端
'''

capture = cv2.VideoCapture(0)
width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH)+0.5)
height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT)+0.5)
HOST,PORT = "127.0.0.1",10000
socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket.connect((HOST,PORT))

while True:
    result,img = capture.read()
    img = Image.fromarray(img)
    img = img.tobytes()
    '''
    buf = StringIO(img)
    jpeg = buf.getvalue()
    buf.close()
    
    transfer = jpeg.replace("\n","\-n")
    print(len(transfer),transfer[-1])
    '''
    #socket.sendall((transfer+"\n").encode())
    if img:
        socket.sendall(img)
    time.sleep(10)
socket.close()


