import numpy as np
import sklearn.metrics as metrics
from statistics import mean
from statistics import median
from statistics import pstdev
from Database.DatabaseMetrics import DatabaseMetrics
from Metric.Evaluation import Evaluation
import Metric.EvaluatorConverter as Converter
from Dataset.DatasetTypeEnum import DatasetTypeEnum
from IA.NeuralNetworkTypeEnum import NeuralNetworkTypeEnum
from Object.Signal.SignalTypeEnum import SignalTypeEnum


class Evaluator:
    """
    Class: Evaluator
    """

    def __init__(self, dataset_type: DatasetTypeEnum, model_type: NeuralNetworkTypeEnum, signal_type: SignalTypeEnum, window_length: int):
        """ """
        self.dataset_name = dataset_type.name
        self.model_name = model_type.name
        self.model_data_domain = signal_type.name
        self.window_length = window_length

        database = DatabaseMetrics()
        db_objects = database.metrics_by_model_domain_window(self.dataset_name, self.model_name, self.model_data_domain, window_length)

        self.evaluations: list[Evaluation] = []

        for db_object in db_objects:
            self.evaluations.append(Converter.model_from_tuple(db_object))

        self.true_positives = [evaluation.true_positives for evaluation in self.evaluations]
        self.true_negatives = [evaluation.true_negatives for evaluation in self.evaluations]
        self.false_positives = [evaluation.false_positives for evaluation in self.evaluations]
        self.false_negatives = [evaluation.false_negatives for evaluation in self.evaluations]
        self.total_samples = [evaluation.total_samples for evaluation in self.evaluations]

        self.accuracy = [evaluation.accuracy * 100 for evaluation in self.evaluations]
        self.precision = [evaluation.precision * 100 for evaluation in self.evaluations]
        self.sensitivity = [evaluation.sensitivity * 100 for evaluation in self.evaluations]
        self.specificity = [evaluation.specificity * 100 for evaluation in self.evaluations]
        self.f1_score = [evaluation.f1_score * 100 for evaluation in self.evaluations]

        self.true_positive_rate = [evaluation.true_positive_rate for evaluation in self.evaluations]
        self.false_positive_rate = [evaluation.false_positive_rate for evaluation in self.evaluations]

    def info(self):
        print("[MODEL INFORMATION]")
        print(f"[DATASET]: {self.dataset_name}")
        print(f"[MODEL]: {self.model_name}")
        print(f"[DOMAIN]: {self.model_data_domain}")
        print(f"[WINDOW]: {self.window_length}")
        print("------------------------------------")

    def samples(self):
        print("[SAMPLE STATISTICS]")
        print(f"[True Positives]: {mean(self.true_positives):.2f}")
        print(f"[True Negatives]: {mean(self.true_negatives):.2f}")
        print(f"[False Positives]: {mean(self.false_positives):.2f}")
        print(f"[False Negatives]: {mean(self.false_negatives):.2f}")
        print(f"[Total Samples]: {mean(self.total_samples):.2f}")
        print("------------------------------------")

    def report(self):
        print("[MODEL EVALUATION REPORT]")
        print(f"[Accuracy]: {mean(self.accuracy):.2f}% ± {pstdev(self.accuracy):.2f}%")
        print(f"[Precision]: {mean(self.precision):.2f}% ± {pstdev(self.precision):.2f}%")
        print(f"[Sensitivity]: {mean(self.sensitivity):.2f}% ± {pstdev(self.sensitivity):.2f}%")
        print(f"[Specificity]: {mean(self.specificity):.2f}% ± {pstdev(self.specificity):.2f}%")
        print(f"[F1-Score]: {mean(self.f1_score):.2f}% ± {pstdev(self.f1_score):.2f}%")
        print(f"[TPR]: {mean(self.true_positive_rate):.2f}% ± {pstdev(self.true_positive_rate):.2f}%")
        print(f"[FPR]: {mean(self.false_positive_rate):.2f}% ± {pstdev(self.false_positive_rate):.2f}%")
        print("------------------------------------")

    def generate_roc_auc_data(self):
        tpr = median(self.true_positive_rate)
        fpr = median(self.false_positive_rate)

        tpr_result = np.concatenate([np.linspace(0, tpr, num=50), np.linspace(tpr, 1, num=50)])
        fpr_result = np.concatenate([np.linspace(0, fpr, num=50), np.linspace(fpr, 1, num=50)])

        auc = metrics.auc(fpr_result, tpr_result)

        return tpr_result, fpr_result, auc
