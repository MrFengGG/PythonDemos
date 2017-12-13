import cv2
import numpy

def strokeEdges(src,dst,blurKsize=7,edgeKsize=5):
    if blurKsize >=3:
        blurredSrc = cv2.medianBlur(src,blurKsize)
        graySrc = cv2.cvtColor(blurredSrc,cv2.COLOR_BGR2GRAY)
    else:
        graySrc = cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)
    graySrc = cv2.Laplacian(graySrc,cv2.CV_8U,graySrc)
    normalizedInverseAlpha = (1.0/255)*(255-graySrc)
    channels = cv2.split(graySrc)

    for channel in channels:
        channel[:] = channel*normalizedInverseAlpha

    cv2.merge(channels,dst)
    cv2.imshow("img",dst)
if __name__=="__main__":
    img = cv2.imread("C:/Users/JACK/Desktop/1.jpg")
    img = strokeEdges(img)
    cv2.imshow("img",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()