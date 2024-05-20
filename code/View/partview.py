class PartView:

    def __init__(self, PartController)
        self.__partcontroller = PartController

    def le_num_inteiro(self_ mensagem: str = "", inteiros_validos

    : [] = None):
    while True:
        Valor_lido = input(mensagem)

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
        print("1 - Incluir Peça")
        print("2 - Alterar Peça")
        print("3 - Atualizar Peças")
        print("4 - Excluir peça")
        print("0 - Retornar")
        opcao = self.le_num_inteiro("Escolha a opcao:", [1, 2,, 3, 4, 0])
        return opcao




