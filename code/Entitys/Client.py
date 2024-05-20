from User import User

class Client(User):


    def __init__(self, name: str, cpf: str, zip: int, username: str, password: str, cellphone: int, email: str):
        super().__init__(name, cpf, zip, username, password)
        if (isinstance(cellphone, int)):
            self.__cellphone = cellphone
        if (isinstance(email, str)):
            self.__email = email

    
    @property
    def cellphone(self):
        return self.__cellphone
    

    @cellphone.setter
    def cellphone(self, cellphone):
        self.__cellphone = cellphone


    @property
    def email(self):
        return self.__email
    

    @email.setter
    def email(self, email):
        self.__email = email