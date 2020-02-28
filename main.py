from checkers.data_checker import DataChecker
from graphs.graph_generator import GraphGenerator

if __name__ == "__main__":
    # First checks the files (test1-15.txt are expected)
    DataChecker.check_files()

    # Everything being ok, generate the graphs using a new instance of GraphGenerator.
    graph_generator = GraphGenerator()
    graph_generator.generate()

    # Say howdy, after all you're an polite program :)
    print("Howdy.")
