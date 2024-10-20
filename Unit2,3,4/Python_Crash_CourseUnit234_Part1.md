
# Python Crash Course - 第二章与第三章 速成讲解 (Part 1)

本篇文档基于《Python Crash Course》的内容，为你提供第二章和第三章的重点速成笔记，包括变量、字符串、列表等基本语法知识。

---

## 第二章 变量和简单的数据类型

### 1. 打印与字符串

- **print() 函数**：用于打印输出信息，括号中的内容会被输出到控制台。
    ```python
    print("hello") # 输出：hello
    ```

- **变量的定义**：Python 中变量不需要声明，直接赋值即可。变量名只能由字母、数字和下划线组成，并且必须以字母或下划线开头，不能使用关键字。
    ```python
    message = "goodmorning"
    ```

### 2. 字符串的操作

- **字符串方法**：
    1. `name.title()`：将字符串首字母大写。
    2. `rstrip()`：去除字符串末尾的空格。
        ```python
        message = " goodmorning "
        print(message.rstrip()) # 输出：goodmorning
        ```

- **字符串拼接**：使用 `+` 号可以拼接多个字符串。
    ```python
    full_name = "what" + "how"
    ```

- **转义字符**：常用的转义字符包括：
    - `\t`：制表符
    - `\n`
`：换行符

- **`str()` 函数**：将整数转换为字符串，用于拼接字符串与数字。
    ```python
    age = 25
    print("I am " + str(age) + " years old.") # 输出：I am 25 years old.
    ```

---

## 第三章 列表的基本使用

### 1. 列表的定义与操作

- **列表 (list)** 是一种有序的集合，使用方括号 `[]` 表示，列表中的元素可以是不同类型。
    ```python
    bicycles = ['trek', 'cannondale', 'redline']
    print(bicycles) # 输出：['trek', 'cannondale', 'redline']
    ```

- **索引**：列表索引从 0 开始，负索引 `-1` 表示最后一个元素。
    ```python
    print(bicycles[0]) # 输出：trek
    print(bicycles[-1]) # 输出：redline
    ```

- **修改元素**：可以通过索引直接修改列表中的元素。
    ```python
    bicycles[1] = 'specialized'
    ```

- **添加元素**：
    1. `append()`：在列表末尾追加新元素。
    2. `insert(index, value)`：在指定索引位置插入元素。
        ```python
        bicycles.append('giant') # 在末尾添加
        bicycles.insert(0, 'schwinn') # 在索引 0 处插入
        ```

- **删除元素**：
    1. `del`：根据索引删除元素。
    2. `pop()`：弹出并返回列表中的最后一个元素，也可以通过索引弹出指定位置的元素。
    3. `remove(value)`：根据值删除列表中的元素。
        ```python
        del bicycles[2] # 删除索引 2 的元素
        last_bike = bicycles.pop() # 弹出最后一个元素
        bicycles.remove('trek') # 删除 'trek'
        ```

### 2. 列表的排序与反转

- **永久排序**：
    1. `sort()`：按字母顺序永久排序。
    2. `sort(reverse=True)`：按字母逆序永久排序。
        ```python
        bicycles.sort() # 正序排序
        bicycles.sort(reverse=True) # 逆序排序
        ```

- **临时排序**：
    - `sorted()`：返回排序后的新列表，原列表不变。
    ```python
    sorted_bicycles = sorted(bicycles) # 临时排序
    ```

- **反转列表**：
    - `reverse()`：直接反转列表元素的顺序。
    ```python
    bicycles.reverse()
    ```

- **获取列表长度**：
    - `len()`：返回列表的长度。
    ```python
    print(len(bicycles)) # 输出列表中的元素数量
    ```

--- 

## 列表索引与避免错误

- **负索引**：`-1` 返回最后一个元素，`-2` 返回倒数第二个元素。
- **避免索引错误**：如果列表为空或索引超出范围，将会抛出 `IndexError`。

---

## 示例代码

```python
bicycles = ['trek', 'cannondale', 'redline']
print(bicycles)

bicycles.append('what')
bicycles.insert(0, 'how')
del bicycles[2]
print(bicycles)
```

