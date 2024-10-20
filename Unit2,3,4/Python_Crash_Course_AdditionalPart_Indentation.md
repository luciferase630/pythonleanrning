
# Python 缩进规则与代码组织逻辑

本篇文档详细讲解了 Python 中的缩进规则，帮助有代码编写基础的用户理解如何通过缩进来组织代码。Python 不使用括号 `{}` 来表示代码块，而是依赖缩进来表示代码的层次结构。

---

## 1. 基本缩进规则

### 1.1 缩进的作用

- 在 Python 中，代码块（如函数、循环、条件判断等）使用**缩进**来标识代码的层级，而不像 C、Java 等语言使用 `{}`。
- **缩进** 是 Python 语法中的强制要求，每个嵌套的代码块都必须相对于上一级的代码块缩进。

### 1.2 缩进的标准

- **每一级缩进建议使用 4 个空格**，这也是 PEP 8（Python 的官方代码风格指南）推荐的标准。Python 也允许使用制表符 `	`，但不建议混用空格和制表符。
    ```python
    def greet_user(username):
        print("Hello, " + username.title() + "!")
    ```

    - `print()` 是 `greet_user()` 函数的主体部分，因此它比函数定义多一个缩进。

---

## 2. 常见代码块的缩进

### 2.1 条件语句的缩进

- **`if` 语句**：条件判断后的代码块需要缩进。
    ```python
    age = 18
    if age >= 18:
        print("You are an adult.")
    else:
        print("You are a minor.")
    ```

    - 当条件满足时，`if` 语句之后的代码块会被执行，`else` 语句同理。

### 2.2 循环语句的缩进

- **`for` 循环**：循环体中的代码同样需要缩进。
    ```python
    for i in range(5):
        print(i)
    ```

    - 这里 `print(i)` 是 `for` 循环的一部分，因此相对于 `for` 语句缩进了 4 个空格。

### 2.3 函数的缩进

- **函数定义**：函数体的代码必须缩进，表示函数内部的逻辑。
    ```python
    def greet_user(username):
        print("Hello, " + username.title() + "!")
    ```

    - `print()` 是 `greet_user()` 函数的一部分，因此它相对于 `def` 缩进。

---

## 3. 嵌套结构的缩进

- **嵌套条件或循环**：当代码块中嵌套另一个代码块时，每层嵌套都需要增加 4 个空格的缩进。
    ```python
    age = 20
    if age >= 18:
        if age >= 21:
            print("You can drink alcohol.")
        else:
            print("You can vote.")
    ```

    - 这里 `if` 语句嵌套了另一个 `if-else` 结构，因此内部的 `print()` 相对于外部的 `if` 多缩进了一层。

---

## 4. 缩进错误

### 4.1 `IndentationError` 错误

- 如果代码块的缩进不一致或错误，Python 会抛出 `IndentationError`，如以下代码：
    ```python
    if True:
        print("This line is correctly indented.")
       print("This line has incorrect indentation.")  # 报错：IndentationError
    ```

    - 由于第二行 `print()` 缩进不一致，Python 将抛出 `IndentationError`。

### 4.2 混合使用空格和制表符

- **避免混用空格和制表符**：Python 允许使用制表符进行缩进，但最好避免空格和制表符混合使用，因为这可能导致不一致的缩进和错误。

---

## 5. PEP 8 缩进规范

- **PEP 8** 是 Python 官方推荐的代码风格指南，关于缩进的建议如下：
    1. **每级缩进 4 个空格**。避免使用 2 个空格或 8 个空格的缩进。
    2. **不要混用空格和制表符**。在同一个项目中，尽量统一使用空格或制表符，不要混合使用。

    ```python
    def main():
        for i in range(5):
            print(i)
    ```

---

## 示例代码

```python
# 示例：Python 中的缩进
def greet_user(username):
    if username:
        print("Hello, " + username + "!")
    else:
        print("Hello, Guest!")

# 调用函数
greet_user('Alice')
```

---

## 总结

- Python 的缩进是代码结构的重要组成部分，替代了其他语言中的 `{}` 大括号。
- 标准缩进为 4 个空格，每个嵌套代码块需要多一级缩进。
- 一旦缩进不正确，Python 会抛出 `IndentationError` 错误，确保缩进保持一致。
- 遵循 PEP 8 规范，可以使代码更加可读和一致。

