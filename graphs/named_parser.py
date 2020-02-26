from graphs.data_parser import DataParser

class NamedParser(DataParser):
    """This class implements the methods for DataParser abstract class, being an utility to get data from .txt files."""
    __author__ = "Marconi Gomes"

    def parse(self, txt_filename):
        file = open("./test_data/" + txt_filename + ".txt")
        file_data = file.read().replace("\n", "")
        print(file_data)