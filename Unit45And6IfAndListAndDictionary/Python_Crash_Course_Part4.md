
# Python Crash Course - 第六章速成讲解 (Part 2)

本篇文档详细讲解了 Python 中的字典，包括字典的基本操作、遍历、嵌套字典与列表的使用，并对代码进行了修正与优化。

---

## 第六章 字典

### 1. 字典的定义与基本操作

- **字典 (dictionary)** 是一组 `key-value` 对的集合，使用花括号 `{}` 表示，每个键和值通过冒号 `:` 分隔。
    - **定义字典**：
    ```python
    alien = {'color': 'red', 'points': 5}
    print(alien['color'])  # 输出：red
    ```

- **添加键值对**：
    - 通过 `alien['key'] = value` 的形式，可以为字典添加新的键值对。
    ```python
    alien['x_position'] = 9
    ```

- **修改值**：
    - 直接通过键索引修改对应的值。
    ```python
    alien['color'] = 'green'
    ```

- **删除键值对**：
    1. 使用 `del` 删除指定键的键值对。
    2. 使用 `pop()` 删除键值对并返回被删除的值。
    ```python
    del alien['points']  # 删除 'points' 键
    color = alien.pop('color')  # 弹出并返回 'color' 的值
    ```

---

### 2. 遍历字典

- **遍历字典中的键值对**：
    - 使用 `items()` 方法同时遍历键和值。
    ```python
    for key, value in alien.items():
        print(f"Key: {key}")
        print(f"Value: {value}")
    ```

- **遍历键**：
    - 使用 `keys()` 方法可以遍历字典的所有键。
    - 还可以通过 `sorted()` 对键进行排序。
    ```python
    for key in alien.keys():
        print(key)
    ```

- **遍历值**：
    - 使用 `values()` 方法遍历字典中的所有值。
    ```python
    for value in alien.values():
        print(value)
    ```

---

### 3. 字典与列表的嵌套

- **列表中嵌套字典**：列表的每个元素可以是字典，常用于存储具有相同结构的多个字典。
    ```python
    aliens = []
    for alien_number in range(3):
        new_alien = {'color': 'green', 'points': 5}
        aliens.append(new_alien)
    print(aliens)
    ```

- **字典中嵌套列表**：字典的值可以是列表，适用于存储多个值的场景。
    ```python
    pizza = {
        'crust': 'thick',
        'toppings': ['mushrooms', 'extra cheese'],
    }
    ```

- **字典中嵌套字典**：可以在字典的值中嵌套另一个字典，常用于描述更复杂的结构。
    ```python
    users = {
        'aeinstein': {
            'first': 'albert',
            'last': 'einstein',
        },
        'mcurie': {
            'first': 'marie',
            'last': 'curie',
        }
    }
    ```

---

## 示例代码

```python
alien = {'color': 'red', 'points': 5}
print(alien['color'])

# 添加新键值对
alien['x_position'] = 9

# 遍历字典中的键值对
for key, value in alien.items():
    print(f"Key: {key}")
    print(f"Value: {value}")

# 删除键值对
print(alien.pop('color'))

# 遍历键
for name in alien.keys():
    print(name)

# 嵌套字典与列表
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese']
}
print(pizza)
```

---

## 纠错与补充

1. **删除操作**：使用 `del` 和 `pop()` 删除字典中的键值对，`del` 直接删除，`pop()` 返回被删除的值。
2. **嵌套数据结构**：Python 支持字典与列表的嵌套，可以通过这种方式组织更复杂的数据结构，如列表中嵌套字典，字典中嵌套列表。
