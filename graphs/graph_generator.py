import matplotlib.pyplot as plt


class GraphGenerator:

    def __init__(self):
        pass

    @staticmethod
    def sample_plot():
        plt.bar("hello", 2, color="green")
        plt.bar("howdy", 4)
        plt.title("Greetings")

        plt.show()