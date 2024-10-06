
players=['charles','marijuana','michael','florence']
print(players[0:3])
"""
4.4切片，就是使用列表的一部分

start stop step 
range(1,13,2)
也是经典 开始结束步长，这种方法的实现是用魔术方法实现的
如果是
players[:3] 则自动从头开始
同理players[2:]
遍历则和c没什么区别
for player in players[:3]这样的
for (int number : numbers)这是c++和java的foreach用法
列表是可以相互赋值的，就直接用等号就好
playerest=players[]

print(playerest)
也可以就是切片赋值
4.5 元组
不可修改的元组
dimensions=(200,50)
是用圆括号引起
虽然不能dimensions[0]=2
这样赋值，但是可以直接把这个元组重新赋值
dimensions=(200,100)
就是这样，相当于只是记录最后一次的变量赋值

最后，代码编写格式，首先建议用每级缩进用四个空格
行长建议小于等于72个
缩进在file->settings->code style-> python
空行可以将程序隔开，但是别滥用。举例：三行创建列表，五行处理列表
"""
playerest=players
print(playerest)
"""
5if
选择语句
for player in playerest:
    if player == 'michael':
        print(player.upper)
    else:
        print(player.title())
这里的函数有问题，没传参就调用了，居然还不会中止，添加括号获取其返回值
当你在 Python 中查询一个方法但没有调用它时（没有在方法名后加上 ()），
Python 会返回一个表示该方法的函数对象，而不是其执行结果。这个对象的表示形式就像你看到的那样：
"""
for player in playerest:
    if player == 'michael':
        print(player.upper)
    else:
        print(player.title())

