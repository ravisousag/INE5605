from entitys.User import User


class Mechanic(User):

    def __init__(self, name: str, cpf: str, zip: int, username: str, password: str, registration: int):
        super().__init__(name, cpf, zip, username, password)
        if isinstance(registration, int):
            self.__registration = registration

    @property
    def registration(self):
        return self.__registration

    @registration.setter
    def registration(self, registration):
        self.__registration = registration
