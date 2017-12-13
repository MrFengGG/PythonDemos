from PIL import Image
from pylab import *
#打开图片
img = array(Image.open("C:/Users/JACK/Desktop/1.jpg").convert("L"))
#创建一副新的图片
figure()
#不使用颜色信息
gray()
#在原点左上角显示轮廓图像
contour(img,origin="image")
axis("equal")
axis("off")
#创建另一个图片
figure()
#绘制直方图,hist只接受一维数组,所以需要使用flatten将图像压平
hist(img.flatten(),128)
show()
