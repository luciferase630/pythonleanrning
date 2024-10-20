
# Python Crash Course - 第九章 类与继承

本篇文档详细讲解了 Python 类的定义、属性与方法的使用、继承的实现，并通过实例代码深入说明如何组织和使用类。

---

## 1. 类的定义与实例化

### 1.1 定义类与 `__init__` 方法

- **类定义**：使用 `class` 关键字定义一个类，类名通常使用大写字母开头的驼峰命名法。
- **`__init__` 方法**：用于初始化对象的构造函数，在创建类的实例时自动调用。`__init__` 方法中的参数包括实例的属性，通过 `self` 参数访问实例对象。

    - **示例**：
    ```python
    class Dog:
        def __init__(self, name, age):
            self.name = name  # 公共属性
            self.__age = age  # 私有属性，前置双下划线

        def sit(self):
            print(self.name.title() + " is now sitting")

    my_dog = Dog("jane", 5)
    my_dog.sit()  # 输出：Jane is now sitting
    ```

- **属性定义**：类的属性在 `__init__` 方法中定义，直接通过 `self.attribute` 进行赋值和访问。

### 1.2 访问控制

- **公开属性**：默认情况下，类的属性和方法都是公开的。
    ```python
    class Dog:
        def __init__(self, name, age):
            self.name = name  # 公共属性

    my_dog = Dog("jane", 5)
    print(my_dog.name)  # 输出：jane
    ```

- **保护属性**：使用单下划线 `_` 开头的属性表示受保护的属性，它是一种约定，不建议外部直接访问，但可以在子类中访问。
    ```python
    class Dog:
        def __init__(self, name, age):
            self._age = age  # 保护属性

    my_dog = Dog("jane", 5)
    print(my_dog._age)  # 仍然可以访问
    ```

- **私有属性**：使用双下划线 `__` 开头的属性表示私有属性，只能在类的内部访问，外部无法直接访问。
    ```python
    class Dog:
        def __init__(self, name, age):
            self.__age = age  # 私有属性

    my_dog = Dog("jane", 5)
    # print(my_dog.__age)  # 报错：AttributeError: 'Dog' object has no attribute '__age'
    ```

---

## 2. 类的方法

### 2.1 公共方法与保护方法

- **公共方法**：类中的普通方法，可以在外部自由调用。
    ```python
    def sit(self):
        print(self.name.title() + " is now sitting")
    ```

- **保护方法**：通过单下划线 `_` 开头，表示不建议外部调用，但仍然可以访问。
    ```python
    def _sit(self):
        print(self.name.title() + " is now sitting")
    ```

---

## 3. 类的继承

### 3.1 基本继承

- **继承**：Python 通过类名括号中写入父类名的方式实现继承。子类继承父类的所有属性和方法，并且可以在子类中添加新的属性和方法。
    ```python
    class Car:
        def __init__(self, brand, model):
            self.brand = brand
            self.model = model

        def describe(self):
            print(f"{self.brand} {self.model}")

    class ElectricCar(Car):  # ElectricCar 继承自 Car
        def __init__(self, brand, model, battery_size):
            super().__init__(brand, model)  # 调用父类的构造函数
            self.battery_size = battery_size

        def describe(self):
            super().describe()  # 调用父类的方法
            print(f"Battery size: {self.battery_size} kWh")
    ```

### 3.2 使用 `super()` 调用父类方法

- **`super()`**：用于在子类中调用父类的方法或构造函数，确保子类可以继承父类的行为。
    ```python
    class ElectricCar(Car):
        def __init__(self, brand, model, battery_size):
            super().__init__(brand, model)  # 调用父类的构造函数
            self.battery_size = battery_size
    ```

### 3.3 方法重写

- 子类可以重写父类中的方法。
    ```python
    class ElectricCar(Car):
        def describe(self):
            print(f"This is an electric car: {self.brand} {self.model}")
    ```

---

## 4. 类的属性和方法的命名约定

### 4.1 属性命名规则

- **单下划线 `_attribute`**：表示保护属性，不建议直接访问，但可以通过子类访问。
- **双下划线 `__attribute`**：表示私有属性，只能在类的内部访问，外部无法直接访问。

### 4.2 特殊方法

- Python 中的**魔术方法**（Magic Methods）使用双下划线包裹，如 `__init__`、`__str__` 等。这些方法有特定的用途。
    - **`__init__()`**：构造函数，用于初始化对象。
    - **`__str__()`**：用于返回对象的字符串表示。
    - **示例**：
    ```python
    class Dog:
        def __init__(self, name):
            self.name = name

        def __str__(self):
            return f"Dog's name is {self.name}"

    my_dog = Dog('Spot')
    print(my_dog)  # 输出：Dog's name is Spot
    ```

---

## 5. 示例代码

```python
# 定义 Dog 类
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # 私有属性
        self._addedattribute = 0  # 保护属性

    def _sit(self):  # 保护方法
        print(self.name.title() + " is now sitting")

    def roll_over(self):  # 公共方法
        print(self.name.title() + " rolled over")

# 实例化 Dog 类
my_dog = Dog("Jane", 15)
my_dog._sit()  # 调用保护方法
print(my_dog._addedattribute)  # 访问保护属性

# 定义 Car 类与其子类 ElectricCar
class Car:
    def __init__(self, name, size):
        self._name = name  # 保护属性
        self.__size = size  # 私有属性

    def describe(self):
        print(self._name + " " + str(self.__size), end=' ')

class ElectricCar(Car):
    def __init__(self, name, size, model, year):
        super().__init__(name, size)  # 调用父类构造函数
        self.model = model
        self.year = year

    def describe(self):
        super().describe()  # 调用父类的 describe 方法
        print(self.model + " " + str(self.year))

my_car1 = Car("BMW", 15)
my_electricar1 = ElectricCar("Tesla", 18, "Model Y", 2030)
my_car1.describe()  # 输出：BMW 15
my_electricar1.describe()  # 输出：Tesla 18 Model Y 2030
```

---

## 总结

- Python 类通过 `class` 关键字定义，`__init__()` 方法用于初始化对象。
- 属性和方法的访问控制通过单下划线 `_`（保护）和双下划线 `__`（私有）实现。
- 子类继承父类时，可以使用 `super()` 调用父类的方法和属性，支持重写父类方法。
- Python 的类设计灵活简洁，方便面向对象的编程实践。
