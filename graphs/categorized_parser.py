from graphs.data_parser import DataParser


class CategorizedParser(DataParser):
    """This class implements the methods for DataParser abstract class, being an utility to get data from .txt files."""
    __author__ = "Marconi Gomes"

    model = "Modelo"
    brand = "Marca"
    type = "Tipo de veículo"
    year = "Ano"
    steering = "Direção"
    mileage = "Quilometragem"
    potency = "Potência do motor"
    fuel = "Combustível"
    exchange = "Câmbio"
    color = "Cor"
    plate_end = "Final de placa"
    ports = "Portas"

    @staticmethod
    def remove_attribute_from_source(self, attr_name):
        self.file_data.pop(self.file_data.index(self.file_data[attr_name]))

    def parse(self, txt_filename):

        self.file_data = open("./test_data/" + txt_filename).read().splitlines()

        if self.brand in self.file_data:
            car_brand = self.file_data[self.file_data.index(self.brand) + 1].split(" - ")
            self.car.set_brand(car_brand.pop())

            self.remove_attribute_from_source(self, self.brand)
            self.file_data.pop(self.file_data.index(self.brand))

        if self.model in self.file_data:
            car_model = self.file_data[self.file_data.index(self.model) + 1].split(self.car.get_brand())
            self.car.set_model(car_model.pop())

        if self.type in self.file_data:
            self.car.set_vehicle_type(self.file_data[self.file_data.index(self.type) + 1])

        if self.year in self.file_data:
            car_year = self.file_data[self.file_data.index(self.year) + 1]
            if car_year[0:4] == car_year[-4:]:
                car_year = car_year[0:4]
            self.car.set_year(int(car_year))

        if self.mileage in self.file_data:
            self.car.set_mileage(int(self.file_data[self.file_data.index(self.mileage) + 1]))

        if self.steering in self.file_data:
            self.car.set_steering(self.file_data[self.file_data.index(self.steering) + 1])

        if self.potency in self.file_data:
            self.car.set_potency(float(self.file_data[self.file_data.index(self.potency) + 1]))

        if self.fuel in self.file_data:
            self.car.set_fuel(self.file_data[self.file_data.index(self.fuel) + 1])

        if self.exchange in self.file_data:
            self.car.set_exchange(self.file_data[self.file_data.index(self.exchange) + 1])

        if self.ports in self.file_data:
            self.car.set_ports(self.file_data)
        if self.color in self.file_data:
            self.car.set_color(self.file_data[self.file_data.index(self.color) + 1])