from entitys.User import User
from view.UserView import UserView


class UserController():
    
    
    def __init__(self, system_controller):
        self.__system_controller = system_controller
        self.__user = []
        self.__user_screen = UserView()