#Refactoring
import json




def get_stored_username(username):
    filename=username
    try:
        with open (filename) as obj:
            username=json.load(obj)
    except FileNotFoundError:
        return None#这个none实际上是一个对象，可以作为值返回并表示无值状态

"""
#函数的默认参数值可以设为none，这点很重要,在函数内判断是否提供了具体的值
在参数较少的时候可以这么操作，因为多了就会有很多条件判断，参数间一般还有相互依赖，降低了代码的可维护性

"""