"""
装饰模式
author: panky
装饰模式是利用 set_component() 来对对象进行包装的，这样每个装饰对象的实现就和
如何使用这个对象分离开了，每个装饰对象只关心自己的功能，不需要关心如何被添加到
对象链中。
"""
import abc


class Component(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def operation(self):
        pass


class ConcreteComponent(Component):
    def operation(self):
        print("具体对象的操作！")


class Decorator(Component, metaclass=abc.ABCMeta):
    def __init__(self, component: Component = None):
        self.component = component

    def set_component(self, component: Component):
        """
        设置 Component，
        利用 set_component() 来对对象进行包装的
        :param component:
        :return:
        """
        self.component = component

    def operation(self):
        """
        重写 operation() ，实际执行的是 Component 的 operation()
        :return:
        """
        if self.component is not None:
            self.component.operation()


class ConcreteDecoratorA(Decorator):
    def __init__(self, added_state: str = None):
        super().__init__()
        self.added_state = added_state  # 本类对象独有属性

    def operation(self):
        """
        首先运行原 Component 的 operation(), 再执行本类的功能，如对 added_state 赋值，相当于
        对原来的 Component 进行了装饰
        :return:
        """
        super().operation()
        self.added_state = "New State"
        print("具体装饰对象A的操作")


class ConcreteDecoratorB(Decorator):
    @staticmethod
    def added_behavior():  # 本类独有方法
        print("具体装饰对象B增加方法 added_behavior")

    def operation(self):
        """
        首先运行原 Component 的 operation(), 再执行本类的功能，如执行 added_behavior() 方法，相当于
        对原来的 Component 进行了装饰
        :return:
        """
        super().operation()
        self.added_behavior()
        print("具体装饰对象B的操作")


if __name__ == "__main__":
    c = ConcreteComponent()
    d1 = ConcreteDecoratorA()
    d2 = ConcreteDecoratorB()

    d1.set_component(c)
    d1.operation()
    print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-")
    d2.set_component(d1)
    d2.operation()
