import matplotlib.pyplot as plt


class BarPlotter:
    """ """

    def __init__(self, models, accuracies, xlabel, title, color="b"):
        self.models = models
        self.accuracies = accuracies
        self.xlabel = xlabel
        self.title = title
        self.color = color

    def plot(self):
        plt.figure(figsize=(12, 8))
        plt.barh(self.models, self.accuracies, color=self.color)
        plt.xlabel(self.xlabel)
        plt.title(self.title)
        plt.gca().invert_yaxis()
        plt.tight_layout()

        plt.show()
