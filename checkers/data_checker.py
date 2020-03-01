import glob
import logging


class DataChecker:
    """This class represents the checker for the Graphs' data."""
    __author__ = "Marconi Gomes"

    @staticmethod
    def check_files():
        """Checks the test files using glob."""
        print("----- Checking files... -----")

        try:
            filenames = glob.glob("./test_data/*.txt")
            filenames.sort()
            for i in range(1, 16):
                filename = "./test_data/test" + str(i) + ".txt"
                if not (filename in filenames):
                    raise Exception(filename + " not found.")

            print("----- OK -----")

        except Exception as ex:
            logging.exception(str(ex))
            raise Exception
