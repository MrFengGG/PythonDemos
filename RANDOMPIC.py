import numpy
import cv2


hang = 200
lie = 300
img = numpy.zeros((hang,lie,3),numpy.uint8)
pos1 = numpy.random.randint(200,size=(2000,1))
pos2 = numpy.random.randint(300,size=(2000,1))


for i in range(2000):
    img[pos1[i],pos2[i],[0]]=numpy.random.randint(0,255)
    img[pos1[i],pos2[i],[0]]=numpy.random.randint(0,255)
    img[pos1[i],pos2[i],[0]]=numpy.random.randint(0,255)

cv2.imshow("random",img)
cv2.waitKey()
cv2.destroyAllWindows()
