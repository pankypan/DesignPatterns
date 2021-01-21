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
