"""
这也是文档字符串？
"""
import module

def greet_user(username):
    print('hello'+username.title()+'!')


greet_user('NAME')
"""
第八章，函数
"""
"""

 函数
一：传入参数
可以有类型注解，但也仅仅只是注解
 def greet_user(username)
    print('hello'+username.title()+'!')
蛙趣，传入参数都不给类型的，这就纯粹逆天
然后突然跳个报错，int object has no attribute 'title'
在函数定义的时候里面的值和引用都是形参， 而函数调用用的都是实参
就是说形参就是个占位符而已
1实参必须按照顺序关联形参
2可以使用关键字实参来传递
greet_user(username='a')
这样的

2default值
比如def greet_user(username='a'),必须放在非默认形参之后
这就相当于在def阶段就有赋值，如果在运行期间没有参数传递
greet_user()就直接调用了实参
所以有很多种等效的函数调用，完全可以乱调用，比如有default值，那我就可以只传一个参，用位置模式

3传入一个列表，可以在函数中修改列表
如果说不想让函数修改列表，那么就要这样传入副本 designs[:]

4传递任意数量的实参 
它会自动被封装到一个元组里
print(i, end='')  可以让它就完全不用

二：返回值
1就不用说了，直接在里面写变量然后把那个变量返回了就行
2让实参变成可选的这就没什么好说的了
3返回一个字典
(while True:)
三：其他模块函数的调用
from module import f1
直接可以调用f1
这样好像是本地会覆盖其他模块的问题,应该是本地优先的
还可以指定别名
from pizza import make_pizza as mp，这种估计也是本地优先
import module as p  也算是指定别名了
而import module，则需要module.f1(2)
同时可以这样 
from pizza import *

eeee额呃呃呃pep8的风格我是真没学明白啊
"""
def getformatname(firstname,lastname,middlename=''):
    if middlename:
        print(firstname+' '+middlename+' '+lastname)
    else:
        print(firstname+' '+lastname)
getformatname('wdf','bro','shit')
def makepizza(*toppings:str):
    print(toppings)
makepizza('1',2,4.5,"梦雅")


def f1(a:int):
    """
    这就是文档字符串啊
    :param a:就是传入的a值啊
    :return:无奈了
    """
    print(f'int{a}')
f1(2)


"""
字典：当你使用 {} 来定义一个字典时，它们确实表示一个键值对集合。
例如，my_dict = {'key': 'value'}。
集合：当你使用 {} 来定义一个集合时，它们表示一个无序的唯一元素集合。
例如，my_set = {1, 2, 3}。
格式化字符串（f-string）：在 f-string 中，花括号 {} 
用于嵌入表达式的值。它们不是字典，而是用于将变量或表达式的值插入到字符串中。
例如，f'Value is {a}' 会将变量 a 的值插入到字符串中。
"""

"""
：这个视频解释了在Python中为什么要使用if __name__ == '__main__'这行代码。
它的作用是判断当前脚本是被直接执行还是作为模块被导入，以避免测试代码被重复执行。通过判断Name变量的取值，
可以确定当前的执行情况。这样可以确保测试代码只在直接执行脚本时被执行，而在导入为模块时不被执行。
"""