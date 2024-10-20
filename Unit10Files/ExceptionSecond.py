#from Unit10Files.Filefirst import file_object
#这一句话到底导入了什么玩意？

a=5
#print('a'+a)
#python是不允许这种直接连接的，但是java可以，emmmm略有不习惯

"""
ZeroDivisionError

引入try except 的用法
"""
try:
    print(5/2)
except ZeroDivisionError:
    print("you have done the wrong thing")
else:print("you have done the right thing")#这相当于还在这个try代码块里，然后try完成功了运行else，但如果像java一样放后面有何不可？真是莫名其妙

result = 5 // 2
#重要的是整除，不用再考虑int除以int什么类型转换的问题
#这甚至也不用说这个异常的名字到底是什么

#然后处理fileNotFoundError
file_name = 'alice.txt'
try:
    with open(file_name) as f_obj:
        contents=f_obj
except FileNotFoundError:
    print("you fucked up")
finally:print("ok")
try:
    with open("alice_wonderland.txt",encoding='utf-8') as file_novel:
        contents= file_novel.read()
except FileNotFoundError:
    print("no")
#split方法
words =contents.split()
print(len(words))

try:
    with open(file_name) as f_obj:
        contents=f_obj
except FileNotFoundError:
    pass
line='Row,row,row your boat'
line.count('row',1,5)#一种传参方式，start和end是切片用
line.lower().count('row')#连续的方法调用，只要你知道返回的是什么
#这个except可以这样做,什么也不干，但是我也不知道这个pass是不是类似空语句。就是花括号{}

