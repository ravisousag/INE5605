import PySimpleGUI as sg

class SystemView:
    def __init__(self):
        self.__window = None
        self.init_components()
        
        
        
    def screen_options(self):
        while True:
            self.init_components()
            button, values = self.__window.read()
            
            self.close()
            print(button)
            return button
            
                      
    def close(self):
        self.__window.Close()
                     
    
    def init_components(self):
        sg.ChangeLookAndFeel('Dark')
        layout = [
            [sg.Text('Bem vindo ao sistema!', font=("Helvica",25))],
            [sg.Text('Escolha sua opção', font=("Helvica",15))],
            [sg.Button('Cliene', key=1)],
            [sg.Button('Mecânico', key=2)],
            [sg.Button('Ordem de serviço', key=3)],
            [sg.Button('Atividade de serviço', key=4)],
            [sg.Cancel('Cancelar',button_color='red', key=5)]     
        ]
        self.__window = sg.Window('Sistema mêcanica').Layout(layout)
        