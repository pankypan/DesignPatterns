# 设计模式python实现(07)--模板方法模式

**模板方法模式：**通过一个模板方法来定义程序的框架或算法，通常模板方法定义在基类中，即原始的模板，然后子类就可以根据不同的需要实现或重写模板方法中的某些算法步骤或者框架的某部分，最后达到使用相同模板实现不同功能的效果。



## 实现理论

### 核心思想

- 使用一个模板方法定义好总的算法框架。
- 子类中根据需要重新定义某些操作，但是不能修改原始模板方法。
- 在多个算法或框架具有类似或相同的逻辑的时候，可以使用模板方法模式，以实现代码重用。
- 当某些操作是强制子类必须实现的时候，此操作就可以定义为抽象方法，如果不是强制要求子类实现的话，则可以在基类中为它定义一个默认实现。



### 主要角色

- **接口：**通常是抽象基类，定义模板方法中需要的各项操作。
- **模板方法：**即模板算法，定义好各项操作的执行顺序或算法框架。
- **真实对象：**子类通过重新实现接口中的各项操作，以便让模板方法实现不同的功能。



### 优缺点

- **优点：**因为子类的实现是根据基类中的模板而来的，所以可以实现代码重用，因为有时候我们需要修改的只是模板方法中的部分操作而已。
- **缺点：**此模式的维护有时候可能会很麻烦，因为模板方法是固定的，一旦模板方法本身有修改的时候，就可能对其他的相关实现造成影响。



### 使用场景

**使用场景:**当不变和可变的行为在方法的子类实现中混合在一起时,不变的行为就会在子类中重复出现，用模板方法模式把这些不变的行为搬到单一的地方,帮助子类摆脱重复不变的行为纠缠



## 模板方法模式案例

### 钩子

钩子是在基类中声明的方法，并且在模板方法中使用它，通常是给它定义好一个默认的实现，钩子的思想是为子类提供一个按需“钩取”的能力，因此如果子类不想使用钩子，则可以忽略钩子的相关实现。

```python
import abc


class Template(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def operation_1(self):
        pass

    @abc.abstractmethod
    def operation_2(self):
        pass

    def template_func(self):
        self.operation_1()
        self.operation_2()
        print('\n')


class SubObj1(Template):
    """子类1：按需重新定义模板方法中的算法操作"""
    def operation_1(self):
        print("SubObj1.operation_1()")

    def operation_2(self):
        print("SubObj1.operation_2()")


class SubObj2(Template):
    def operation_1(self):
        print("SubObj2.operation_1()")

    def operation_2(self):
        print("SubObj2.operation_2()")


if __name__ == "__main__":
    SubObj1().template_func()
    SubObj2().template_func()
```