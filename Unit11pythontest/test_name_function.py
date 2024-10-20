#单元测试的意义：不用再像你之前写c语言一样就仅仅是手动输入各种样例，直接编写代码来进行自动测试
import unittest

from names import get_formatted_name


class NamesTestCase(unittest.TestCase):
    """测试name_function的操作"""
    def test_first_last_name(self):
        """第一个测试"""
        formatted_name=get_formatted_name("john",'niko')
        self.assertEqual(formatted_name,'John Niko')
if __name__ == '__main__':
    unittest.main()


"""
1莫名其妙说我No tests ran 
服了，现在集成工具都不让我用了
python integrated

2太有操作了，如果没有test为第一个名字，则不会被识别为test代码

3,这里输出的时候居然用的是标准错误流，控制台是红色的。stderr
p193
assertEqual(a,b) 核实a==b
assertNotEqual(a,b) 核实a!=b
assertTrue(x)核实x为true，非零值全部都被解释为真值  b=(bool)x ，顺便说一下无穷大的问题pos_inf = float('inf')  # 正无穷  neg_inf = float('-inf')  # 负无穷
assertFalse(x)核实x为false
assertIn(Item,List)
assertNotIN(item,list) 这些都十分显然。 那有没有dictionary的呢？，字典就只能检查键了

这里顺便提一下assert语句
assert 条件, "错误信息"
def calculate_average(scores):
    assert len(scores) > 0, "分数列表不能为空"
    return sum(scores) / len(scores)
我现在估计用不上





"""

