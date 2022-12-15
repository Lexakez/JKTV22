class Product:
    def __init__(self):
        self.__name = ''
        self.__price = ''

    '''Установка имени'''
    @property
    
    def name(self):
        return self.__price

    @name.setter

    def name(self, name):
        self.__name = name

    '''Установка цены'''
    @property

    def price(self):
        return self.__price
    
    @price.setter

    def price(self, price):
        if price > 0:
            self.__price = price
        else:
            print("Не правильная цена продукта")

    def print_info(self):
        print(f"Name: {self.__name}\t|\tPrice: {self.__price}")