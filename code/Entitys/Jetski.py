class Jetski:
    def __init__(self, brand: str, model: str, jet_year: int, serial_number: str, propulsion_type: str, jet_obs: str):
        if(isinstance(brand, str)):
            self._brand = brand
        if(isinstance(model)):
            self._model = model
        if(isinstance(jet_year, int)):
            self._jet_year = jet_year
        if(isinstance(serial_number, str)):
            self._serial_number = serial_number
        if(isinstance(propulsion_type, str)):
            self._propulsion_type = propulsion_type
        if(isinstance(jet_obs, str)):
            self._jet_obs = jet_obs


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
