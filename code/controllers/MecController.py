from view.MecView import MecView
from entitys.Mechanic import Mechanic


class MecController():

    def __init__(self, system_controller):
        self.__system_controller = system_controller
        self.__mechanic = []
        self.__mechanic_screen = MecView()