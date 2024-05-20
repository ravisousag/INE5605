
class SystemView:
    def screen_options(self):
        print("""
========= Bem vindo ao JetEase =========
1- Cliente
2- Mecânico
3- Ordem de serviço
4- Atividade de serviço
5- Sair
""")
        while True:
            try:
                option = int(input('Insira a opção: '))
                if option in range(1, 6):
                    return option
            except Exception as erro: 
                 print('Opção inválida. Insira opcção contida no menu\n')