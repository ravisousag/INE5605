from mechanic import Mechanic
from viewmechanic import ViewMechanic

class Controller_mechanic:

    def__init__(self):
        self.__view_mechanic = Viewmechanic(self)
        self.__mechanic = []
    
    def inicia(self)
        self.abre_tela_inicia()

    def inclui_mechanic(self):
        Mechanic = self.busca_mechanic_pelo_id(mechanic.id)
        if not mechanic:
            self.__mechanic.append(Mechanic)
    
    def alterar_mechanic(self):

    def exclui_mechanic(self):
        if mechanic in self.__mechanic:
            self.__mechanic.remove(mechanic)

    def lista_mechanic(self):

    def finalizar(self):
        exit(0)

    def abre_tela_inicial (self):
        switcher = {0: self.finalizar, 1:self.inclui_mechanic, 2:self.alterar_mechanic, 3:self.exclui_mechanic, 4:self.lista_mechanic}

        while True:
            opcao = self.__view_mechanic.mostra_tela_opcoes()
            funcao_escolhida = switcher[opcao]
            funcao_escolhida ()


    
   