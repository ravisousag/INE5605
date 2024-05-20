from entitys.OrderService import OrderService
from view.OrderServiceView import OrderServiceView


class OrderServiceController():

    def __init__(self, system_controller):
        self.__system_controller = system_controller
        self.__order_service = []
        self.__os_screen = OrderServiceView()