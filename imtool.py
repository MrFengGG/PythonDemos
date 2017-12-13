from PIL import Image
from pylab import *
import numpy

FILE_PATH = "C:/Users/JACK/Desktop/"

def imresize(im,sz):
    '''使用PIL对象重新定义图像数组的大小'''
    pil_im = Image.fromarray(numpy.uint8(im))
    return numpy.array(pil_im.resize(sz))

def histeq(im,nbr_bins=256):
    '''对一幅图像进行直方图均衡化'''

    #计算图像的直方图
    imhist,bins = histogram(im.flatten(),nbr_bins,normed=True)
    cdf = imhist.cumsum()
    cdf = 255 * cdf / cdf[-1]

    #使用累积分布函数的线性插值,计算新的像素值
    im2 = interp(im.flatten(),bins[:-1],cdf)
    return im2.reshape(im.shape),cdf

def compute_average(imlist):
    '''计算图像列表的平均图像'''

    #打开第一幅图像,将其存储在浮点型数组中
    averageim = array(Image.open(imlist[0]),"f")

    for imname in imlist[1:]:
        try:
            averageim += array(Image.open(imname))
        except:
            print(imname+"...跳过")
    averageim /= len(imlist)

    return array(averageim,"uint8")

if __name__ == "__main__":
    img = array(Image.open("C:/Users/JACK/Desktop/test2.jpg").convert("L"))
    img2,cdf = histeq(img)
    figure()
    imshow(img2)
    figure()
    imshow(img)
    figure()
    hist(img.flatten(),128)
    figure()
    hist(img2.flatten(),128)
    show()
