# 数据可视化学习 | 第一部分 | matplotlib库生成数据的学习

import matplotlib.pyplot as plt
from random import choice,randint
import pygal

# 绘制折线图
from matplotlib.font_manager import FontProperties 
font_set = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=25)
#上述两句定义了中文字符格式，实现了pyplot模块正常输入中文的效果，否则中文输入会乱码
input_values=[1,2,3,4,5]
squares=[1,4,9,16,25]
plt.plot(input_values,squares,linewidth=5,color='red')
plt.title(u"完全平方数",fontproperties=font_set)
#注意上一句中"测试"中文字符前要加u使用utf-8格式，此外调用font_set实现中文格式设置
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square of Value",fontsize=14)
plt.tick_params(axis='both',labelsize=14)   #设置刻度标记大小
plt.show()

#绘制散点图
## 绘制一个点
#plt.scatter(2,4,s=200)
#绘制一系列点
##第一种方式：给出点的坐标
#x_values=[1,2,3,4,5]
#y_values=[1,4,9,16,25]
#第二种方式：自动计算坐标
x_values=list(range(1,1001))
y_values=[x**2 for x in x_values]
#plt.scatter(x_values,y_values,c=(0.5,0,0.8),edgecolor='none',s=10)    #c='red'可以直接设置颜色，也可以RGB如前所示设置，用0~1的小数设置RGB
#下面一行提供了一种设置数据的颜色映射的方法，颜色映射可以很好的根据数据密度呈现不同颜色的手段
plt.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Blues,edgecolors='none',s=40)
plt.title("Square Numbers",fontsize=24)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square of Value",fontsize=14)
#plt.tick_params(axis='both',which='major',labelsize=14)    #配合第一种方式使用的代码
plt.tick_params([0,1100,0,1100000])    #配合第二种方式使用的代码
#plt.show()
#如果要保存图表，那么可以在最后不使用show方法，而是用savefig方法
plt.savefig('squares_plot.png',bbox_inches='tight')

#练习 | 彩色立方
x_values=list(range(1,5001))
y_values=[x**3 for x in x_values]
plt.scatter(x_values,y_values,s=10,c=y_values,cmap=plt.cm.Greens,edgecolor='none')
plt.title("Colorful Cube",fontsize=24)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Cube of Value",fontsize=14)
plt.tick_params([0,5000,0,5000**3])
plt.savefig('colorful_cube.png',bbox_inches='tight')

# 随机漫步 | Randomwalk
class RandomWalk():
    '''生成一个描述随机漫步的类'''
    def __init__(self, num_points=5000):    #初始化随机漫步的属性
        self.num_points=num_points
        self.x_values=[0]
        self.y_values=[0]   #所有的随机漫步都起始于原点(0,0)
    def fill_walk(self):
        #不断漫步直到列表达到指定长度
        while len(self.x_values)<self.num_points:
            #决定前进方向以及沿着这个方向前进的距离
            x_direction=choice([1,-1])
            x_distance=choice(list(range(0,5)))
            x_step=x_direction*x_distance
            y_direction=choice([1,-1])
            y_distance=choice(list(range(0,5)))
            y_step=y_direction*y_distance
            #拒绝原地踏步
            if not x_step and not y_step:
                continue
            next_x=self.x_values[-1]+x_step
            next_y=self.y_values[-1]+y_step     #基础知识:<list>[-1]描述的是列表的最后一个元素
            self.x_values.append(next_x)
            self.y_values.append(next_y)
while True:
    rw=RandomWalk(50000)
    rw.fill_walk()
    plt.figure(figsize=(10,6),dpi=128)  #figure用于指定图表的宽度、高度、分辨率和背景色，需要为形参figsize指定一个元组，利用形参dpi向figure()传递分辨率
    point_numbers=list(range(rw.num_points))
    plt.scatter(rw.x_values,rw.y_values,s=1,c=point_numbers,cmap=plt.cm.Blues,edgecolor='none')
    #下面两行对漫步过程的起点和终点进行突出强化显示并更换颜色
    plt.scatter(0,0,s=75,c='green',edgecolor='none')
    plt.scatter(rw.x_values[-1],rw.y_values[-1],s=75,c='red',edgecolor='none')
    #将这两行放在show方法的上面是因为紧连着show才能最后被绘制，如果在绘制其他点的scatter方法前对起点和终点进行绘制，那么起点和终点将会落在漫步过程的散点图的下方，影响视觉效果
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)   #这两行隐藏了横纵坐标轴
    plt.show()
    if input("Make another walk? (y/n):")=='n':
        break
