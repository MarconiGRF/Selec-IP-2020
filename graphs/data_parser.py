from abc import ABC, abstractclassmethod


class DataParser(ABC):
    """This abstract class describes the abstract methods to get the data from .txt files."""
    __author__ = "Marconi Gomes"

    def __init__(self, car):
        self.car = car
        self.file_data = None

    @abstractclassmethod
    def parse(cls, txt_filename):
        pass
