from view.ClientView import ClientView
from entitys.Client import Client

class ClientController():
    
    def __init__(self, system_controller):
        self.__system_controller = system_controller
        self.__client = []
        self.__client_screen = ClientView()