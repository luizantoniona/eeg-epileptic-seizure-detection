import matplotlib.pyplot as plt
import seaborn as sns


class ConfusionMatrixPlotter:
    def __init__(self, confusion_matrix, combinations):
        self.confusion_matrix = confusion_matrix
        self.combinations = combinations
        self.labels = [f"{model.name}-{signal.name}-{window}s" for model, signal, window in combinations]

    def plot(self):
        plt.figure(figsize=(8, 8))
        sns.heatmap(self.confusion_matrix, xticklabels=self.labels, yticklabels=self.labels, cmap="coolwarm", cbar=True, linewidths=0.5, linecolor="black", square=True)

        plt.title("p-values")
        plt.xlabel("Configuration")
        plt.ylabel("Configuration")
        plt.xticks(rotation=90, fontsize=8)
        plt.yticks(fontsize=8)
        plt.tight_layout()
        plt.show()
