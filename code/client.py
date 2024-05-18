from User import User

class Client(User):

    
    def __init__(self, id_client, cellphone, email):
        self.__id_client = id_client
        self.__cellphone = cellphone
        self.__email = email

    
    @property
    def id_client(self):
        return self.__id_client
    

    @id_client.setter
    def id_client(self, id_client):
        self.__id_client = id_client

    
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