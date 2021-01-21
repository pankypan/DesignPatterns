"""
简单工厂模式
author: panky
"""
import abc  # 利用abc模块实现抽象类


class Operation(metaclass=abc.ABCMeta):
    def __init__(self, number_a, number_b):
        self._numberA = number_a
        self._numberB = number_b

    @abc.abstractmethod  # 定义抽象方法，无需实现功能, 由子类实现具体功能
    def get_result(self):
        pass


class OperationAdd(Operation):
    def get_result(self):
        return self._numberA + self._numberB


class OperationSub(Operation):
    def get_result(self):
        return self._numberA - self._numberB


class OperationMul(Operation):
    def get_result(self):
        return self._numberA * self._numberB


class OperationDiv(Operation):
    def get_result(self):
        try:
            return self._numberA / self._numberB
        except ZeroDivisionError:
            print("Divide by zero!")
            return 0


class OperationFactory(object):
    operation_map = {
        '+': OperationAdd,
        '-': OperationSub,
        '*': OperationMul,
        '/': OperationDiv
    }

    def creat_operation(self, op: str, num_a, num_b):
        operation_class = self.operation_map.get(op)
        if operation_class:
            operation = operation_class(num_a, num_b)
            return operation
        else:
            raise Exception("非法操作")


if __name__ == '__main__':
    while True:
        raw_str = input("输入算式：").strip()
        if raw_str == 'Q':
            break
        a, opr, b = raw_str.split(' ')
        factory = OperationFactory()
        opr_obj = factory.creat_operation(opr, int(a), int(b))
        res = opr_obj.get_result()
        print(res)
