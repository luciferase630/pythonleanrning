"""第二章"""
print("hello")
#print是一个函数，故而需要用括号引起其中要打印的
message =" goodmorning   "
#1字母数字下划线，下划线和字母打头。2变量无空格。3不能用关键字。
#	一 variable 不用声明
"""
python 多行注释就是这么打的
1字符串 方法1 name.title()大写首字母
2方法2 .rstrip，剥除函数（这就是对象函数吧，只是叫了方法），剥除尾部空格
3字符串拼接，这应该和c++的运算符重载一样，举个例子
full_name ="what" + "how"
转义字符，\t 制表符tab， \n 换行符号
str函数将int型变量直接转化为字符串

"""
print(message.rstrip())
""" 第三章"""
#列表问题，用的是[]来表示列表，用逗号分隔。
#用print就直接连带[]一起给打印了
#索引从零开始
"""
增删改
1修改元素，就跟修改cpp数组元素一样
2bicycle.append('what')
这样就可以加入新的元素
3bicycle.insert(0,'how')
通过要插入的位置和元素，来直接进行插入，每个元素都右移一个位置
列表不止可以增添这些字符串
4使用del语句删除
del bicycles[2]
5通过pop删除
比如说，bicycles.pop()就是直接把最后一个元素给搞没了
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
七组织列表
1排序
bicycles.sort()按首字母排序
首字母反序
bicycles.sort(reverse=true)
就是相当于默认参数，和传递不同参数的函数行为不一样的情况吧。函数重载
"""

