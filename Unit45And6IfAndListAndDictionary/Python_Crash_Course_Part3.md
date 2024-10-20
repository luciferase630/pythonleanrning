
# Python Crash Course - 第四章至第六章速成讲解 (Part 1)

本篇文档详细讲解了 Python 列表切片、元组、`if` 语句、字典等知识，并包括了对代码进行的修正与优化。

---

## 第四章 列表的操作

### 1. 列表切片

- **切片**：通过指定起始、结束和步长来获取列表的一部分。
    - 语法：`list[start:stop:step]`
    - 示例：
    ```python
    players = ['charles', 'marijuana', 'michael', 'florence']
    print(players[0:3])  # 输出：['charles', 'marijuana', 'michael']
    ```

- **起始和结束索引**：
    - `players[:3]`：从列表头开始获取到索引 `3` 之前的元素。
    - `players[2:]`：从索引 `2` 开始，一直到列表末尾的元素。

- **遍历切片**：可以遍历切片的一部分，类似于 `C++` 和 `Java` 中的 `foreach`。
    ```python
    for player in players[:3]:
        print(player)
    ```

- **切片赋值**：可以将切片赋值给其他列表。
    ```python
    playerest = players[:]
    print(playerest)
    ```

### 2. 元组

- **元组 (tuple)**：类似列表，但不可修改。使用圆括号 `()` 表示。
    - **定义元组**：
    ```python
    dimensions = (200, 50)
    ```

- **修改元组的值**：虽然不能直接修改元组中的值，但可以通过重新赋值整个元组来更新内容。
    ```python
    dimensions = (200, 100)
    ```

---

## 第五章 `if` 语句

### 1. 基本 `if` 语句

- **`if` 语句**：用于判断条件并执行相应的代码块。
    - **示例**：
    ```python
    for player in players:
        if player == 'michael':
            print(player.upper())  # 注意：此处需要加括号来调用 `upper()` 方法
        else:
            print(player.title())
    ```

    - **修正**：`player.upper` 应加上括号，以确保调用方法并获取返回值，而不是直接引用函数对象。

### 2. 逻辑运算符

- **逻辑运算**：在 `if` 语句中，可以使用以下运算符：
    - `and`：两个条件都为 `True` 时，返回 `True`。
    - `or`：任一条件为 `True` 时，返回 `True`。
    - `not`：用于取反，`True` 变为 `False`，`False` 变为 `True`。

### 3. 检查元素是否在列表中

- **使用 `in`**：可以使用 `in` 关键字检查元素是否包含在列表中。
    ```python
    if 'mushrooms' in players:
        print("not found")
    ```

- **`if-elif-else` 结构**：用于依次判断多个条件。
    ```python
    if 'mushrooms' in players:
        print("not found")
    elif 'michael' in players:
        print('found')
    else:
        print("fine, ok")
    ```

### 4. 列表为空时的判断

- **空列表**：如果列表为空，则 `if` 判断为 `False`。
    ```python
    requested_players = []
    if requested_players:
        print("列表不为空")
    else:
        print("列表为空")
    ```

---

## 示例代码

```python
players = ['charles', 'marijuana', 'michael', 'florence']
for player in players:
    if player == 'michael':
        print(player.upper())  # 修正：加上括号
    else:
        print(player.title())

# 检查元素是否在列表中
requested_players = players
if 'mushrooms' in requested_players:
    print("not found")
elif 'michael' in requested_players:
    print('found')
else:
    print("fine, ok")
```

---

## 纠错与补充

1. **方法调用问题**：在 Python 中，当你不加括号调用方法时，返回的是方法的引用，而不是方法的执行结果。因此，像 `upper`、`title` 这些字符串方法应该加上括号来执行。
    ```python
    player.upper()  # 正确调用
    ```

2. **`if` 语句的结构**：`if-elif-else` 是标准的选择结构，在条件满足时，后续的 `elif` 和 `else` 语句不会被执行。

