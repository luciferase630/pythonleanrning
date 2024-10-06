"""第二章"""
print("hello")
#print是一个函数，故而需要用括号引起其中要打印的
message =" goodmorning   "
#1字母数字下划线，下划线和字母打头。2变量无空格。3不能用关键字。
#	一 variable 不用声明
"""
python 多行注释就是这么打的
单引号 (') 或双引号 (") 来引用，两者在功能上是等价的。
1字符串 方法1 name.title()大写首字母
2方法2 .rstrip，剥除函数（这就是对象函数吧，只是叫了方法），剥除尾部空格
3字符串拼接，这应该和c++的运算符重载一样，举个例子
full_name ="what" + "how"
转义字符，\t 制表符tab， \n 换行符号
str函数将int型变量直接转化为字符串

"""
print(message.rstrip())
""" 第三章"""
#它是list类底下的一个对象
#列表问题，用的是[]来表示列表，用逗号分隔。
#用print就直接连带[]一起给打印了
#索引从零开始
#列表可以包含不同类型的值my_list = [1, "hello", 3.14, True, [5, 6, 7]]
"""
他们存储的是对象的引用而不是本身，是不是说它存储的是一堆堆指针，
然后指针的内存占用都是int一样大，但是实际上这些列表元素对象都是分散存储的
增删改
1修改元素，就跟修改cpp数组元素一样
2bicycle.append('what')
这样就可以加入新的元素
3bicycle.insert(0,'how')
通过要插入的位置和元素，来直接进行插入，每个元素都右移一个位置
列表不止可以增添这些字符串
4使用del语句删除
del bicycles[2] 删除第一个元素
5通过pop删除
比如说，bicycles.pop()就是直接把最后一个元素给删除
bicycles.pop(索引值)可以删除任意位置的元素
可以只pop不使用其返回值
还可以赋值给其他的
6通过remove 删除同样，这也是一个方法
bicycles.remove('how')
"""
bicycles = ['trek', 'cannondale','redline']
print(bicycles)
bicycles.append('what')
bicycles.insert(0, 'how')
del bicycles[2]
print(bicycles)
"""
3.3组织列表
1排序
bicycles.sort()按首字母排序
首字母反序
bicycles.sort(reverse=true)
就是相当于默认参数，和传递不同参数的函数行为不一样的情况吧。函数重载
#sorted排序是临时的，调用完就没了
#返回新列表: sorted() 返回的是一个新的列表，而不是在原地修改原始列表。这意味着原始列表保持不变。
没想到这单行和多行还能嵌套？？
cars.reverse，直接反转内部排序
len(cars)直接返回其长度
2避免使用错误的索引，它会检查，报error
3列表的.-1将会直接返回末尾的元素
当列表为空的时候
motorcycles=[]就会-1返回错误，motorcycles[-1]


"""



"""
4.1操作列表
（我估计要开始讲循环了）
magicians=["alice","david","john"]
for magician in magicians:
    print(magician)
    print（magician.title+",wow")
举个例子，他就是这样的
1用magician获取第一个magicians里的元素，记得冒号不要省略
2而for执行哪一行
不是用花括号而是用缩进
expected an indented block 
Unexpected indent
3缩进代表下一行属于上一行
4range直接创造数字列表
numbers=list(range(1,6))
表示从1开始数到6，但是range还有各种重载形式
range(2,11,2)
会输出2  4 6 8 10 小于等于11
value**2代表着乘方运算
wtf，python甚至不用说类型，直接用，类型是动态分配的
"""
magicians=["alice","david","john"]
for magician in magicians:
    print(magician)
squares=[value**2 for value in range(1,11)]
print(squares)






