"""
代理模式
author: panky
"""
import abc


# Subject 类，定义了 RealSubject 和 Proxy 的共用接口
class Subject(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def request(self):
        pass


# RealSubject 类，定义了 Proxy 所代表的真实实体
class RealSubject(Subject):
    def request(self):
        print("真实的请求", self)


# Proxy类，保存一个引用使得代理可以访问实体，并提供一个与 Subject 的接口相同的接口，这样代理可以用来代替实体
class Proxy(Subject):
    def __init__(self, real_subject: RealSubject = None):
        self.real_subject = real_subject

    def request(self):
        if self.real_subject is None:
            self.real_subject = RealSubject()

        self.real_subject.request()

    def reset_real_subject(self, real_subject: RealSubject):
        self.real_subject = real_subject


if __name__ == "__main__":
    proxy = Proxy()
    proxy.request()

    aa = RealSubject()
    proxy.reset_real_subject(aa)
    proxy.request()
