class Invoice:


    def __init__(self, id_payment: int, value: float, dt_payment, pay_method: str):
        if (isinstance(id_payment, int)):
            self.__id_payment = id_payment
        if (isinstance(value, float)):
            self.__value = value
        if (isinstance(pay_method, str)):
            self.__payment_method = pay_method
        self.__dt_payment = dt_payment
    

    @property
    def id_payment(self):
        return self.__id_payment
    

    @property
    def value(self):
        return self.__value
    

    @property
    def dt_payment(self):
        return self.__dt_payment
    

    @property
    def pay_method(self):
        return self.__payment_method
    

    @id_payment.setter
    def id_payment(self, id_payment):
        self.__id_payment = id_payment
    

    @value.setter
    def value(self, valeu):
        self.__value = valeu
    

    @dt_payment.setter
    def dt_payment(self, dt_payment):
        self.__dt_payment = dt_payment
    

    @pay_method.setter
    def pay_method(self, pay_method):
        self.__payment_method = pay_method