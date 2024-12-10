import itertools
import Utils.Commons as cm
from Utils.Graphics.BarPlotter import BarPlotter
from Metric.Evaluator import Evaluator

combinations = list(itertools.product(cm.models(), cm.signals(), cm.windows()))

model_accuracies = []

for model, signal, window in combinations:
    evaluation = Evaluator(dataset_type=cm.datasets(), model_type=model, signal_type=signal, window_length=window)

    if len(evaluation.accuracy) < 10:
        continue

    avg_accuracy = sum(evaluation.f1_score) / len(evaluation.f1_score)
    model_accuracies.append((f"{model.name}-{signal.name}-{window}s", avg_accuracy))

model_accuracies.sort(key=lambda x: x[1], reverse=True)

models = [item[0] for item in model_accuracies]
accuracies = [item[1] for item in model_accuracies]

plotter = BarPlotter(models, accuracies, "F1-Score", "Rank by F1-Score", color="k")
plotter.plot()
