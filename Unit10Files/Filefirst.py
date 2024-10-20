"""
尝试搞一个文件
这里的with，as我后面都会讲。
with就是让python来控制什么时候打开什么时候关闭。函数open（），接受一个参数，要打开的文件名称，一般来说是相对地址
但是绝对地址我还没试过，我试一下.
不能直接使用windows里的路径，因为win是反斜杠。反斜杠在python里是转义。所以一定要正斜杠

如果文件不存在，会弹出fileNotFoundException
"""

with open('pi_digits.txt') as file_object :
    contents = file_object.read()
    print(contents)
with open('G:/ppjforall/remote/pythonleanrning/Unit10Files/pi_digits.txt') as file_object :
    contents = file_object.read()
    print(contents)



with open('G:\\ppjforall\\remote\\pythonleanrning\\Unit10Files\\pi_digits.txt') as file_object :
    contents = file_object.read()
    print(contents)
    print("------------------------------------------------")
"""
这个unicode就非常幽默，因为它这个必须转义，所以说尽管是windows的绝对路径，也要转义
"""


"""
逐行读取,如果仅仅是这样，空白行会更多，应该直接strip(前后的空白都给删了）
rstrip 只删右边

readline 和readlines是不一样的.

"""

file_name="pi_digits.txt"
with open(file_name) as file_object:
    for line1 in file_object:
        print(line1.strip())
with open(file_name) as file_object:
    lines =file_object.readlines()
#读取每一行然后把他存储 到一个列表里,使用readlines方法
for line in lines:
    print(line)
if 3589 in lines:
    print("that is the right pi")
else:
    print("fuck,that one was separated")



"""
写入文件，两种模式，一种是覆写模式，一种是链接模式,分别为'w'  'a'  that is that 
写入文件则可以创建文件，所以不必在乎到底有没有这个文件
默认参数是读取文件
"""

file_name2="programming.txt"
with open(file_name2,'w') as file_object:
    file_object.write("I really love to program\n")
#注意！python只能写入字符串，无法像java一样生成文件字节流对象，所以如果要写入其他东西，类似int，则必须str()函数
#编码问题还没有考虑过
#write不会在你的文末自动增加换行符，你可以\n
with open(file_name2,"a") as file_object:
    file_object.write("I really want to do sth!")

#

