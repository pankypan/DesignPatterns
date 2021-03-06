# 设计模式python实现(02)--单例模式

## 简单的单例模式

```python
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
```





## 多线程版的单例模式

```python
import threading


def make_synchronized(func):
    if not hasattr(func, '__lock__'):
        func.__lock__ = threading.Lock()

    def wrapper(*args, **kwargs):
        with func.__lock__:
            return func(*args, **kwargs)
    return wrapper


class Singleton(object):
    __instance = None

    @make_synchronized
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            # 实现单例的关键点,对象空间创建的复用
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def go(self, name: str):
        print(self, name + ' go!')


def worker(name: str):
    s = Singleton()
    s.go(name)


if __name__ == '__main__':
    tasks = list()

    for i in range(100):
        t = threading.Thread(target=worker, args=(str(i),))
        tasks.append(t)

    for t in tasks:
        t.start()
    for t in tasks:
        t.join()

```

