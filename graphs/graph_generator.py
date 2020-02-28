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
        returnable_cars = []

        for filename in filenames:
            car = Car()
            file_data = open("./test_data/" + filename).read().splitlines()

            if file_data[0].lower() == "categoria":
                CategorizedParser(car).parse(filename)
            else:
                NamedParser.parse(car, filename)

            returnable_cars.append(car)

        return returnable_cars


    def generate(self):
        filenames = self.get_filenames()
        cars = self.analyze_and_parse(filenames)

    # def sample_plot(self):
    #     plt.bar("hello", 2, color="green")
    #     plt.bar("howdy", 4)
    #     plt.title("Greetings")
    #
    #     plt.show()