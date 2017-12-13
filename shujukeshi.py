import sys
sys.path.append("F:\学习\python项目")
from matplotlib import pyplot
import data_utils
import numpy


def draw_pic(data):
    x = [i for i in range(len(data))]
    y = data
    pyplot.scatter(x,y,1,"red")
    pyplot.show()

if __name__ == "__main__":
    data = data_utils.get_data("F:/工作/正常.txt")
    data = data_utils.change_bad_data(data)
    draw_pic(data)
