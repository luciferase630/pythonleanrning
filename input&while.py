import pandas

import function
message=input("what do you want to enter？：")
print(message)
"""
1我都懒得说了，input里是出现的消息
2而input读入的是字符串，如果我想要读入int
int(内部必须是以有效整数表示的字符串)
这样来转换一下
3求模运算符 %
4 ps:raw_input()来提示用户输入
5while 条件
    缩进，然后执行
6可以使用标志来控制这个玩意一直循环
active =true
然后直接
while active 
怎么处理active那是别的代码块的问题
break退出循环
continue 跳过之后的循环代码块直接执行下一个代码
x += 1
无限循环的时候可以按ctrl+c 
然后可以 traceback most recent call last 最近调用堆栈
或者就直接关了
for 中不建议修改元素？
while lai xiugai yuansu ?
如果列表里多个相同元素的东西
那么用 'cat' in pets 
然后来pets.remove('cat')
remove似乎只会remove离一开始最近的那个？？
while 标志
然后输入
每次输入都处理一下
，对比一下输入是不是 某个输入，决定是否暂停输入

"""
x =1
while x <= 5:
    print(x)
    x +=1
f1(2)

#可以，这一章，非常简单