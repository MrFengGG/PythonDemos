import numpy
import cv2

img = cv2.imread("C:/Users/JACK/Desktop/CAT.jpg")
w = img.shape[1]
h = img.shape[0]

for xi in range(w):
    for xj in range(h):
        img[xj,xi,0] = int(img[xj,xi,0]*0.7)
        img[xj,xi,1] = int(img[xj,xi,1]*0.7)
        img[xj,xi,2] = int(img[xj,xi,2]*0.7)
cv2.namedWindow("img")
cv2.imshow("img",img)
cv2.waitKey()
cv2.destroyAllWindows()
        