#上面是循环生成随机漫步过程图

# 练习 | 重构的RandomWalk类
class RandomWalk():
    '''生成一个描述随机漫步的类'''
    def __init__(self, num_points=5000):    #初始化随机漫步的属性
        self.num_points=num_points
        self.x_values=[0]
        self.y_values=[0]   #所有的随机漫步都起始于原点(0,0)
    def get_step(self):
            return choice([1,-1])*choice(list(range(0,5)))
    def fill_walk(self):
        #不断漫步直到列表达到指定长度
        while len(self.x_values)<self.num_points:
            #决定前进方向以及沿着这个方向前进的距离
            x_step=self.get_step()
            y_step=self.get_step()
            #拒绝原地踏步
            if not x_step and not y_step:
                continue
            next_x=self.x_values[-1]+x_step
            next_y=self.y_values[-1]+y_step     #基础知识:<list>[-1]描述的是列表的最后一个元素
            self.x_values.append(next_x)
            self.y_values.append(next_y)

#练习 | 分子运动路线模拟(需要用到RandomWalk类的头文件)
while True:
    rw=RandomWalk()
    rw.fill_walk()
    plt.figure(figsize=(10,6),dpi=128)  #figure用于指定图表的宽度、高度、分辨率和背景色，需要为形参figsize指定一个元组，利用形参dpi向figure()传递分辨率
    point_numbers=list(range(rw.num_points))
    plt.plot(rw.x_values,rw.y_values,linewidth=1,c='blue')
    #下面两行对漫步过程的起点和终点进行突出强化显示并更换颜色
    plt.scatter(0,0,s=75,c='green',edgecolor='none')
    plt.scatter(rw.x_values[-1],rw.y_values[-1],s=75,c='red',edgecolor='none')
    #将这两行放在show方法的上面是因为紧连着show才能最后被绘制，如果在绘制其他点的scatter方法前对起点和终点进行绘制，那么起点和终点将会落在漫步过程的散点图的下方，影响视觉效果
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)   #这两行隐藏了横纵坐标轴
    plt.show()
    if input("Make another walk? (y/n):")=='n':
        break
#上面是循环生成随机漫步过程图

# Pygal模拟掷骰子
# Pygal生成的可缩放矢量图形文件可以在尺寸不同的屏幕上自适应的缩放，对于在线使用的图表，优先考虑用Pygal生成
class Die():
    '''表示一个骰子的类'''
    def __init__(self,num_sides=6):
        self.num_sides=num_sides
    def roll(self):
        return randint(1,self.num_sides)    #返回一个位于1和骰子面数之间的随机值
die_1=Die()
die_2=Die()
#results=[]
#for roll_num in range(1000):
#    result=die_1.roll()+die_2.roll()
#    results.append(result)         #上面这几行被注释的部分都可以通过列表解析来实现，列表解析后的代码如下
results=[die_1.roll()*die_2.roll() for roll_num in range(50000)]
max_result=die_1.num_sides*die_2.num_sides
#frequencies=[]
#for value in range(2,max_result+1):
#    frequency=results.count(value)
#    frequencies.append(frequency)      #上面这几行被注释的部分都可以通过列表解析来实现，列表解析后的代码如下
frequencies=[results.count(value) for value in range(1,max_result+1)]
hist=pygal.Bar()
hist.title="Results of rolling dice"
#hist.x_labels=list(range(2,max_result+1))      #对这一行进行列表解析如下一行所示
hist.x_labels=[i for i in range(1,max_result+1)]
hist.x_title="Result"
hist.y_title="Frequency of Result"
hist.add('RollingDice',frequencies)
hist.render_to_file('RollingDice.svg')
print("The program has successfully processed the processing result.")
print("frequencies:",frequencies)
#print("results:",results)
