import cv2

if __name__ == "__main__":
    img = cv2.imread("C:/Users/JACK/Desktop/CAT.jpg")
    cv2.imshow("cat",img)
    cv2.waitKey()
    cv2.destroyAllWindows()
    
    
