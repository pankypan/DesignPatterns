from abc import abstractmethod


# 披萨原料基类
class PizzaIngredientFactory(object):
    @abstractmethod
    def choose_dough(self):
        pass

    @abstractmethod
    def choose_sauce(self):
        pass

    @abstractmethod
    def choose_cheese(self):
        pass

    @abstractmethod
    def choose_veggies(self):
        pass

    @abstractmethod
    def choose_clam(self):
        pass


class Dough(object):  # 披萨原料

    def __init__(self, name, shop_name):
        self._name = name
        self._shop_name = shop_name

    def dough_type(self):
        if self._shop_name == 'NY':
            return 'thick crust dough'
        elif self._shop_name == 'Chicago':
            return 'thin crust dough'
        else:
            print('There is no such store.')


class Sauce(object):  # 披萨原料

    def __init__(self, name, shop_name):
        self._name = name
        self._shop_name = shop_name

    def sauce_type(self):
        if self._shop_name == 'NY':
            return 'plum tomato sauce'
        elif self._shop_name == 'Chicago':
            return 'marinara sauce'
        else:
            print('There is no such store.')


class Clams(object):  # 披萨原料

    def __init__(self, name, shop_name):
        self._name = name
        self._shop_name = shop_name

    def clams_type(self):
        if self._shop_name == 'NY':
            return 'frozen clams'
        elif self._shop_name == 'Chicago':
            return 'fresh clams'
        else:
            print('There is no such store.')


class Cheese(object):  # 披萨原料

    def __init__(self, name, shop_name):
        self._name = name
        self._shop_name = shop_name

    def cheese_type(self):
        if self._shop_name == 'NY':
            return 'mozzarella cheese'
        elif self._shop_name == 'Chicago':
            return 'reggiano cheese'
        else:
            print('There is no such store.')


class NYPizzaIngredientFactory(PizzaIngredientFactory):  # 纽约的原料工厂
    def __init__(self, name):
        self._name = name

    def choose_dough(self):
        return Dough('choose_dough', 'NY').dough_type()

    def choose_sauce(self):
        return Sauce('choose_sauce', 'NY').sauce_type()

    def choose_veggies(self):
        veggies = ['garlic', 'onion', 'mushroom']
        return veggies

    def choose_cheese(self):
        return Cheese('choose_cheese', 'NY').cheese_type()

    def choose_clam(self):
        return Clams('choose_clams', 'NY').clams_type()


class ChicagoPizzaIngredientFactory(PizzaIngredientFactory):  # 芝加哥的原料工厂
    def __init__(self, name):
        self._name = name

    def choose_dough(self):
        return Dough('choose_dough', 'Chicago').dough_type()

    def choose_sauce(self):
        return Sauce('choose_sauce', 'Chicago').sauce_type()

    def choose_veggies(self):
        veggies = ['garlic', 'onion', 'mushroom']
        return veggies

    def choose_cheese(self):
        return Cheese('choose_cheese', 'Chicago').cheese_type()

    def choose_clam(self):
        return Clams('choose_clams', 'Chicago').clams_type()


class Pizza(object):  # 披萨基类，获取工厂原料
    @abstractmethod
    def require_ingredient(self):
        pass


class PizzaShop(object):  # 披萨店基类
    @abstractmethod
    def create_pizza(self):
        pass


class PreparePizza(object):  # 披萨准备类
    def bake(self):
        print('Bake for 25min at 350')

    def cut(self):
        print('cutting the pizza into diagonal slices')

    def box(self):
        print('place pizza in official pizza store box')


class CheesePizza(Pizza):  # 芝士披萨

    def __init__(self, name, shop_name):
        self._name = name
        self._shop_name = shop_name

    def require_ingredient(self):
        if self._shop_name == 'NY':
            return NYPizzaIngredientFactory('NY_shop').choose_cheese()
        elif self._shop_name == 'Chicago':
            return ChicagoPizzaIngredientFactory('Chicago_shop').choose_cheese()
        else:
            print('There is no such store.')


class ClamPizza(Pizza):  # 蛤蜊披萨

    def __init__(self, name, shop_name):
        self._name = name
        self._shop_name = shop_name

    def require_ingredient(self):
        if self._shop_name == 'NY':
            return NYPizzaIngredientFactory('NY_shop').choose_clam()
        elif self._shop_name == 'Chicago':
            return ChicagoPizzaIngredientFactory('Chicago_shop').choose_clam()
        else:
            print('There is no such store.')


class NYPizzaStore(PizzaShop):  # 纽约店，披萨在这里制作

    def __init__(self, pizza_name, pizza_shop='NY'):
        self._pizza_shop = pizza_shop
        self._pizza_name = pizza_name

    def create_pizza(self):
        pizza = None
        if self._pizza_name == 'Cheese':
            pizza = CheesePizza('cheese_pizza', self._pizza_shop).require_ingredient()
        elif self._pizza_name == 'Clam':
            pizza = ClamPizza('clam_pizza', self._pizza_shop).require_ingredient()
        PreparePizza().bake()
        PreparePizza().cut()
        PreparePizza().box()
        marked_words = f'the {pizza} pizza is ready'
        return marked_words


# 在纽约披萨店点了份芝士披萨
if __name__ == '__main__':
    cheese_pizza = NYPizzaStore('Cheese').create_pizza()
    print(cheese_pizza)
