
# Python Crash Course - 第八章 函数与模块详解

本篇文档详细讲解了 Python 函数的定义、参数传递、返回值，以及模块的导入和函数的别名。并通过实例代码解释 Python 中的多种字符串格式化方式。

---

## 1. 函数的定义与参数传递

### 1.1 基本函数定义

- **函数定义**：通过 `def` 关键字定义一个函数。
    - 函数名称后跟括号，括号内可以包含参数列表，参数可以没有类型注解，参数类型完全动态。
    - **示例**：
    ```python
    def greet_user(username):
        print('hello ' + username.title() + '!')
    ```

### 1.2 传递参数

- **位置参数**：按照顺序传递实参给形参。
    ```python
    greet_user('John')  # 输出：hello John!
    ```

- **关键字参数**：通过参数名传递实参，使调用时参数顺序可以随意。
    ```python
    greet_user(username='Alice')  # 输出：hello Alice!
    ```

### 1.3 默认参数值

- **默认参数值**：在定义函数时，可以为参数提供默认值，未传递该参数时，将使用默认值。
    ```python
    def greet_user(username='Guest'):
        print('hello ' + username + '!')
    
    greet_user()  # 输出：hello Guest!
    greet_user('Tom')  # 输出：hello Tom!
    ```

---

## 2. 列表和任意数量的参数

### 2.1 修改列表

- **传递列表**：列表作为参数传递时，函数可以修改列表的内容。
    ```python
    def process_items(items):
        items.append('new_item')

    items = ['item1', 'item2']
    process_items(items)
    print(items)  # 输出：['item1', 'item2', 'new_item']
    ```

- **传递列表副本**：如果不希望修改原始列表，可以传递列表的副本。
    ```python
    process_items(items[:])  # 传递列表副本
    ```

### 2.2 任意数量的参数

- **任意数量的参数**：通过 `*args` 接收任意数量的位置参数，它们会被封装为一个元组。
    ```python
    def make_pizza(*toppings):
        print(toppings)
    
    make_pizza('pepperoni', 'cheese', 'olives')  # 输出：('pepperoni', 'cheese', 'olives')
    ```

---

## 3. 返回值

- **返回值**：函数可以返回单个值、多个值（使用元组）、或字典等。
    ```python
    def get_formatted_name(first_name, last_name, middle_name=''):
        if middle_name:
            return first_name + ' ' + middle_name + ' ' + last_name
        else:
            return first_name + ' ' + last_name

    name = get_formatted_name('John', 'Doe', 'Michael')
    print(name)  # 输出：John Michael Doe
    ```

---

## 4. 模块与导入

### 4.1 模块导入

- **导入整个模块**：使用 `import module_name`。
    - 之后通过 `module_name.function_name()` 访问模块内的函数。
    ```python
    import math
    print(math.sqrt(16))  # 输出：4.0
    ```

- **导入模块中的特定函数**：使用 `from module_name import function_name`。
    ```python
    from math import sqrt
    print(sqrt(25))  # 输出：5.0
    ```

- **导入并指定别名**：使用 `as` 为模块或函数指定别名。
    ```python
    from math import sqrt as square_root
    print(square_root(36))  # 输出：6.0
    ```

- **导入模块中的所有函数**：使用 `from module_name import *`。
    - 不推荐使用这种方式，因为它可能导致命名冲突。

---

## 5. 字符串格式化方式

### 5.1 f-string 格式化

- **f-string**：Python 3.6 引入的字符串格式化方式，使用 `f` 引导的字符串中，可以直接嵌入表达式和变量。
    ```python
    name = 'John'
    age = 25
    print(f'Hello, {name}. You are {age} years old.')  # 输出：Hello, John. You are 25 years old.
    ```

### 5.2 format() 方法

- **`format()` 方法**：通过位置或关键字参数进行字符串插值。
    ```python
    print("Hello, {}. You are {} years old.".format('Alice', 30))  # 输出：Hello, Alice. You are 30 years old.
    
    # 也可以使用关键字参数
    print("Hello, {name}. You are {age} years old.".format(name='Bob', age=40))  # 输出：Hello, Bob. You are 40 years old.
    ```

### 5.3 百分号格式化

- **百分号格式化**：旧的格式化方式，类似于 C 语言中的 `printf`。
    ```python
    name = 'Charlie'
    age = 28
    print('Hello, %s. You are %d years old.' % (name, age))  # 输出：Hello, Charlie. You are 28 years old.
    ```

---

## 6. 文档字符串与 `if __name__ == '__main__'`

### 6.1 文档字符串

- **文档字符串 (docstring)**：用三重引号 `"""..."""` 定义，用于为函数、模块、类编写说明。
    - 示例：
    ```python
    def f1(a: int):
        """
        这是一个文档字符串
        :param a: 传入的整数值
        :return: 无
        """
        print(f'int{a}')
    ```

### 6.2 `if __name__ == '__main__'` 的作用

- **`if __name__ == '__main__'`**：用于判断当前模块是否是被直接执行还是被导入。
    - 当一个模块被导入时，`__name__` 的值是模块名；当模块被直接执行时，`__name__` 的值是 `'__main__'`。这行代码确保测试代码只在直接执行时被运行。
    ```python
    if __name__ == '__main__':
        print("This code is running as the main program.")
    ```

---

## 示例代码

```python
# 定义一个带默认参数的函数
def greet_user(username='Guest'):
    print('hello ' + username + '!')

# 调用函数
greet_user()  # 输出：hello Guest!
greet_user('Alice')  # 输出：hello Alice!

# f-string 格式化
name = 'John'
age = 25
print(f'Hello, {name}. You are {age} years old.')  # 输出：Hello, John. You are 25 years old.

# 模块导入示例
from math import sqrt
print(sqrt(16))  # 输出：4.0
```

---

## 总结

- **函数** 是组织代码、复用逻辑的重要工具，支持位置参数、关键字参数、默认参数、任意数量参数等多种方式。
- **f-string** 是 Python 3.6 引入的简洁强大的字符串格式化方式，其他格式化方式如 `format()` 和 `%` 也常用。
- **模块** 提供了代码复用与组织的途径，可以通过导入模块的不同方式灵活调用外部代码。
- **`if __name__ == '__main__'`** 是 Python 中控制模块执行的最佳实践。
