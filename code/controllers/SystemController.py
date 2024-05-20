from controllers.ActivityServiceController import AcitivityServiceController
from controllers.ClientController import ClientController
from controllers.MecController import MecController
from controllers.OrderServiceController import OrderServiceController
from controllers.UserController import UserController
from view.SystemView import SystemView


class SystemController:

    def __init__(self):
        self.__user_controller = UserController(self)
        self.__client_controller = ClientController(self)
        self.__mechanic_controller = MecController(self)
        self.__ac_service_controller = AcitivityServiceController(self)
        self.__os_controller = OrderServiceController(self)
        self.__system_screen = SystemView()

    @property
    def user_controller(self):
        return self.__user_controller

    @property
    def client_controller(self):
        return self.__client_controller

    @property
    def mechanic_controller(self):
        return self.__mechanic_controller

    @property
    def ac_service_controller(self):
        return self.__ac_service_controller

    @property
    def os_controller(self):
        return self.__os_controller

    def start_system(self):
        self.open_screen()

    def insert_client(self):
        self.__client_controller.open_screen()

    def insert_mechanic(self):
        self.__mechanic_controller.open_screen()

    def insert_order_service(self):
        self.__os_controller.open_screen()

    def insert_ac_service(self):
        self.__ac_service_controller.open_screen()

    def close_system(self):
        print('Sistema encerrado!')
        exit(5)

    def open_screen(self):
        options = {1: self.insert_client, 2: self.insert_mechanic, 3: self.insert_order_service,
                   4: self.insert_ac_service,
                   5: self.close_system}

        while True:
            choose_option = self.__system_screen.screen_options()
            func_choose = options[choose_option]
            func_choose()
