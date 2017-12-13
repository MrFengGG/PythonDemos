import cv2
import numpy

img = cv2.imread("C:/Users/JACK/Desktop/CAT.jpg")
sp = img.shape
print("图片的大小是",sp)

sz1 = sp[0]
sz2 = sp[1]

cv2.namedWindow("img")
cv2.imshow("img",img)

myimg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("myimg",myimg)
cv2.waitKey()
cv2.destroyAllWindows()
