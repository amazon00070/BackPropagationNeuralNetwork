#20200318python
#20200323matrix(numpy)
#20200325BPNN
#20200326class
import math
import numpy
import random
class bpnn:
    'This is a class for a BPNN'
    def __init__(self,n_1,n_2,n_3):
        self.n_1 = n_1
        self.n_2 = n_2
        self.n_3 = n_3
        self.__init_matrix()
    def __sigmoid_array(self,x):
        a = []
        for i in range(0,len(x)):
            a.append([1 / (1 + math.exp(-x[i]))])
        return numpy.array(a)
    def __init_random(self,x,y):
        mid = numpy.zeros((x,y))
        for i in range(0,x):
            for j in range(0,y):
                mid[i][j] = random.uniform(-1,1)
        return mid
    def __init_matrix(self):
        self.x_1 = numpy.zeros((self.n_1 + 1,1))
        self.x_2 = numpy.zeros((self.n_2 + 1,1))
        self.x_3 = numpy.zeros((self.n_3,1))
        self.x_1[self.n_1] = 1
        self.x_2[self.n_2] = 1
        self.w_1_2 = self.__init_random(self.n_2,self.n_1 + 1)
        self.w_2_3 = self.__init_random(self.n_3,self.n_2 + 1)
    def __forward(self,x_1):
        self.x_1[0:self.n_1] = x_1
        self.o_2 = numpy.dot(self.w_1_2,self.x_1)
        self.x_2[0:self.n_2] = self.__sigmoid_array(self.o_2)
        self.o_3 = numpy.dot(self.w_2_3,self.x_2)
        self.x_3 = self.__sigmoid_array(self.o_3)
    def __backward(self,xite):
        self.e_x3_o3 = self.x_3 - (self.x_3 ** 2)
        self.e_x3 = self.e_x3_o3 * self.e_total_x3
        self.e_x2_o2 = self.x_2 - (self.x_2 ** 2)
        self.e_x2 = self.e_x2_o2 * numpy.dot(self.w_2_3.T,self.e_x3)    
        self.w_2_3 = self.w_2_3 - numpy.dot((xite * self.e_x3),(self.x_2.T))
        self.w_1_2 = self.w_1_2 - numpy.dot((xite * self.e_x2[0:self.n_2]),(self.x_1.T))
    def run(self,x_1,aim,xite):
        self.__forward(x_1)
        self.e_total_x3 = self.x_3[0:self.n_3] - aim
        self.__backward(xite)
#下方为用例

#此部分用于图表显示的存储
x = []
nn1_y1 = []
nn1_y2 = []
nn1_y3 = []
nn2_y1 = []
nn2_y2 = []
nn2_y3 = []
nn2_y4 = []

#用例（共2个）
nn1 = bpnn(3,8,3)# <----------------一个bpnn实例，3输入、8隐层、3输出
nn2 = bpnn(3,10,4)
for i in range(0,100000):# <----------------训练100000次（实际应用时建议通过实时训练度判定来决定训练边界）
    nn1.run([[0.1],[0.6],[0.3]],[[0.7],[0.8],[0.9]],0.01)# <----------------括号内三个参数，(输入向量,输出,学习速率)
    nn2.run([[0.7],[0.8],[0.9]],[[0.1],[0.2],[0.3],[0.4]],0.01)
    
    #数据记录
    x.append(i)
    nn1_y1.append(nn1.x_3[0])
    nn1_y2.append(nn1.x_3[1])
    nn1_y3.append(nn1.x_3[2])
    nn2_y1.append(nn2.x_3[0])
    nn2_y2.append(nn2.x_3[1])
    nn2_y3.append(nn2.x_3[2])
    nn2_y4.append(nn2.x_3[3])

#显示输出结果
print(nn1.x_3)
print(nn2.x_3)

#打印图表
import matplotlib.pyplot as plt
plt.plot(x, nn1_y1)
plt.plot(x, nn1_y2)
plt.plot(x, nn1_y3)
plt.plot(x, nn2_y1)
plt.plot(x, nn2_y2)
plt.plot(x, nn2_y3)
plt.plot(x, nn2_y4)
plt.show()
