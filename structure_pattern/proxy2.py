"""
代理模式
author: panky
"""
import abc


class GiveGift(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def give_dolls(self):
        pass

    @abc.abstractmethod
    def give_flowers(self):
        pass

    @abc.abstractmethod
    def give_chocolate(self):
        pass


class SchoolGirl:
    def __init__(self, name):
        self.name = name


class Pursuit(GiveGift):
    def __init__(self, mm: SchoolGirl):
        self.mm = mm

    def give_dolls(self):
        print(self.mm.name, "送你洋娃娃")

    def give_flowers(self):
        print(self.mm.name, "送你鲜花")

    def give_chocolate(self):
        print(self.mm.name, "送你巧克力")


class Proxy(GiveGift):
    def __init__(self, mm: SchoolGirl):
        self.gg = Pursuit(mm)

    def give_dolls(self):
        self.gg.give_dolls()

    def give_flowers(self):
        self.gg.give_flowers()

    def give_chocolate(self):
        self.gg.give_chocolate()


if __name__ == "__main__":
    jiao_jiao = SchoolGirl("Li jiao jiao")

    proxy = Proxy(jiao_jiao)
    proxy.give_flowers()
    proxy.give_dolls()
    proxy.give_chocolate()
