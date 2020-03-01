import matplotlib.pyplot as plt
from objects.car_object import Car
from graphs.named_parser import NamedParser
from graphs.categorized_parser import CategorizedParser
import glob

class GraphGenerator:
    """
    This class represents the graph generator and its functions to correctly generate
    graphs for the desired purpose.
    """
    __author__ = "Marconi Gomes"

    def __init__(self):
        pass

    @staticmethod
    def get_filenames():
        returnable_filenames = []

        filenames = glob.glob("./test_data/*.txt")
        for filename in filenames:
            temp = filename.split("/")
            returnable_filenames.append(temp[2])

        return returnable_filenames

    @staticmethod
    def analyze_and_parse(filenames):
        print("----- Parsing data... -----")
        returnable_cars = []

        for filename in filenames:
            car = Car()
            file_data = open("./test_data/" + filename).read().splitlines()

            if file_data[0].lower() == "categoria":
                CategorizedParser(car).parse(filename)
            else:
                NamedParser(car).parse(filename)

            returnable_cars.append(car)

        print("----- OK -----")
        return returnable_cars

    @staticmethod
    def by_price(cars):
        print("    By price...")
        plt.title("Modelos de carro por preço (R$)")

        for car in cars:
            if car.get_price() is not None:
                model = car.get_model().split(" ")[0]
                plt.bar(model, car.get_price())

        plt.show()
        print("    OK.")

    @staticmethod
    def by_brand(cars):
        print("    By brand...")
        plt.title("Quantidade de carros à venda por marca")

        car_brands = []
        for car in cars:
            car_brands.append(car.get_brand().upper())

        for brand in car_brands:
            appearsons = car_brands.count(brand)
            plt.bar(brand, appearsons)

        plt.show()
        print("    OK.")

    @staticmethod
    def by_color(cars):
        print("    By color...")
        plt.title("Quantidade de carros à venda por cor")

        car_colors = []
        pt_to_en_colors = {
            'VERMELHO': 'red',
            'AMARELO': 'yellow',
            'VERDE': 'green',
            'BRANCO': 'white',
            'PRATA': 'silver',
            'AZUL': 'blue',
            'PRETO': 'black',
            'MARROM': 'brown'
        }
        for car in cars:
            car_colors.append(car.get_color().upper())

        for color in car_colors:
            color_count = car_colors.count(color)
            plt.bar(color, color_count, color=pt_to_en_colors.get(color), edgecolor=pt_to_en_colors.get('VERDE'))

        plt.show()
        print("    OK.")

    @staticmethod
    def by_fuel(cars):
        print("    By color...")
        plt.title("Porcentagem de carros à venda por tipo de combustível")

        car_fuel_types = []
        for car in cars:
            car_fuel_types.append(car.get_fuel().upper())

        fuel_types_count = []
        dict_fuel_types = set(car_fuel_types)
        for fuel_type in dict_fuel_types:
            fuel_types_count.append(car_fuel_types.count(fuel_type))

        percentages = []
        for value in fuel_types_count:
            total = 0
            for i in fuel_types_count:
                total = total + i

            percentages.append((value * 100)/total)

        plt.pie(percentages, labels=list(dict_fuel_types), autopct='%1.1f%%')
        plt.show()
        print("    OK")

    def generate(self):
        filenames = self.get_filenames()
        cars = self.analyze_and_parse(filenames)

        print("----- Generating plots -----")
        self.by_price(cars)
        plt.clf()
        self.by_brand(cars)
        plt.clf()
        self.by_color(cars)
        plt.clf()
        self.by_fuel(cars)
        plt.clf()
        print("----- OK -----")
