class ActivityServiceView():
        
        
    def search_activity(self):
        print(""""

========= Atividades de serviço =========
1- Buscar atividade de serviço
2- Editar atividade de serviço
3- Excluir atividade de serviço
4- Retornar
              
              """)
        while True:
            try:
                option = int(input('Insira a opção: '))
                if option in range(1, 4):
                    return option
            except Exception as erro: 
                 print('Opção inválida. Insira opcção contida no menu\n')

