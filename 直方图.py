from PIL import Image
from pylab import*
import numpy

filename="C:/Users/JACK/Desktop/test.jpg"
im = Image.open(filename)
img =im.convert("L")
array = numpy.array(im)
array2 = numpy.array(img)
figure()

#gray()
#imshow(img)

print(array[1])
print(array2[1,1])

figure()
hist(array2.flatten(),128)
#show()
