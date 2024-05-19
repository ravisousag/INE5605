class ViewUser:

    def __init__(self, controller_user)
        self.__controller_user = controller_user

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
    print("----------USER----------")
    print("----Escolha uma ooção----")
    print("1 - Incluir usuário")
    print("2 - Alterar Usuário")
    print("3 - Listar Usuário")
    print("4 - Excluir Usuário")
    print("0 - Retornar")
    opcao = self.le_num_inteiro("Escolha a opcao:", [1, 2, , 3, 4, 0])
    return opcao

    


    