from scipy.stats import kruskal
import scikit_posthocs as sp
from Metric.Evaluator import Evaluator
import Utils.Commons as cm
import pandas as pd


def kruskal_wallis_with_dunn_windows():
    results = {}

    for model in cm.models():
        for signal in cm.signals():

            data = []
            window_labels = []
            flattened_data = []
            groups = []

            for window in cm.windows():
                evaluator = Evaluator(dataset_type=cm.datasets(), model_type=model, signal_type=signal, window_length=window)
                accuracies = evaluator.accuracy
                data.append(accuracies)

                window_label = f"{model.name}_{signal.name}_Win{window}"
                window_labels.append(window_label)

                flattened_data.extend(accuracies)
                groups.extend([window_label] * len(accuracies))

            stat, p_value = kruskal(*data)
            results[f"{model}_{signal}"] = (stat, p_value)
            print(f"Kruskal-Wallis {model.name} - {signal.name}: H={stat:.8f}, p={p_value:.8f}")

            if p_value < 0.05:
                print(f"Realizando o teste de Dunn para {model.name} - {signal.name}")

                df = pd.DataFrame({"Accuracy": flattened_data, "Group": groups})

                dunn_results = sp.posthoc_dunn(df, val_col="Accuracy", group_col="Group", p_adjust="bonferroni")
                print(dunn_results)

    return results


def kruskal_wallis_with_dunn_representations():
    results = {}

    for model in cm.models():
        for window in cm.windows():
            data = []
            window_labels = []
            flattened_data = []
            groups = []

            for signal in cm.signals():
                evaluator = Evaluator(dataset_type=cm.datasets(), model_type=model, signal_type=signal, window_length=window)
                accuracies = evaluator.accuracy
                data.append(evaluator.accuracy)

                window_label = f"{model.name}_{signal.name}_Win{window}"
                window_labels.append(window_label)

                flattened_data.extend(accuracies)
                groups.extend([window_label] * len(accuracies))

            stat, p_value = kruskal(*data)
            results[f"{model}_{window}"] = (stat, p_value)
            print(f"Kruskal-Wallis {model.name} - {window}: H={stat:.8f}, p={p_value:.8f}")

            if p_value < 0.05:
                print(f"Realizando o teste de Dunn para {model.name} - {window}s")

                df = pd.DataFrame({"Accuracy": flattened_data, "Group": groups})

                dunn_results = sp.posthoc_dunn(df, val_col="Accuracy", group_col="Group", p_adjust="bonferroni")
                print(dunn_results)

    return results
