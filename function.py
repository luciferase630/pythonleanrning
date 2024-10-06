
def greet_user(username):
    print('hello'+username.title()+'!')
greet_user(1)
"""

 函数
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
比如def greet_user(username='a')
这就相当于在def阶段就有赋值，如果在运行期间没有参数传递
greet_user()就直接调用了实参

"""

