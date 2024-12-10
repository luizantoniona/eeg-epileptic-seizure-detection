import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


class ViolinPlot:
    def __init__(self, data, x_col="Model", y_col="Metric", group_col="Group", palette="muted"):
        """ """
        if isinstance(data, dict):
            self.data = pd.DataFrame(data)
        elif isinstance(data, pd.DataFrame):
            self.data = data
        else:
            raise ValueError("Data must be a dictionary or a pandas DataFrame")

        self.x_col = x_col
        self.y_col = y_col
        self.group_col = group_col
        self.palette = palette

    def plot(self, title="Violin Plot", xlabel="Model", ylabel="Metric", figsize=(10, 6), inner="quartile"):
        """ """
        plt.figure(figsize=figsize)
        sns.violinplot(
            x=self.data[self.x_col], y=self.data[self.y_col], hue=self.data[self.group_col] if self.group_col in self.data.columns else None, data=self.data, palette=self.palette, inner=inner, split=True if self.group_col in self.data.columns else False
        )
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.legend(title=self.group_col if self.group_col in self.data.columns else None)
        plt.show()
