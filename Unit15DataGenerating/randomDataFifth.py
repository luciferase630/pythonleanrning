from random import choice

import matplotlib.pyplot as plt

"""
通过一个随机漫步类让我对随机数有一个理解
然后消除坐标轴


"""


class RandomWalk():
    """ 随机漫步数据的类"""

#将生成5000个点
    def __init__(self,num_points=5000):
        """初始化"""
        self.num_points=num_points
        self.x_values=[0]
        self.y_values=[0]
    def fill_walk(self):
        """计算随机漫步包含的点"""
        while len(self.x_values) < self.num_points: #4999次循环,5000个点。一开始是1，小于5000，在4999时可以执行，执行之后一共有
            # """Choose a random element from a non-empty sequence."""
            x_direction=choice([1,-1])
            x_distance=choice([0,1,2,3,4])
            x_step=x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            if x_step==0 and y_step==0:
                continue
            next_x =self.x_values[-1] +x_step
            next_y =self.y_values[-1] +y_step#负数就是倒着数的值

            self.x_values.append(next_x)
            self.y_values.append(next_y)
"""
实际上，`range` 并不是列表的子类。它们是两种完全不同的数据类型，
尽管它们都可以用于表示和操作一系列整数。
`range` 类型是一个不可变的序列类型，它专门用来表示一个整数序列。
这种类型是高效的，因为它不会像列表那样实际存储每个数字，
而是按需计算每个值，这样可以节省内存空间。`range` 对象定义了开始、结束和步长，
只有当你尝试访问序列中的值时，这些值才被计算出来。
列表（`list`）是一种更通用的数据结构，用于存储一个有序的元素集合，
这些元素可以是任何类型，并且可以随时添加、删除或更改。列表是动态数组，
支持快速的随机访问和高效的尾部添加和弹出操作。
由于 `range` 和列表在功能和存储机制上的区别，它们不共享继承关系。
你可以通过将 `range` 对象转换为列表来获取一个真正的列表，以便进行更复杂的操作，但它们本质上是独立的类型。要查看任何对象或变量的类型，你可以使用 Python 的 `type()` 函数。例如：

```python
print(type(range(5)))  # <class 'range'>
print(type([1, 2, 3, 4, 5]))  # <class 'list'>
```

这些输出显示了 `range` 和列表是不同的类。

"""
while True:
    rw=RandomWalk(50000)
    rw.fill_walk()
    ##再加点料，让那个
    point_numbers=list(range(rw.num_points))
    ####再把坐标轴隐藏了
    """
    这个隐藏坐标轴必须得，先得创建实例，且得放在scatter前面。
    放在scatter前，没有创建实例，则直接没有作用
    放在scatter后，创建实例则坐标轴干净。不创建，则坐标轴的数字发生重叠
     current_axes = plt.axes()
    current_axes.get_xaxis().set_visible(False)
    current_axes.get_yaxis().set_visible(False)
    
    这是书上的——》plt.axes().get_xaxis().set_visible(False)
                plt.axes().get_yaxis().set_visible(False)
                gpt建议直接创建子图
         .完全是史，不好用
                
    """
    current_axes = plt.axes()
    current_axes.get_xaxis().set_visible(False)
    current_axes.get_yaxis().set_visible(False)

    plt.show()


   #方法串接，这很常见
    ###突出起点和终点
    plt.scatter(0,0,c='Blue',edgecolors='none',s=100)#这里颜色的blue什么的好像无所谓

    plt.scatter(rw.x_values,rw.y_values,s=5,c=point_numbers,
                cmap=plt.cm.Reds,edgecolors='none')


    plt.show()

    keep_running=input("do you want continue or not?(yes/no)")
    if keep_running=='yes':
        break


