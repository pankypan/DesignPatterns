"""
策略模式--应用
author: panky
"""
import abc


class CashSuper(metaclass=abc.ABCMeta):
    """现金收费抽象类"""

    @abc.abstractmethod
    def accept_cash(self, money):
        pass


class CashNormal(CashSuper):
    """正常收费子类"""
    def accept_cash(self, money):
        return money


class CashRebate(CashSuper):
    """打折收费子类"""
    def __init__(self, discount=1.0):
        self.discount = discount

    def accept_cash(self, money):
        return money * self.discount


class CashReturn(CashSuper):
    """返利收费子类"""

    def __init__(self, money_condition=0, money_return=0):
        self.money_condition = money_condition
        self.money_return = money_return

    def accept_cash(self, money):
        if money >= self.money_condition:
            return money - (money / self.money_condition) * self.money_return
        return money


class Context(object):
    """具体策略类"""
    def __init__(self, c_super: CashSuper):
        self.c_super = c_super

    def get_result(self, money):
        return self.c_super.accept_cash(money)


if __name__ == "__main__":
    input_money = input("原价：")
    strategy = dict()
    strategy[1] = Context(CashNormal())
    strategy[2] = Context(CashRebate(0.8))
    strategy[3] = Context(CashReturn(100, 10))
    mode = input("选择折扣方式： 1）原价 2）8折 3）满100减10：")
    if int(mode) in strategy:
        c_s = strategy[int(mode)]
    else:
        print("不存在的折扣方式")
        c_s = strategy[1]
    print("pay: ", c_s.get_result(float(input_money)))
