from entitys.Jetski import Jetski
from entitys.Mechanic import Mechanic

class ActivityService:
    
    def __init__(self, id_activity: int, desc_service: str, estimated_cost: float, real_cost: float, conc_date, jetski: Jetski):
        if (isinstance(id_activity,int)):
            self.__id_activity = id_activity
        if (isinstance(desc_service, str)):
            self.__desc_service = desc_service
        if (isinstance(estimated_cost, float)):
            self.__estimated_cost = estimated_cost
        if (isinstance(real_cost, float)):
            self.__real_cost = real_cost
        if (isinstance(jetski, Jetski)):
            self.__jetski = jetski  
        self.__mechanics = []
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
        return self.__conc_date
    
    @property
    def jetski(self):
        return self.__jetski
    
    
    @property
    def mechanics(self):
        return self.__mechanics
    
    
    @id_activity.setter
    def id_activity(self, id_activity):
        self.__id_activity = id_activity
    

    @desc_service.setter
    def desc_service(self, desc_service):
        self.__desc_service = desc_service
        
    
    @conc_date.setter
    def conc_date(self, conc_date):
        self.__conc_date = conc_date
    
    
    @jetski.setter
    def jetski(self, jetski):
        self.__jetski = jetski
        
    
    @mechanics.setter
    def mechanics(self, mechanics):
        self.__mechanics = mechanics