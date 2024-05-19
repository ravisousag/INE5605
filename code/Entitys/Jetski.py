class Jetski:
    def __init__(self, id_jetski, brand, model, jet_year, serial_number, propulsion_type, jet_obs):
        self._id_jetski = id_jetski
        self._brand = brand
        self._model = model
        self._jet_year = jet_year
        self._serial_number = serial_number
        self._propulsion_type = propulsion_type
        self._jet_obs = jet_obs


    @property
    def id_jetski(self):
        return self._id_jetski


    @id_jetski.setter
    def id_jetski(self, value):
        self._id_jetski = value


    @property
    def brand(self):
        return self._brand
    

    @brand.setter
    def brand(self, value):
        self._brand = value


    @property
    def model(self):
        return self._model


    @model.setter
    def model(self, value):
        self._model = value


    @property
    def jet_year(self):
        return self._jet_year


    @jet_year.setter
    def jet_year(self, value):
        self._jet_year = value


    @property
    def serial_number(self):
        return self._serial_number


    @serial_number.setter
    def serial_number(self, value):
        self._serial_number = value


    @property
    def propulsion_type(self):
        return self._propulsion_type


    @propulsion_type.setter
    def propulsion_type(self, value):
        self._propulsion_type = value


    @property
    def jet_obs(self):
        return self._jet_obs


    @jet_obs.setter
    def jet_obs(self, value):
        self._jet_obs = value
