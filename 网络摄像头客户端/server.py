import socket
from io import StringIO
from PIL import Image
import cv2

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind(("127.0.0.1", 10000))
sock.listen(2)

src,src_addr = sock.accept()
i = 0;
while True:
    msg = src.recv(1024*1024)
    if not msg:
        break
    img = cv2.CreateImageHeader((640, 480), cv2.IPL_DEPTH_8U, 3))
    cv2.imshow("camera",img)
    if (cv2.waitKey(1) & 0xFF) == ord('q'):
        break
sock.close()

cv2.DestoryAllWindows()