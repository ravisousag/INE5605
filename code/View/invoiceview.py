
class InvoiceView:

    def __init__(self, InvoiceController)
        self.__invoicecontroller = InvoiceControllerController

    def le_num_inteiro(self_ mensagem: str = "", inteiros_validos: [] = None):
while True:
    Valor_lido = input (mensagem)

try:
    inteiro: = int(valor_lido)
    if inteiros_validos and inteiro not in inteiros_validos:
        raise ValueError
    return inteiro 
except ValueError:
    print("Valor incorreto: Digite um valor numerico inteiro valido")
    if inteiros_validos:
        print("Valor validos:", inteiros_validos)

def mostra_tela_opcoes(self):
    print("----------Part----------")
    print("----Escolha uma ooção----")
    print("1 - Incluir Fatura")
    print("2 - Alterar Fatura")
    print("3 - Relatório de faturamento")
    print("4 - Excluir Fatura")
    print("0 - Retornar")
    opcao = self.le_num_inteiro("Escolha a opcao:", [1, 2, , 3, 4, 5, 0])
    return opcao

    


    