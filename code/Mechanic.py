from User import User


class Mechanic(User):


    def __init__(self, id_mec, registration):

        self.__id_mec = id_mec
        self.__registration = registration

    @property
    def id_mec(self):
        return self.__id_mec
    
    
    @id_mec.setter
    def id_mec(self, id_mec):
        self.__id_mec = id_mec
    

    @property
    def registration(self):
        return self.__registration
    

    @registration.setter
    def registration(self, registration):
        self.__registration = registration
    