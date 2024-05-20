
from validate_docbr import CPF


class MecView:

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


    def get_mec_data(self):
        print('====== Insira dados Mecânico ======')
        name = str(input('Nome: '))
        cpf = self.valid_cpf()                  
        zip = int(input('CEP: '))
        username = str(input('Usuário: '))
        password = str(input('Senha: '))
        registration = int(input('Matricula: '))
        
        return {'name': name, 'cpf': cpf, 'zip': zip, 'username': username, 'password': password, 'registration': registration}


    def show_mec(self, data_mec):
        print(f"""
              Matrícula: {data_mec['registration']}
              Nome: {data_mec['name']}
              CPF: {data_mec['cpf']}
              CEP: {data_mec['zip']}
              Usuário: {data_mec['username']}
              Senha: {data_mec['password']}
              
              """)
       
            
    def valid_cpf(self):
        is_cpf = False
        while is_cpf == False:
            cpf = str(input('CPF: '))
            verify_cpf = CPF()
            if verify_cpf.validate(cpf) is False:
                print('CPF inválido\n')
                is_cpf = verify_cpf.validate(cpf)
            else:
                is_cpf = verify_cpf.validate(cpf)
                return cpf
    
    
    def msg(self, msg):
        print(msg)