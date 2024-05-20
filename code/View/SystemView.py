from controllers.ActivityServiceController import AcitivityServiceController
class SystemView:
    def screen_options():
        print("""
========= Bem vindo ao JetEase =========
1- Cliente
2- Mecânico
3- Ordem de serviço
4- Atividade de serviço
0- Sair
""")
        while True:
            try:
                option = int(input('Insira a opção: '))
            except Exception as erro: 
                 print('Opção inválida. Insira opcção contida no menu\n')
            if not option in range(0, 4):
                print('Opção inválida. Insira opcção contida no menu\n')
            else:
                return option
    
    screen_options()