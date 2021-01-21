"""
装饰模式--应用
author: panky
"""
import abc


# Person类(ConcreteComponent)
class Person:
    def __init__(self, name: str = None):
        self.name = name

    def show(self):
        print(f"\033[32m装扮的{self.name}\033[0m!")


# 服饰类(Decorator)
class Finery(Person, metaclass=abc.ABCMeta):
    def __init__(self, component: Person = None):
        super().__init__()
        self.component = component

    def decorate(self, component):
        self.component = component

    @abc.abstractmethod
    def show(self):
        if self.component is not None:
            self.component.show()


# 具体服饰类(ConcreteDecorator)
class TShirts(Finery):
    def show(self):
        print("TShirts")
        super().show()


class BigTrouser(Finery):
    def show(self):
        print("垮裤")
        super().show()


class Tie(Finery):
    def show(self):
        print("领带")
        super().show()


class Suit(Finery):
    def show(self):
        print("西装")
        super().show()


class LeatherShoes(Finery):
    def show(self):
        print("皮鞋")
        super().show()


class Sneakers(Finery):
    def show(self):
        print("运动鞋")
        super().show()


if __name__ == "__main__":
    p1 = Person("suki")
    print("\n第一种装扮：")
    t = TShirts()
    b = BigTrouser()
    ls = LeatherShoes()

    # 装饰过程
    t.decorate(p1)
    b.decorate(t)
    ls.decorate(b)
    ls.show()

    print("\n第二种装扮：")
    px = LeatherShoes()
    ld = Tie()
    xz = Suit()

    # 装扮过程
    px.decorate(p1)
    ld.decorate(px)
    xz.decorate(ld)
    xz.show()
