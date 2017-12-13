import cv2
import numpy
from scipy import ndimage

kernel_3x3 = numpy.array(
    [[-1,-1,-1],
     [-1,8,-1],
     [-1,-1,-1]]
)
kernem_5x5 = numpy.array(
    [[-1,-1,-1,-1,-1],
     [-1,1,2,1,-1],
     [-1,2,4,2,-1],
     [-1,1,2,1,-1],
     [-1,-1,-1,-1,-1]]
)

img = cv2.imread("C:/Users/JACK/Desktop/1.jpg",0)
cv2.imshow("img",img)
k3 = ndimage.convolve(img,kernel_3x3)
k5 = ndimage.convolve(img,kernem_5x5)

blurred = cv2.GaussianBlur(img,(11,11),0)
g_hpf = img-blurred
cv2.imshow("3x3",k3)
cv2.imshow("5x5",k5)
cv2.imshow("g_hpf",g_hpf)
cv2.waitKey()
cv2.destroyAllWindows()