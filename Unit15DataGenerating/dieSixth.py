from random import randint
class Die:
    """ 表示一个骰子"""
    def __init__(self,num_sides=6):
        """骰子默认六面"""
        self.num_sides=num_sides
    def roll(self):
        """返回一个位于1和骰子面数的随机数"""
        return randint(1,self.num_sides)#这个是范围
