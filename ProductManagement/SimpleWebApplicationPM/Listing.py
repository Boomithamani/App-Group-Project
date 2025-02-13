class Listing:
    def __init__(self, name, sizing, price, category, picture, id):
        self.__name = name
        self.__sizing = sizing
        self.__price = price
        self.__category = category
        self.__picture = picture
        self.__id = id

    def get_name(self):
        return self.__name

    def get_sizing(self):
        return self.__sizing

    def get_price(self):
        return self.__price

    def get_category(self):
        return self.__category

    def get_picture(self):
        return self.__picture

    def get_id(self):
        return self.__id

    def set_name(self, name):
        self.__name = name

    def set_sizing(self, sizing):
        self.__sizing = sizing

    def set_price(self, price):
        self.__price = price

    def set_category(self, category):
        self.__category = category

    def set_picture(self, picture):
        self.__picture = picture

    def set_id(self, id):
        self.__id = id
