class Sale:
    count_id = 0

    def __init__(self, item_name, category, quantity_sold, unit_price):
        Sale.count_id += 1
        self.__sale_id = Sale.count_id
        self.__item_name = item_name
        self.__category = category
        self.__quantity_sold = quantity_sold
        self.__unit_price = unit_price
        self.__total_price = quantity_sold * unit_price

    def get_sale_id(self):
        return self.__sale_id

    def get_item_name(self):
        return self.__item_name

    def get_category(self):
        return self.__category

    def get_quantity_sold(self):
        return self.__quantity_sold

    def get_unit_price(self):
        return self.__unit_price

    def get_total_price(self):
        return self.__total_price


    def set_sale_id(self, sale_id):
        self.__sale_id = sale_id

    def set_item_name(self, item_name):
        self.__item_name = item_name

    def set_category(self, category):
        self.__category = category

    def set_quantity_sold(self, quantity_sold):
        self.__quantity_sold = quantity_sold

    def set_unit_price(self, unit_price):
        self.__unit_price = unit_price

    def set_total_price(self, total_price):
        self.__total_price = total_price