from scipy.stats import kruskal
import scikit_posthocs as sp
from Metric.Evaluator import Evaluator
import Utils.Commons as cm
from Object.Signal.SignalTypeEnum import signal_enum_by_name


def kruskal_wallis_with_dunn_windows():
    results = {}
    heatmap_data = []
    labels = []

    for model in cm.models():
        for signal in cm.signals():

            data = []
            window_labels = []

            for window in cm.windows():
                evaluator = Evaluator(dataset_type=cm.datasets(), model_type=model, signal_type=signal, window_length=window)
                data.append(evaluator.accuracy)
                window_labels.append(f"Window {window}")

            stat, p_value = kruskal(*data)
            results[f"{model}_{signal}"] = (stat, p_value)
            labels.append(f"{model}_{signal}")
            heatmap_data.append(p_value)

            print(f"Kruskal-Wallis {model} - {signal}: H={stat:.8f}, p={p_value:.8f}")

            if p_value < 0.05:
                print(f"Realizando o teste de Dunn para {model} - {signal}...")
                dunn_results = sp.posthoc_dunn(data, p_adjust="bonferroni")
                print(dunn_results)

    return results


def kruskal_wallis_with_dunn_representations():
    results = {}
    heatmap_data = []
    labels = []

    for model in cm.models():
        for window in cm.windows():
            data = []
            window_labels = []

            for signal in cm.signals():

                evaluator = Evaluator(dataset_type=cm.datasets(), model_type=model, signal_type=signal, window_length=window)
                data.append(evaluator.accuracy)
                window_labels.append(f"Signal {signal}")

            stat, p_value = kruskal(*data)
            results[f"{model}_{window}s"] = (stat, p_value)
            labels.append(f"{model}_{window}s")
            heatmap_data.append(p_value)

            print(f"Kruskal-Wallis {model} - {window}s: H={stat:.8f}, p={p_value:.8f}")

            if p_value < 0.05:
                print(f"Realizando o teste de Dunn para {model} - {window}s...")
                dunn_results = sp.posthoc_dunn(data, p_adjust="bonferroni")
                print(dunn_results)

    return results
