from PIL import Image
from pylab import *

img = array(Image.open("C:/Users/JACK/Desktop/1.jpg"))
imshow(img)
img2 = 255 - img
img3 = (100.0/255)*img+100
img4 = 255.0*(img/255.0)**2

subplot(221)
imshow(img)

subplot(222)
imshow(img2)

subplot(223)
imshow(img3)

subplot(224)
imshow(img4)

show()
