import abc
from copy import copy, deepcopy


class Prototype(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def clone(self):
        pass

    @abc.abstractmethod
    def deep_clone(self):
        pass


# 工作经历类
class WorkExperience(object):
    def __init__(self):
        self._time_area = ''
        self._company = ''

    def set_work_experience(self, time_area, company):
        self._time_area = time_area
        self._company = company

    @property
    def time_area(self):
        return self._time_area

    @property
    def company(self):
        return self._company


# 简历类
class Resume(Prototype):
    def __init__(self, name):
        self._name = name
        self._sex = None
        self._age = None
        self._work_experience = WorkExperience()

    def set_person_info(self, sex: str, age: int):
        self._sex = sex
        self._age = age

    def set_work_experience(self, time_area: str, company: str):
        self._work_experience.set_work_experience(time_area, company)

    def display(self):
        print(self._name)
        print(self._sex, self._age)
        print('工作经历：', self._work_experience.time_area, self._work_experience.company)

    def clone(self):
        return copy(self)

    def deep_clone(self):
        return deepcopy(self)


if __name__ == '__main__':
    obj1 = Resume('panky')
    obj2 = obj1.clone()
    obj3 = obj1.deep_clone()

    print(obj1, obj2, obj3)

    obj1.set_person_info('man', 27)
    obj1.set_work_experience('2016-2020', 'GZ')

    obj2.set_person_info('man', 28)
    obj2.set_work_experience('2017-2018', 'HM')

    obj3.set_person_info('man', 29)
    obj3.set_work_experience('2020-2021', 'HW')

    obj1.display()
    obj2.display()
    obj3.display()
