import matplotlib.pyplot as plt
import sklearn.metrics as metrics


class ROCPlotter:
    """ """

    def __init__(self):
        self.curves = []
        self.labels = []
        self.colors = []

    def add_curve(self, ground_truth, predictions, label="ROC Curve", color=None):
        """
        Add a new ROC curve to the plotter.

        Args:
        ground_truth (array-like): True binary labels.
        predictions (array-like): Predicted probabilities.
        label (str): Label for the ROC curve.
        color (str): Optional color for the curve.
        """
        fpr, tpr, _ = metrics.roc_curve(ground_truth, predictions)
        auc_value = metrics.auc(fpr, tpr)

        self.curves.append((fpr, tpr, auc_value))
        self.labels.append(f"{label} (AUC = {auc_value:.2f})")
        self.colors.append(color)

    def plot(self, plot_random_guess=False):
        """
        Plot all the added ROC curves.
        """

        for i, (fpr, tpr, _) in enumerate(self.curves):
            color = self.colors[i] if self.colors[i] is not None else "b"
            plt.plot(fpr, tpr, label=f"{self.labels[i]}", color=color)

        if plot_random_guess:
            plt.plot([0, 1], [0, 1], "r--", label="Random Guess")

        plt.title("Receiver Operating Characteristic")
        plt.xlabel("False Positive Rate")
        plt.ylabel("True Positive Rate")
        plt.xlim([0, 1])
        plt.ylim([0, 1])
        plt.legend(loc="lower right")
        plt.show()
