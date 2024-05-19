class ActivityService:
    
    def __init__(self, id_activity, desc_service, estimated_cost, real_cost, conc_date):
        self.__id_activity = id_activity
        self.__desc_service = desc_service
        self.__estimated_cost = estimated_cost
        self.__real_cost = real_cost
        self.__conc_date = conc_date


    @property
    def id_activity(self):
        return self.__id_activity
    

    @property
    def desc_service(self):
        return self.__desc_service
    

    @property
    def estimated_cost(self):
        return self.__estimated_cost
    

    @property
    def real_cost(self):
        return self.__real_cost


    @property
    def conc_date(self):
        return self.conc_date
    

    @id_activity.setter
    def id_activity(self, id_activity):
        self.__id_activity = id_activity
    

    @desc_service.setter
    def desc_service(self, desc_service):
        self.__desc_service