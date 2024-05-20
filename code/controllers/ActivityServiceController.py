from entitys.ActivityService import ActivityService
from view.ActivityServiceView import ActivityServiceView


class AcitivityServiceController():

    def __init__(self, system_controller):
        self.__system_controller = system_controller
        self.__activity_service = []
        self.__activity_screen = ActivityServiceView()

    def __str__(self):
        return f"""ID da atividade de serviço: {self.id_activity}
                    Jetski: {self.jetski}
                    Descrição do serviço: {self.desc_service}
                    Custo estimado: {self.estimated_cost}
                    Custo final: {self.real_cost}
                    Data de conclusão: {self.conc_date}
        """