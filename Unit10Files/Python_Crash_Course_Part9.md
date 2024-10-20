
# Python Crash Course - 第十章 异常处理与字符串操作

本篇文档详细讲解了 Python 中的异常处理机制、`try-except` 块的使用，以及字符串的常见操作。通过简洁的示例说明如何处理常见的错误，并介绍了基本的字符串处理方法。

---

## 1. 异常处理

### 1.1 什么是异常？

- **异常** 是程序运行时的错误，Python 提供了异常处理机制，确保程序在遇到错误时不会立即崩溃，而是可以执行一些其他操作或安全退出。
- Python 使用 **`try-except` 块** 来处理可能发生的异常。

    - **示例**：
    ```python
    try:
        print(5 / 0)  # 会引发 ZeroDivisionError 异常
    except ZeroDivisionError:
        print("You can't divide by zero!")  # 捕获异常并执行替代操作
    ```

### 1.2 `try-except-else` 结构

- **`else` 块**：如果 `try` 块中的代码没有引发异常，Python 将执行 `else` 块中的代码。
    ```python
    try:
        result = 5 / 2
    except ZeroDivisionError:
        print("Error: Division by zero.")
    else:
        print("The result is", result)  # 当没有异常时执行
    ```

### 1.3 `finally` 块

- **`finally`** 块中的代码无论是否有异常，都会被执行，通常用于清理资源。
    ```python
    try:
        print(5 / 2)
    except ZeroDivisionError:
        print("You can't divide by zero!")
    finally:
        print("This will always run.")  # 无论有无异常都会执行
    ```

---

## 2. 文件操作中的异常处理

### 2.1 处理 `FileNotFoundError`

- **文件未找到错误**：当尝试打开不存在的文件时，Python 会抛出 `FileNotFoundError`，可以使用 `try-except` 块来处理。
    ```python
    file_name = 'alice.txt'
    try:
        with open(file_name) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        print("The file was not found.")
    ```

### 2.2 `pass` 语句

- **`pass`**：`except` 块中可以使用 `pass` 语句跳过错误处理。
    - **示例**：
    ```python
    try:
        with open('missing_file.txt') as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        pass  # 什么也不做，继续执行
    ```

### 2.3 使用 `finally` 进行资源清理

- **`finally`**：无论文件是否找到，都会执行 `finally` 块中的代码，通常用于关闭文件或释放资源。
    ```python
    try:
        with open("alice_wonderland.txt", encoding='utf-8') as file_novel:
            contents = file_novel.read()
    except FileNotFoundError:
        print("File not found!")
    finally:
        print("Finished attempting to open file.")
    ```

---

## 3. 字符串操作

### 3.1 字符串分割

- **`split()`**：将字符串按空格或指定分隔符分割为一个列表。
    ```python
    line = "Row, row, row your boat"
    words = line.split()
    print(words)  # 输出：['Row,', 'row,', 'row', 'your', 'boat']
    ```

- **`count()`**：统计子字符串在字符串中出现的次数。
    - **示例**：
    ```python
    line = 'Row, row, row your boat'
    print(line.count('row'))  # 输出：2
    print(line.lower().count('row'))  # 输出：3，忽略大小写
    ```

### 3.2 连续方法调用

- **链式调用**：可以连续调用多个方法，前一个方法的返回值作为下一个方法的输入。
    ```python
    line = "Row, row, row your boat"
    print(line.lower().count('row'))  # 先转换为小写，再统计 'row' 出现的次数
    ```

### 3.3 字符串切片

- **字符串切片**：可以通过指定开始和结束索引来获取字符串的子串。
    ```python
    line = "Row, row, row your boat"
    print(line[1:5])  # 输出：'ow, '
    ```

---

## 4. 示例代码

```python
# 异常处理示例
try:
    print(5 / 0)
except ZeroDivisionError:
    print("You can't divide by zero!")

# 文件操作中的异常处理
file_name = 'alice.txt'
try:
    with open(file_name) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    print("The file was not found.")
finally:
    print("Finished attempting to open file.")

# 字符串操作示例
line = 'Row, row, row your boat'
print(line.count('row'))  # 输出 2
print(line.lower().count('row'))  # 输出 3
```

---

## 总结

- **`try-except`** 块用于处理异常，确保程序在发生错误时不会崩溃。
- **`else` 和 `finally`** 块可以帮助处理成功的操作或清理资源。
- **字符串操作** 如 `split()`、`count()` 和链式调用是处理文本的常用技巧。
- 通过异常处理，程序可以更稳健地应对不确定性，如文件不存在或数学错误。
