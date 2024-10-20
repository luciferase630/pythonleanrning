
# Python 文件操作详解

本篇文档详细讲解了 Python 中的文件操作，包括文件的读取、写入、路径处理，以及常见的模式和技巧。通过简洁的示例说明如何进行文件的常用操作。

---

## 1. 文件打开与关闭

### 1.1 `open()` 函数

- **`open()`** 是 Python 中用于打开文件的函数，返回一个文件对象。常见的参数有：
    - **文件路径**：可以是相对路径或绝对路径。
    - **模式**：指定文件的打开方式（`r` 读取、`w` 写入、`a` 附加等）。
    - **编码**：指定文件的字符编码（例如：`encoding='utf-8'`）。

    - **示例**：
    ```python
    with open('pi_digits.txt') as file_object:
        contents = file_object.read()
        print(contents)  # 输出文件内容
    ```

### 1.2 使用 `with` 自动关闭文件

- 使用 `with` 语句可以自动管理文件的打开和关闭，避免忘记关闭文件导致资源泄露。
    - **示例**：
    ```python
    with open('pi_digits.txt') as file_object:
        contents = file_object.read()
        print(contents)  # 读取文件后自动关闭
    ```

### 1.3 路径处理

- **相对路径与绝对路径**：
    - 相对路径：相对于当前工作目录的路径。
    - 绝对路径：指定文件的完整路径。
    - Windows 的路径使用反斜杠 `\`，需要使用转义字符或正斜杠 `/`。
    ```python
    # 绝对路径示例
    with open('G:/folder/file.txt') as file_object:
        contents = file_object.read()
    ```

---

## 2. 文件的读取

### 2.1 读取整个文件

- **`read()`**：一次性读取整个文件内容。
    - **示例**：
    ```python
    with open('pi_digits.txt') as file_object:
        contents = file_object.read()
        print(contents.strip())  # 去除文件内容中的多余空白
    ```

### 2.2 逐行读取

- **`readline()`**：每次读取文件的一行。
- **`readlines()`**：读取文件的所有行并返回一个列表。
    - **示例**：
    ```python
    with open('pi_digits.txt') as file_object:
        for line in file_object:
            print(line.strip())  # 去除每行末尾的换行符
    ```

### 2.3 `readlines()` 方法

- **`readlines()`**：将文件的所有行存储在一个列表中，便于遍历或后续处理。
    ```python
    with open('pi_digits.txt') as file_object:
        lines = file_object.readlines()
    
    for line in lines:
        print(line.strip())  # 输出每行内容
    ```

---

## 3. 文件的写入

### 3.1 写入文件

- **写入模式**：使用 `'w'` 模式打开文件可以写入内容，如果文件不存在会创建新文件，文件已存在则会覆盖。
    - **示例**：
    ```python
    file_name = 'programming.txt'
    with open(file_name, 'w') as file_object:
        file_object.write("I love programming.
")
    ```

- **注意**：`write()` 方法不会自动在文件末尾添加换行符，需要手动添加 `\n`。

### 3.2 附加模式

- **附加模式**：使用 `'a'` 模式可以在文件末尾追加内容，不会覆盖文件现有内容。
    - **示例**：
    ```python
    with open('programming.txt', 'a') as file_object:
        file_object.write("I want to do more programming!
")
    ```

---

## 4. 错误处理

### 4.1 `FileNotFoundError` 异常

- 当试图打开不存在的文件时，会抛出 `FileNotFoundError` 异常，可以使用 `try-except` 来处理。
    ```python
    try:
        with open('missing_file.txt') as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        print("The file was not found.")
    ```

### 4.2 处理非文本文件

- 当处理非文本文件时（如图片、音频文件），需要使用**二进制模式**来打开文件。
    ```python
    with open('image.png', 'rb') as binary_file:
        data = binary_file.read()
    ```

---

## 示例代码

```python
# 读取文件的示例
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.strip())

# 写入和附加内容到文件
file_name = 'programming.txt'
with open(file_name, 'w') as file_object:
    file_object.write("I love programming.
")

with open(file_name, 'a') as file_object:
    file_object.write("I want to do more programming!
")

# 错误处理
try:
    with open('missing_file.txt') as file_object:
        contents = file_object.read()
except FileNotFoundError:
    print("The file was not found.")
```

---

## 总结

- **`with open()`** 是文件处理的最佳实践，自动管理文件的打开与关闭。
- **读取文件** 可以使用 `read()`、`readline()`、`readlines()` 等方法。
- **写入文件** 需要指定模式 `'w'`、`'a'`，并注意字符串写入要求。
- **错误处理** 在文件操作中非常重要，尤其是处理文件路径和文件不存在的情况。
