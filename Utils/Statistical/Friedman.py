from scipy.stats import friedmanchisquare
from statsmodels.stats.multicomp import pairwise_tukeyhsd
import numpy as np
from Metric.Evaluator import Evaluator
import Utils.Commons as cm


def friedman_test_models():
    results = {}

    for signal in cm.signals():
        for window in cm.windows():
            data = []
            window_labels = []
            flattened_data = []
            groups = []

            for model in cm.models():
                evaluator = Evaluator(dataset_type=cm.datasets(), model_type=model, signal_type=signal, window_length=window)
                accuracies = evaluator.accuracy
                data.append(accuracies)

                window_label = f"{signal.name}_{window}_MOD{model}"
                window_labels.append(window_label)

                flattened_data.extend(accuracies)
                groups.extend([window_label] * len(accuracies))

            friedman_result, p_value = friedmanchisquare(*data)
            results[f"{signal}_{str(window)}"] = (friedman_result, p_value)
            print(f"Friedman {signal.name} - {window}: H={friedman_result:.8f}, p={p_value:.8f}")

            if p_value < 0.05:
                print(f"Performing Tukey's Post-Test for Signal={signal.name}, Window={window}s...")

                assert len(flattened_data) == len(groups), f"Mismatch in lengths: {len(flattened_data)} vs {len(groups)}"

                tukey_result = pairwise_tukeyhsd(np.array(flattened_data), np.array(groups), alpha=0.05)
                print(tukey_result.summary())

    return results
