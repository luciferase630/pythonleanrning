
# Python Crash Course - 单元测试与 `unittest` 模块

本篇文档详细讲解了 Python 中的单元测试，重点介绍 `unittest` 模块的使用。通过分析代码和扩展知识点，学习如何编写和组织自动化测试，提升代码的健壮性与稳定性。

---

## 1. 什么是单元测试？

### 1.1 单元测试的意义

- **单元测试** 是自动化测试的一种，用来验证代码的某个特定模块（如函数、类）的行为是否符合预期。
- 单元测试可以替代手动输入样例，自动化执行测试代码，捕获异常和错误，减少人工测试的时间和错误率。

    - **示例**：
    ```python
    import unittest
    from names import get_formatted_name

    class NamesTestCase(unittest.TestCase):
        """测试 `get_formatted_name` 函数"""
        
        def test_first_last_name(self):
            formatted_name = get_formatted_name("john", "niko")
            self.assertEqual(formatted_name, 'John Niko')

    if __name__ == '__main__':
        unittest.main()
    ```

### 1.2 `unittest` 模块简介

- **`unittest`** 是 Python 自带的测试模块，用于编写单元测试。通过继承 `unittest.TestCase` 类，我们可以轻松地编写和运行测试。

---

## 2. 基本的测试方法

### 2.1 编写测试类与测试方法

- 每个测试类都继承自 `unittest.TestCase`，每个测试方法都以 **`test_`** 开头，以便测试框架识别它们为测试。
    - **示例**：
    ```python
    class NamesTestCase(unittest.TestCase):
        def test_first_last_name(self):
            formatted_name = get_formatted_name("john", "niko")
            self.assertEqual(formatted_name, 'John Niko')
    ```

### 2.2 常用的断言方法

- **`assertEqual(a, b)`**：判断 `a == b`，核实两个值是否相等。
- **`assertNotEqual(a, b)`**：判断 `a != b`。
- **`assertTrue(x)`**：判断 `x` 是否为 `True`。
- **`assertFalse(x)`**：判断 `x` 是否为 `False`。
- **`assertIn(item, list)`**：检查 `item` 是否在 `list` 中。
- **`assertNotIn(item, list)`**：检查 `item` 是否不在 `list` 中。

    - **示例**：
    ```python
    self.assertEqual(formatted_name, 'John Niko')
    self.assertIn('English', my_survey._responses)
    ```

### 2.3 其他常见断言

- **`assertRaises()`**：测试某个错误是否被引发。
    - **示例**：
    ```python
    with self.assertRaises(ValueError):
        some_function()  # 此处会引发 ValueError
    ```

---

## 3. 测试执行流程

### 3.1 测试时机：`if __name__ == '__main__'`

- **`unittest.main()`**：用于启动测试运行，自动发现并运行所有以 `test_` 开头的测试方法。
- **`if __name__ == '__main__'`**：确保当脚本作为主程序运行时执行测试，而不是被导入时。

### 3.2 `setUp()` 方法

- **`setUp()`** 方法会在每个测试方法运行之前自动调用，用于创建测试时需要的对象和数据。这样可以避免在每个测试方法中重复相同的初始化代码。
    - **示例**：
    ```python
    class TestAnonymousSurvey(unittest.TestCase):
        def setUp(self):
            question = "What language did you first learn to speak?"
            self.my_survey = AnonymousSurvey(question)
            self.responses = ['English', 'Spanish', 'Mandarin']

        def test_store_multiple_responses(self):
            for response in self.responses:
                self.my_survey.store_response(response)
            for response in self.responses:
                self.assertIn(response, self.my_survey._responses)
    ```

- `setUp()` 方法的优势在于为每个测试方法创建干净的测试环境，确保每个测试相互独立，且不会相互影响。

---

## 4. 常见问题与调试

### 4.1 测试未运行的问题

- 如果没有以 `test_` 为前缀命名测试方法，`unittest` 不会识别为测试用例，导致测试未运行。
- 确保测试方法的命名符合 `unittest` 的规范。

    - **示例**：
    ```python
    def test_first_last_name(self):  # 正确命名
        pass

    def first_last_name(self):  # 不会被识别为测试
        pass
    ```

### 4.2 `stderr` 输出问题

- 当测试失败时，`unittest` 会将错误信息输出到标准错误流（`stderr`），通常以红色显示。可以通过捕获异常来调试问题。

---

## 5. 示例代码

```python
# 测试函数 get_formatted_name
import unittest
from names import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """测试 get_formatted_name 函数"""
    
    def test_first_last_name(self):
        formatted_name = get_formatted_name("john", "niko")
        self.assertEqual(formatted_name, 'John Niko')

if __name__ == '__main__':
    unittest.main()

# 测试类 AnonymousSurvey
class AnonymousSurvey:
    def __init__(self, question):
        self._question = question
        self._responses = []

    def store_response(self, new_response):
        self._responses.append(new_response)

class TestAnonymousSurvey(unittest.TestCase):
    def setUp(self):
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Mandarin']

    def test_store_multiple_responses(self):
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey._responses)

if __name__ == '__main__':
    unittest.main()
```

---

## 总结

- Python 的 `unittest` 模块通过继承 `unittest.TestCase` 提供了便捷的单元测试方法。
- 断言方法如 `assertEqual()`、`assertIn()` 等可以帮助验证测试结果。
- `setUp()` 方法可以减少重复代码，提高测试的可维护性。
- 通过自动化测试，确保代码在各种场景下都能正常工作。
