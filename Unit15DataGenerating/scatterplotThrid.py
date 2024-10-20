import matplotlib.pyplot as plt


#发现清除缓存可以影响生成图
plt.subplot(2, 2, 1)  # 2行2列的第1个位置
plt.plot([1, 2, 3, 4, 5], [1, 4, 9, 16, 25])
plt.title('Plot 1')

plt.subplot(2, 2, 2)
plt.scatter(2,4)


#设置刻度标记大小，这个我一直没理解到
"""

1. axis='both'
这个参数指定要修改的轴。axis='both' 意味着更改将应用于 x 轴和 y 轴上的刻度线。其他可能的选项包括：

'x': 仅应用更改到 x 轴的刻度线。
'y': 仅应用更改到 y 轴的刻度线。
2. which='major'
这个参数定义了将更改应用于哪种类型的刻度线。在 Matplotlib 中，每个轴通常有主要刻度线（major ticks）和次要刻度线（minor ticks）。which='major' 指定更改仅应用于主要刻度线。其他可能的选项包括：

'minor': 应用更改到次要刻度线。
'both': 同时应用更改到主要刻度线和次要刻度线。
3. labelsize=14
这个参数设置刻度标签的字体大小为 14。刻度标签是轴旁边显示的数字或文字，表示刻度的值。通过设置 labelsize，你可以控制这些标签的可读性，使图表更易于理解。

总结来说，这行代码的作用是同时对图表的 x 轴和 y 轴的主要刻度线标签应用字体大小为 14 的设置。这样的调整可以帮助改善图表的视觉效果，使得刻度标签更加清晰和易于阅读，特别是在进行演示或将图表用于出版物时。

"""
plt.subplot(2, 2, 3)
plt.tick_params(axis='both',which='major',labelsize=14)

#同样可以绘制一系列点
x_values=[1,2,3,4,5]
y_values=[1,4,9,16,25]

plt.scatter(x_values,y_values)

plt.subplot(2,2,4)
plt.title("Squares Numbers",fontsize=24)
plt.xlabel("Value",fontsize=12)
plt.ylabel("Squares of Value",fontsize=12)
xvalues=list(range(1,1001))
yvalues=[x**2 for x in xvalues]
plt.scatter(xvalues,yvalues,s=40,edgecolors='none',c=yvalues,cmap=plt.cm.Blues)
plt.show()
