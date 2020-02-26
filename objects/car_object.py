class Car:
    """This class represents a car object which data will be parsed."""
    __author__ = "Marconi Gomes"

    def __init__(self):
        self.name = None
        self.model = None
        self.brand = None
        self.vehicle_type = None
        self.color = None
        self.location = None
        self.year = None
        self.mileage = None
        self.ports = None
        self.price = None
        self.state = None
        self.pictures = None
        self.address = None

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_model(self):
        return self.model

    def set_model(self, model):
        self.model = model

    def get_brand(self):
        return self.brand

    def set_brand(self, brand):
        self.brand = brand

    def get_vehicle_type(self):
        return self.vehicle_type

    def set_vehicle_type(self, vehicle_type):
        self.vehicle_type = vehicle_type

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color

    def get_location(self):
        return self.location

    def set_location(self, location):
        self.location = location

    def get_year(self):
        return self.year

    def set_year(self, year):
        self.year = year

    def get_mileage(self):
        return self.mileage

    def set_mileage(self, mileage):
        self.mileage = mileage

    def get_ports(self):
        return self.ports

    def set_ports(self, ports):
        self.ports = ports

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price

    def get_state(self):
        return self.state

    def set_state(self, state):
        self.state = state

    def get_pictures(self):
        return self.pictures

    def set_pictures(self, pictures):
        self.pictures = pictures

    def get_address(self):
        return self.address

    def set_address(self, address):
        self.address = address
