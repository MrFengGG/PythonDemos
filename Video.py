import numpy
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret,frame = cap.read()
    cv2.putText(frame,"FENGZIYU",(10,500),cv2.FONT_HERSHEY_SIMPLEX,4,(255,255,255),2)
    cv2.imshow("frame",frame)
    if cv2.waitKey(1)&0xFF == ord("q"):
        break;
cap.release()
cv2.destroyAllWindows()
                                   

                
