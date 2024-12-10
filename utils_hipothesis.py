from Metric.Evaluator import Evaluator
from scipy.stats import mannwhitneyu
import numpy as np
import itertools
from Utils.Graphics.ConfusionMatrixPlotter import ConfusionMatrixPlotter
import Utils.Commons as cm


def generate_hipothesis(group_1, group_2):
    p_value = mannwhitneyu(group_1, group_2).pvalue
    return p_value


def models_competition():
    num_combinations = len(cm.models()) * len(cm.signals()) * len(cm.windows())

    confusion_matrix = np.zeros((num_combinations, num_combinations))

    combinations = list(itertools.product(cm.models(), cm.signals(), cm.windows()))

    for i, (model_1, signal_1, window_1) in enumerate(combinations):
        first = Evaluator(dataset_type=cm.datasets(), model_type=model_1, signal_type=signal_1, window_length=window_1)

        for j, (model_2, signal_2, window_2) in enumerate(combinations):
            second = Evaluator(dataset_type=cm.datasets(), model_type=model_2, signal_type=signal_2, window_length=window_2)

            p_value = generate_hipothesis(first.accuracy, second.accuracy)
            #            if p_value > 0.05:
            #                p_value = 1.0
            #            elif p_value <= 0.05:
            #                p_value = 0.0005

            confusion_matrix[i, j] = p_value

    return confusion_matrix, combinations


confusion_matrix, combinations = models_competition()
plotter = ConfusionMatrixPlotter(confusion_matrix, combinations)
plotter.plot()
