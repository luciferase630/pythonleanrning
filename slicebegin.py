
players = [' charles '  , ' marijuana '   , 'michael'  , 'florence']
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
不是吧
且或非
age >= 21 and age >= 21 这个是且
age >= 21 or age >= 21 这个是或

检查特定值是否包含在列表中
 用in关键字
 元素  in   列表 
 这个expression就是可以判断真假的
 if 'mushrooms' in requested_players:
    print("not found")
elif  'michael' in requested_players:
    print('found')
else:
    print("fine,ok")
    这三行代码让我深入理解python里的选择结构
else 是可以省略的
通过测试后，会直接跳过余下的测试
所以if if if也在别的情况下非常好用
if 列表名
如果列表为空则返回false 如果列表不为空则返回true
 
"""
for player in playerest:
    if player == 'michael':
        print(player.upper)
    else:
        print(player.title())
requested_players=players
print('mushrooms' in requested_players)
print('michael' in requested_players)
if 'mushrooms' in requested_players:
    print("not found")
elif  'michael' in requested_players:
    print('found')
else:
    print("fine,ok")
"""
6字典
用花括号引起
alien={'color': red , ' points ':5}
前面是key  后面是value 就是可以用key作为索引，来索引后面的值//具体实现未可知

可以增添
alien['x_position']= 9
这样就可以在末尾添加了
而如果改变的先前的键值对，那么就是赋值
同理del alien[key]
alien.pop(paragmeter)必须要有参数啊 eg:print(alien.pop('color'))
一遍历键值对
for key,value in alien.items():
    print('\nKey:'+key)
    print('Value',value)
这是循环遍历方式，非常的好用，key 和value一起遍历
二遍历键
而for name in alien.keys():
     print(name)就是直接遍历key，也可以省略掉.keys()因为实际上可以省略，增加代码可读性
     sorted(alien.keys())临时排序的情况
三遍历值
for value in alien.values()就很合理返回一个值的列表然后直接进行遍历

列表和字典的嵌套
列表的每一个元素都可以是一个字典
aliens[]
然后一直append（这个元素）
str(len(aliens))经典，因为要+

反过来，字典中存储列表
也就是说，把values值的类型设置为列表了，比如说
pizza={
 'crust':'thick'
 'toppings':['mushroooms','extra cheese'
 }
 一般来说不需要缩进，但是还是建议缩进，一个级别，规定一般是一个级别为四个
而逗号后面一般要留一个空，但前面不留

最后，字典套字典
users={
    'aeinstein':{
        'first': 'albert'
        },
    下一个字典
}
    

"""
alien={'color': 'red', ' points ':5}
print(alien['color'])
for key,value in alien.items():
    print('\nKey:'+key)
    print('Value',value)
print(alien.pop('color'))
#这里删除了color
for name in alien.keys():
     print(name)
pizza={
    'crust': 'thick',
    'toppings': ['mushroooms', 'extra cheese']
 }

