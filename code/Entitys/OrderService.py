from entitys.ActivityService import ActivityService


class OrderService:

    def __init__(self, id_order: int, dt_entry, estimated_de_dt, dt_exit, state_order: str, obs_order: str,
                 or_service_cost: float):
        if isinstance(id_order, int):
            self.__id_order = id_order
        if isinstance(state_order, str):
            self.__state_order = state_order
        if isinstance(obs_order, str):
            self.__obs_order = obs_order
        if isinstance(or_service_cost, float):
            self.__or_service_cost = or_service_cost
        self.__dt_entry = dt_entry
        self.__estimated_de_dt = estimated_de_dt
        self.__dt_exit = dt_exit
        self.__activities_os = []

    @property
    def id_oder(self):
        return self.__id_order

    @property
    def dt_entry(self):
        return self.__dt_entry

    @property
    def estimated_de_dt(self):
        return self.__estimated_de_dt

    @property
    def dt_exit(self):
        return self.__dt_exit

    @property
    def state_order(self):
        return self.__state_order

    @property
    def obs_order(self):
        return self.__obs_order

    @property
    def or_service_cost(self):
        return self.__or_service_cost

    @property
    def acitivity_os(self):
        return self.__activity_os

    @id_oder.setter
    def id_order(self, id_order):
        self.__id_order = id_order

    @dt_entry.setter
    def dt_entry(self, dt_entry):
        self.__dt_entry = dt_entry

    @estimated_de_dt.setter
    def estimated_de_dt(self, estimated_de_dt):
        self.__estimated_de_dt = estimated_de_dt

    @dt_exit.setter
    def dt_exit(self, dt_exit):
        self.__dt_exit = dt_exit

    @state_order.setter
    def state_order(self, state_order):
        self.__state_order = state_order

    @obs_order.setter
    def obs_order(self, obs_order):
        self.__obs_order = obs_order

    @or_service_cost.setter
    def or_service_cost(self, or_service_cost):
        self.__or_service_cost = or_service_cost

    def add_activity_os(self, id_activity, desc_service, estimated_cost, real_cost, conc_date, jetski):
        activity_service = ActivityService(id_activity, desc_service, estimated_cost, real_cost, conc_date, jetski)
        self.__activities_os.append(activity_service)

    def list_activities(self):
        for activity_os in self.__activities_os:
            print(activity_os)