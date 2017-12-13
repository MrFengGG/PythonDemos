import cv2
import numpy
import matplotlib
from matplotlib import pyplot

def show(blur_Func=None,blurSize=(5,5)):
    capture = cv2.VideoCapture(0)
    while True:
        ret,frame = capture.read()
        if ret ==True:
            low = nothing();
            #frame = cv2.Canny(frame,low,200)
            frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            frame = face_get(frame)
            if blur_Func:
                frame = blur_Func(frame,blurSize)
            '''
            pyplot.subplot(121)
            pyplot.imshow(img)
            pyplot.title("yuan tu")
            pyplot.subplot(122)
            pyplot.imshow(blur)
            pyplot.title("junhenghua")
            pyplot.show()
            '''
            cv2.imshow("frame",frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break
    capture.release()
    cv2.destroyAllWindows()
def face_get(src):
    face_cascade = cv2.CascadeClassifier('C:/Users/JACK/Desktop/data/haarcascades/haarcascade_righteye_2splits.xml')
    faces = face_cascade.detectMultiScale(
    src,
    scaleFactor=1.2,
    minNeighbors=1,
    minSize=(32, 32)
    )
    for(x,y,w,h) in faces:
        cv2.rectangle(src,(x,y),(x+w,y+w),(0,255,0),2)
        #cv2.circle(src,(int((x+x+w)/2),int((y+y+h)/2),int(w/2),(0,255,0),2))
    return src
    
def a(x):
    pass
def nothing():
    
    low = cv2.getTrackbarPos("low","image")
    return low
    
def blur_Blur(image,Size):
    return cv2.blur(image,Size)

def gaus_Blur(image,Size):
    try:
        return cv2.GaussianBlur(image,Size,0)

    except:
        print("error,Size shoud be odd")
        return image
    
def meidan_Bulr(image,Size):
    if isinstance(Size,tuple):
        Size = Size[0]
    if Size%2==0:
        Size+=1
    return cv2.medianBlur(image,Size)

if __name__=="__main__":
    show()
