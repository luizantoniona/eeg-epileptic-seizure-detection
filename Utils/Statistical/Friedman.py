from scipy.stats import friedmanchisquare
from statsmodels.stats.multicomp import pairwise_tukeyhsd
import numpy as np
from Metric.Evaluator import Evaluator
import Utils.Commons as cm
from Object.Signal.SignalTypeEnum import signal_enum_by_name


def friedman_test_models():
    results = {}
    heatmap_data = []
    labels = []

    for signal in cm.signals():
        data = []

        for window in cm.windows():
            accuracies = []

            for model in cm.models():
                evaluator = Evaluator(dataset_type=cm.datasets(), model_type=model, signal_type=signal, window_length=window)
                accuracies.append(evaluator.accuracy)

            stat, p_value = friedmanchisquare(*accuracies)
            data.append((stat, p_value))

        results[f"{signal}"] = data
        labels.append(f"{signal}")
        heatmap_data.append([p_value for _, p_value in data])

        print(f"Friedman Test for Signal={signal}:")
        for idx, (stat, p_value) in enumerate(data):
            print(f"Window {cm.windows()[idx]}s: H={stat:.4f}, p={p_value:.4f}")

            if p_value < 0.05:
                print(f"Performing Nemenyi Post-Test for Signal={signal}, Window={cm.windows()[idx]}s...")
                pairwise_results = pairwise_tukeyhsd(np.array(accuracies).flatten(), np.repeat(range(len(accuracies)), len(accuracies[0])), alpha=0.05)
                print(pairwise_results)

    return results
