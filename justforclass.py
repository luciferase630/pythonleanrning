class Dog:
    def __init__(self, name, age) -> None:
        self.name = name
        self.__age = age
        self._addedattribute = 0

    def _sit(self):
        print(self.name.title() + "is now sitting")

    def roll_over(self):
        print(self.name.title() + "rolled over")


my_dog = Dog("JANE", 15)
my_dog._sit()
print(my_dog._addedattribute)  # 这个是protected的
#print(my_dog.__age)  # 这行会报错，因为这个__age这个属性，就是私有的
"""
1上面就清清楚楚的写了一个狗类，这个init 必须得__init__这样来声明，真是服了
2这里面怎么不声明属性啊？
属性是相当于就在init里。我真是服了他了
而可以有默认属性
这样干，
self.addedattribute=0
这样的就直接写在init下
3->None 是一种注解
4修改属性的值，通过方法修改属性的值。不是，这python没有访问权限？
通过在属性或方法名前加一个下划线 _ 来表示受保护。
这是一种约定，表示这些属性或方法不应该在类的外部使用，但在子类中可以访问。
__两个下划线就是private了
在子类里确实是调用不了
单下划线就是可以用作方法和属性前
前后都是双下划线是特殊方法
还有python的魔术方法
5继承
继承就没有extends了 直接

"""
class car:
    def __init__(self,name,size):
        self._name=name
        self.__size=size

    def describeeverything(self):
        print(self._name + str(self.__size) )

class Electriccar(car):
    def __init__(self,name,size,model,year):
        super().__init__(name ,size)
        self.model=model
        self.year=year
    def describeeverything(self):
        print(self._name+self.model+str(self.year))

my_car=car("BMW",15)
my_electricar=Electriccar("TESLA",18,"Y",2030)
my_car.describeeverything()
my_electricar.describeeverything()

def cat(Dog):
    def _sit(self):
        print("what is the fuck")

cat()