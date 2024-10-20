
# Python Crash Course - 第七章 用户输入和 `while` 循环

本篇文档详细讲解了 Python 中用户输入的处理、`while` 循环的使用、`break` 和 `continue` 语句，并通过实例代码进行解释和补充。

---

## 1. 用户输入

- **`input()` 函数**：用于接收用户输入，括号内的参数是提示信息。
    ```python
    message = input("What do you want to enter? ")
    print(message)  # 打印用户输入的内容
    ```

### 2. 数据类型转换

- **字符串转整数**：用户输入的内容默认是字符串，如果需要将其转换为整数，可以使用 `int()` 函数。
    ```python
    age = int(input("How old are you? "))
    print(f"You are {age} years old.")
    ```

- **求模运算符**：用于计算两个数的余数，常用于判断奇偶等情况。
    ```python
    number = int(input("Enter a number: "))
    if number % 2 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")
    ```

---

## 3. `while` 循环

- **基本 `while` 循环**：当条件为 `True` 时，`while` 循环会一直执行，直到条件为 `False`。
    ```python
    x = 1
    while x <= 5:
        print(x)
        x += 1  # 每次循环后自增 x
    ```

- **无限循环**：当循环条件始终为 `True` 时，会进入无限循环。可以通过按 `Ctrl + C` 来强制退出程序。
    ```python
    while True:
        print("This is an infinite loop. Press Ctrl + C to stop.")
    ```

- **使用标志控制循环**：通过设置标志变量来控制循环的执行。
    ```python
    active = True
    while active:
        message = input("Enter 'quit' to end the loop: ")
        if message == 'quit':
            active = False  # 修改标志，结束循环
        else:
            print(f"You entered: {message}")
    ```

- **`break` 语句**：用于立即退出循环。
    ```python
    while True:
        message = input("Enter something (type 'exit' to quit): ")
        if message == 'exit':
            break  # 立即退出循环
        print(f"You entered: {message}")
    ```

- **`continue` 语句**：用于跳过当前循环的剩余代码，并开始下一次循环。
    ```python
    x = 0
    while x < 10:
        x += 1
        if x % 2 == 0:
            continue  # 跳过偶数并进入下一次循环
        print(x)  # 只输出奇数
    ```

---

## 4. 使用 `while` 循环修改列表

- **在 `while` 循环中修改列表**：
    - 在遍历列表时，**不建议**在 `for` 循环中修改列表的元素，建议使用 `while` 循环。
    - **示例**：移除列表中的特定元素。
    ```python
    pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
    print(pets)

    while 'cat' in pets:
        pets.remove('cat')  # 每次移除一个 'cat'
    
    print(pets)  # 输出移除 'cat' 后的列表
    ```

- **注意**：`remove()` 方法只会删除列表中第一次出现的匹配元素。因此，如果列表中有多个相同元素，可以使用 `while` 循环逐个删除。

---

## 5. 使用标志和输入循环

- **使用标志来控制循环**：通过一个布尔标志来决定是否继续执行循环。
    ```python
    active = True
    while active:
        message = input("Enter something (or type 'quit' to stop): ")
        
        if message == 'quit':
            active = False  # 设置标志为 False 来终止循环
        else:
            print(f"You entered: {message}")
    ```

---

## 6. 循环实例：处理用户输入

- 通过 `input()` 读取用户输入，并使用 `while` 循环持续处理用户的输入，直到用户输入特定的命令退出。
    ```python
    prompt = "
Tell me something, and I will repeat it back to you:"
    prompt += "
Enter 'quit' to end the program. "

    message = ""
    while message != 'quit':
        message = input(prompt)
        if message != 'quit':
            print(message)
    ```

---

## 示例代码

```python
# 简单的输入输出示例
message = input("What do you want to enter? ")
print(message)

# while 循环控制输入
x = 1
while x <= 5:
    print(x)
    x += 1

# 标志控制循环
active = True
while active:
    message = input("Enter 'quit' to end the loop: ")
    if message == 'quit':
        active = False
    else:
        print(f"You entered: {message}")

# 使用 break 和 continue
while True:
    message = input("Enter something (type 'exit' to quit): ")
    if message == 'exit':
        break
    print(f"You entered: {message}")

x = 0
while x < 10:
    x += 1
    if x % 2 == 0:
        continue
    print(x)
```

---

## 总结

- **`while` 循环** 用于在条件为真时重复执行一段代码，直到条件变为假。
- **`input()`** 用于获取用户输入，输入默认是字符串，需要转换为其他数据类型时可以使用 `int()` 等函数。
- **`break`** 和 **`continue`** 是控制循环执行的重要工具，分别用于退出循环和跳过当前循环。
