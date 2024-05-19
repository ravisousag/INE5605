class InventoryItem:
    

    def __init__(self, id_part, part_name, part_desc, qt_stock, id_inventory):
        self.__id_part = id_part
        self.__part_name = part_name
        self.__part_desc = part_desc
        self.__qt_stock = qt_stock
        self.__id_inventory = id_inventory


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
    def qt_stock(self):
        return self.__qt_stock
    

    @property
    def id_inventory(self):
        return self.__id_inventory
    

    @id_part.setter
    def id_part(self, id_part):
        self.__id_part = id_part


    @part_name.setter
    def part_name(self, part_name):
        self.__part_name = part_name
    

    @part_desc.setter
    def part_desc(self, part_desc):
        self.__part_desc = part_desc
    

    @qt_stock.setter
    def qt_stock(self, qt_stock):
        self.__qt_stock = qt_stock
    

    @id_inventory.setter
    def id_inventory(self, id_inventory):
        self.__id_inventory = id_inventory