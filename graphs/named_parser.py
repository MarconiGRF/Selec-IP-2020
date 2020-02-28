from graphs.data_parser import DataParser


class NamedParser(DataParser):
    """This class implements the methods for DataParser abstract class, being an utility to get data from .txt files."""
    __author__ = "Marconi Gomes"

    @classmethod
    def parse(cls, car, txt_filename):
        file_data = open("./test_data/" + txt_filename).read().splitlines()


        print(file_data)
