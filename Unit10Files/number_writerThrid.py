import json

from Unit10Files.Filefirst import file_name#
#导入特定的变量？？？不止是函数from  xxx import  xxx  我估计还可以导入类吧
#导入这个东西，我不知道这是个啥。
#这模块json能让你把简单的python数据结构（问题1，什么是简单是python数据结构）存储到文件中，并在程序再次运行时加载该文件的数据。小型数据库？
"""
json格式存储数据
JavaScript Object Notation 最初为JavaScript开发的，但是后面成为了常见格式

"""

numbers = [2,3,5,7,9,11,13]
file1='numbers.json'
with open(file1,'w') as f1:
    json.dump(numbers,f1)

#

"""
SupportsWrite[str]：这个类型一般指一个支持写入 str 数据的方法
（比如 write()）的对象。通常这个接口的对象需要实现 write(str) 方法。
TextIO：这是 Python 的 io 模块中的一种类型，表示一个文本文件对象。
TextIO 通常具有 write() 方法，但是在某些类型检查工具中，
它并不严格被认为符合 SupportsWrite[str] 的要求。就是指支持write（str）接口的对象



json.dump() 是一种更高层的写入方法，与 write() 方法不同。json.dump() 
会自动将 Python 数据结构（如列表、字典）转换成 JSON 格式并写入文件，
而你无需直接调用 write() 方法。


"""