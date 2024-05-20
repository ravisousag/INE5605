from view.MecView import MecView
from entitys.Mechanic import Mechanic


class MecController():

    def __init__(self, system_controller):
        self.__system_controller = system_controller
        self.__mechanic = []
        self.__mechanic_screen = MecView()
        
    
    def get_mec_regis(self, regis: int):
        for mec in self.__mechanic:
            if(mec.regis == regis):
                return mec
        return None
    
    def get_mec_cpf(self, cpf: str):
        for mec in self.__mechanic:
            if(mec.cpf == cpf):
                return mec
        return None
    
    
    def insert_mec(self):
        data_mec = self.__mechanic_screen.get_mec_data()
        new_mec = Mechanic(data_mec['name'],data_mec['cpf'], data_mec['zip'],data_mec['username'], data_mec['password'],data_mec['registration'])
        # mec = self.get_mec_regis(mec['regis'])
        
        self.__mechanic.append(new_mec)
        self.__mechanic_screen.msg('\nMecânico cadastraado com sucesso\n')
    
    def list_mec(self):
        for mec in self.__mechanic:
            if(mec is not None):
                self.__mechanic_screen.show_mec({'registration': mec.registration, 'name': mec.name, 'cpf': mec.cpf, 'zip': mec.zip, 'username': mec.username, 'password': mec.password})
            else:
                self.__mechanic_screen.msg('Não há mecânico cadastrado')
                
    
    def alter_mec(self):
        self.list_mec()
        cpf_mec = self.__mechanic_screen.valid_cpf()
        mec = self.get_mec_cpf(cpf_mec)
        
        if(mec is not None):
            new_data_mec = self.__mechanic_screen.get_mec_data()
            mec.registration = new_data_mec['registration']
            mec.name = new_data_mec['name']
            mec.cpf = new_data_mec['cpf']
            mec.zip = new_data_mec['zip']
            mec.username = new_data_mec['username']
            mec.password = new_data_mec['password']
        else:
            self.__mechanic_screen.msg('Mecânico inexistente\n')
            
    
    def delete_mec(self):
        self.list_mec()
        cpf_mec = self.__mechanic_screen.valid_cpf()
        mec = self.get_mec_cpf(cpf_mec)
        
        if (mec is not None):
            self.__mechanic.remove(mec)
            self.list_mec()
        else:
            self.__mechanic_screen.msg('Mecânico inexistente\n')
            self.open_screen()
            
    def go_back(self):
        self.__system_controller.open_screen()
        
        
    
    def open_screen(self):
        options = {1: self.insert_mec, 2: self.alter_mec, 3: self.delete_mec,
                   4: self.list_mec,
                   5: self.go_back}
        
        while True:
            choose_option = self.__mechanic_screen.screen_options()
            func_choose = options[choose_option]
            func_choose()