class Part:
    

    def __init__(self, id_part, part_name, part_desc, unity_price, qt_stock, brand):
        self.__id_part = id_part
        self.__part_name = part_name
        self.__part_desc = part_desc
        self.__unity_price = unity_price
        self.__qt_stock = qt_stock
        self.__brand = brand


    @property
    def id_part(self):
        return self.__id_part
    

    @property
    def part_name(self):
        return self.__part_name
    

    @property
    def part_desc(self):
        return self.__part_desc
    

    @property
    def unity_price(self):
        return self.__unity_price
    

    @property
    def qt_stock(self):
        return self.__qt_stock
    

    @property
    def brand(self):
        return self.__brand
    

    @id_part.setter
    def id_part(self, id_part):
        self.__id_part = id_part


    @part_name.setter
    def part_name(self, part_name):
        self.__part_name = part_name
    

    @part_desc.setter
    def part_desc(self, part_desc):
        self.__part_desc = part_desc
    

    @unity_price.setter
    def unity_price(self, unity_price):
        self.__unity_price = unity_price
    

    @qt_stock.setter
    def qt_stock(self, qt_stock):
        self.__qt_stock = qt_stock
    

    @brand.setter
    def brand(self, brand):
        self.__brand = brand