from entitys.invetoryitem import InventoryItem:
from transactionitem import TransactionItem:

def__init__(self):
        self.__inventoryitemview = InventoryItemView(self)
        self.__inventory = []
    
    def inicia(self)
        self.abre_tela_inicia()
      
   def lista_part(self):
        return self.__inventory

    def finalizar(self):
        exit(0)

    def abre_tela_inicial (self):
        switcher = {0: self.finalizar, 1:self.lista_part}

        while True:
            opcao = self.__view_client.mostra_tela_opcoes()
            funcao_escolhida = switcher[opcao]
            funcao_escolhida ()


