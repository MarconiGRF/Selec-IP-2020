from graphs.data_parser import DataParser
import re


class NamedParser(DataParser):
    """This class implements the methods for DataParser abstract class, being an utility to get data from .txt files."""
    __author__ = "Marconi Gomes"

    color = "COR"
    mileage = "KM"
    year = "ANO"
    ports = "PORTAS"
    fuel = "Combustível:"
    plate = "placa:"
    engine = "Motor:"
    exchange = "Transmissão:"
    other_info_regex = '[A-z\u00C0-\u017F]*: .*'
    photos_regex = '[0-9]* [a-z]{5}'

    @staticmethod
    def parse_brand_and_model(self):
        brand_and_model = self.file_data[0].split(" ")
        self.car.set_brand(brand_and_model.pop(0))
        self.car.set_model(" ".join(brand_and_model))

    @staticmethod
    def parse_location(self):
        location = self.file_data[1].split(" - ")
        self.car.set_location(location[0])
        self.car.set_state(location[1])

    @staticmethod
    def parse_mileage(self):
        if self.mileage in self.file_data:
            self.car.set_mileage(int(self.file_data[self.file_data.index(self.mileage) + 1]))

    @staticmethod
    def parse_year(self):
        if self.year in self.file_data:
            car_year = self.file_data[self.file_data.index(self.year) + 1]
            if car_year[0:4] == car_year[-4:]:
                car_year = car_year[0:4]
                self.car.set_year(int(car_year))
            else:
                self.car.set_year(car_year)

    @staticmethod
    def parse_color(self):
        self.car.set_color(self.file_data[self.file_data.index(self.color) + 1])

    @staticmethod
    def parse_ports(self):
        if self.ports in self.file_data:
            self.car.set_ports(int(self.file_data[self.file_data.index(self.ports) + 1]))

    @staticmethod
    def parse_price(self):
        exp = re.compile('[R][$] [0-9]{2}[.]*[0-9]*,[0-9]*')
        price = float(list(filter(exp.match, self.file_data))[0][3:].replace(".", "").replace(",", "."))
        self.car.set_price(price)

    @staticmethod
    def parse_other_info(self):
        exp = re.compile(self.other_info_regex)
        other_info = list(filter(exp.match, self.file_data))[0].split(" ")

        self.car.set_fuel(other_info[other_info.index(self.fuel) + 1])
        self.car.set_plate_ending(other_info[other_info.index(self.plate) + 1])
        self.car.set_potency(other_info[other_info.index(self.engine) + 1])
        self.car.set_exchange(other_info[other_info.index(self.exchange) + 1])


    @staticmethod
    def parse_photos(self):
        exp = re.compile(self.photos_regex)
        photos = list(filter(exp.match, self.file_data))

        if len(photos) == 0:
            self.car.set_photos(0)
        else:
            photos = self.file_data.pop(self.file_data.index(photos[0])).split(" ")
            self.car.set_photos(photos[0])

    @staticmethod
    def parse_address(self):
        if not re.match(self.other_info_regex, self.file_data[len(self.file_data) - 1]):
            self.car.set_address(self.file_data[len(self.file_data) - 1])


    def parse(self, txt_filename):
        print("    Parsing " + txt_filename + "...")
        self.file_data = open("./test_data/" + txt_filename).read().splitlines()

        self.parse_brand_and_model(self)
        self.parse_location(self)
        self.parse_mileage(self)
        self.parse_year(self)
        self.parse_color(self)
        self.parse_ports(self)
        self.parse_price(self)
        self.parse_photos(self)
        self.parse_other_info(self)
        self.parse_address(self)

        print("    OK.")

