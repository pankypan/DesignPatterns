class Singleton(object):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            # 实现单例的关键点,对象空间创建的复用
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, flag: int):
        self.flag = flag


if __name__ == '__main__':
    s1 = Singleton(1)
    s2 = Singleton(2)
    print(s1, s2)
    print(s1.flag, s2.flag)
