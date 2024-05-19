class User:
    

    def __init__(self, id_user, name, cpf, zip, username, password):
        self.__id_user = id_user
        self.__name = name
        self.__cpf = cpf
        self.__zip = zip
        self.__username = username
        self.__password = password


    @property
    def id_user(self):
        return self.__id_user
    

    @id_user.setter
    def id_user(self, id_user):
        self.__id_user = id_user


    @property
    def name(self):
        return self.__name
    

    @name.setter
    def name(self, name):
        self.__name = name

    
    @property
    def cpf(self):
        return self.__cpf
    

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf


    @property
    def zip(self):
        return self.__zip
    

    @zip.setter
    def zip(self, zip):
        self.__zip = zip

    
    @property
    def username(self):
        return self.__username
    

    @username.setter
    def username(self, username):
        self.__username = username

    
    @property
    def password(self):
        return self.__password
    

    @password.setter
    def password(self, password):
        self.__password = password
    