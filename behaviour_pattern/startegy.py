"""
策略模式
author: panky
"""
import abc


# 抽象算法类
class Strategy(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def algorithm_interface(self):
        pass


# 具体算法 A
class ConcreteStrategyA(Strategy):
    def algorithm_interface(self):
        print("算法 A 实现")


# 具体算法 A
class ConcreteStrategyB(Strategy):
    def algorithm_interface(self):
        print("算法 B 实现")


# 具体算法 C
class ConcreteStrategyC(Strategy):
    def algorithm_interface(self):
        print("算法 C 实现")


class Context:
    def __init__(self, strategy: Strategy):  # 初始化时，传入具体的策略对象
        self.strategy = strategy

    def context_interface(self):  # 根据具体的策略对象，调用其算法方法
        self.strategy.algorithm_interface()


if __name__ == "__main__":
    context = Context(ConcreteStrategyA())
    context.context_interface()

    context = Context(ConcreteStrategyB())
    context.context_interface()

    context = Context(ConcreteStrategyC())
    context.context_interface()
