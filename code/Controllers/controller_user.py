from user import User
from viewuser import ViewUser

class Controller_user:

    def__init__(self):
        self.__view_user = ViewUser(self)
        self.__user = []
    
    def inicia(self)
        self.abre_tela_inicia()

    def inclui_user(self):
        User = self.busca_user_pelo_cpf(user.cpf)
        if not user:
            self.__user.append(User)
    
    def alterar_user(self):

    def exclui_user(self):
        if user in self.__user:
            self.__user.remove(user)

    def lista_user(self):

    def finalizar(self):
        exit(0)

    def abre_tela_inicial (self):
        switcher = {0: self.finalizar, 1:self.inclui_user, 2:self.alterar_user, 3:self.exclui_user, 4:self.lista_user}

        while True:
            opcao = self.__view_user.mostra_tela_opcoes()
            funcao_escolhida = switcher[opcao]
            funcao_escolhida ()


    
   