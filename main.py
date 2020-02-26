from checkers.data_checker import DataChecker
from objects.car_object import Car
from graphs.graph_generator import GraphGenerator
from graphs.named_parser import NamedParser

if __name__ == "__main__":
    GraphGenerator.sample_plot()
    test_car = Car()
    named_test = NamedParser(test_car)
    named_test.parse("test1")
    DataChecker.check_files()
    print("Howdy.")
