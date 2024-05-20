class MecView():

    def screen_options(self):
        print("""
              ====== Tela Mecânico ======
              1- Incluir mecânico
              2- Editar mecânico
              3- Excluir mecânico
              4- Listar mecânicos
              5- Retornar ao menu anterior
              """)
        option = int(input("Escolha a opção: "))
        return option

