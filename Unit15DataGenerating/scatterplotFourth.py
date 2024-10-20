import matplotlib.pyplot as plt


plt.title("Squares Numbers",fontsize=24)
plt.xlabel("Value",fontsize=12)
plt.ylabel("Squares of Value",fontsize=12)
xvalues=list(range(1,1001))
yvalues=[x**2 for x in xvalues]
plt.scatter(xvalues,yvalues,s=40,edgecolors='none',c=yvalues,cmap=plt.cm.Blues)
plt.axis([0,1100,0,1100000])#这咋是这样写出的???
#[xmin, xmax, ymin, ymax]
plt.show()
#plt.scatter(xvalues,yvalues,s=40,edgecolors='none',c=(0,1,0.8))这是非常经典的c用元组来定义rgb，也可以c='red'
#c=yvalues这样可以搞颜色映射
#我可以告诉它用哪一组颜色映射
#具体颜色映射 matplotlib.org  单击example，向下滚动到colorexample，然后colormaps_reference


#设置刻度标记的大小