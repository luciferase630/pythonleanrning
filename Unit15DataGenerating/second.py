import matplotlib.pyplot as plt


"""
单例 plt 对象
plt 并不是传统意义上的对象实例，而是一个模块，它的工作方式类似于一个全局状态机。
当你使用 plt 来创建图表或调用绘图函数时，你是在操作一个全局的图形环境。
这意味着在大多数情况下，你使用的 plt 实际上是单一的，操作的是同一组全局状态和配置。

绘制多个图形
尽管 plt 像是单一的，但你确实可以在同一个 Python 程序中创建多个图形。
有几种方法可以做到这一点：

使用 plt.figure()
最简单的方法是使用 plt.figure() 创建新的图形。每次调用 plt.figure() 时，
matplotlib 都会创建一个新的图形窗口，你可以在每个窗口中绘制不同的数据和图表。

使用子图 plt.subplot()
如果你想在一个窗口内创建多个图表，可以使用 plt.subplot()：
subplot 的基本语法是：

python
复制代码
plt.subplot(nrows, ncols, index)
nrows 和 ncols 参数指定将图形窗口划分为多少行和列。
index 参数指定当前激活的是哪一个子图，索引从1开始到 nrows * ncols。

# 第一个子图
plt.subplot(2, 2, 1)  # 2行2列的第1个位置
plt.plot([1, 2, 3, 4, 5], [1, 4, 9, 16, 25])
plt.title('Plot 1')


类型注解的语法是在变量名后面加冒号（:），然后跟上类型。例如，x: int 表示 x 应该是一个整数
"""
plt.figure()
squares=[1,4,9,16,25]
plt.plot(squares,linewidth=5)
plt.title("Square Numbers",fontsize =24)
plt.xlabel("Value",fontsize=12)
plt.ylabel("Square of value",fontsize=12)

#设置刻度标记的大小，这个axis还能传什么值？
plt.tick_params(axis='both',labelsize=14)
plt.show()
#新建一个子图之后之前这些设置就都不顶用了
#奇怪，那这个plot内怎么啥都能传呢
plt.figure()
input_values=['a','b','c','d','e']
plt.plot(input_values,squares,linewidth=2)#先x后y,如果没写则自动从0开始，然后依次递增，01234这种
plt.show()

