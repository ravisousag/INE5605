from abc import ABC, abstractmethod


class User(ABC):

    @abstractmethod
    def __init__(self, name: str, cpf: str, zip: int, username: str, password: str):
        if isinstance(name, str):
            self.__name = name
        if isinstance(cpf, str):
            self.__cpf = cpf
        if isinstance(zip, int):
            self.__zip = zip
        if isinstance(username, str):
            self.__username = username
        if isinstance(password, str):
            self.__password = password

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
