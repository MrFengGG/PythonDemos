from PIL import Image
from pylab import *

#读取图片
img = array(Image.open("C:/Users/JACK/Desktop/CAT.jpg"))

#显示图片
imshow(img)

#点
x = [100,100,400,400]
y = [200,500,200,500]

#用*来绘制这些点
plot(x,y,"r*")

#将图片链接起来
plot(x[:2],y[:2])

#添加标题
title('Plotting:"jpg"')
show()
