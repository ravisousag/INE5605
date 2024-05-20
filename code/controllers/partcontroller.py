from Entitys.part import Part
from view.partview import PartView

class PartController:

    def__init__(self):
        self.__view_part = PartView(self)
        self.__part = []
    
    def inicia(self)
        self.abre_tela_inicia()

    def inclui_part(self):
        Client = self.busca_peça_pelo_id(part.id)
        if not Part:
            self.__part.append(Part)
    
    def exclui_part(self):
        if part in self.__part:
            self.__part.remove(part)

    def lista_part(self):
        return self.__part

    def finalizar(self):
        exit(0)

    def abre_tela_inicial (self):
        switcher = {0: self.finalizar, 1:self.inclui_part, 2:self.exclui_part, 3:self.lista_part}

        while True:
            opcao = self.__view_part.mostra_tela_opcoes()
            funcao_escolhida = switcher[opcao]
            funcao_escolhida ()


    
   