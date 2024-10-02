import numpy as np
import sklearn.metrics as metrics
from statistics import mean 
from statistics import median
from statistics import pstdev
from Database.DatabaseMetrics import DatabaseMetrics
from Metric.Evaluation import Evaluation
import Metric.EvaluatorConverter as Converter

class Evaluator:
    """

    """
    def __init__(self, dataset_name, model_name, model_data_domain, model_window_length):
        """
        """
        self.dataset_name = dataset_name
        self.model_name = model_name
        self.model_data_domain = model_data_domain
        self.model_window_length = model_window_length

        database = DatabaseMetrics()
        db_objects = database.metrics_by_model_domain_window(dataset_name, model_name, model_data_domain, model_window_length)

        self.evaluations: list[Evaluation] = []

        for db_object in db_objects:
            self.evaluations.append(Converter.model_from_tuple(db_object))

        self.true_positives = [evaluation.true_positives for evaluation in self.evaluations]
        self.true_negatives = [evaluation.true_negatives for evaluation in self.evaluations]
        self.false_positives = [evaluation.false_positives for evaluation in self.evaluations]
        self.false_negatives = [evaluation.false_negatives for evaluation in self.evaluations]
        self.total_samples = [evaluation.total_samples for evaluation in self.evaluations]
        self.accuracy = [evaluation.accuracy for evaluation in self.evaluations]
        self.precision = [evaluation.precision for evaluation in self.evaluations]
        self.sensitivity = [evaluation.sensitivity for evaluation in self.evaluations]
        self.specificity = [evaluation.specificity for evaluation in self.evaluations]
        self.true_positive_rate = [evaluation.true_positive_rate for evaluation in self.evaluations]
        self.false_positive_rate = [evaluation.false_positive_rate for evaluation in self.evaluations]
        self.f1_score = [evaluation.f1_score for evaluation in self.evaluations]

    def show_name(self):
        print("MODEL:", self.model_name)
        print("DATA DOMAIN:", self.model_data_domain)
        print("WINDOW SIZE:", self.model_window_length)

    def show_sample(self):
        print("SAMPLE:")
        print('True Positives:', mean(self.true_positives))
        print('True Negatives:', mean(self.true_negatives))
        print('False Positives:', mean(self.false_positives))
        print('False Negatives:', mean(self.false_negatives))
        print('Total Samples:', mean(self.total_samples))
        print("------------------------------------")

    def show_mean(self):
        print("MEAN:")
        print('Accuracy:', mean(self.accuracy))
        print('Precision:', mean(self.precision))
        print('Sensitivity:', mean(self.sensitivity))
        print('Specificity:', mean(self.specificity))
        print('F1-Score:', mean(self.f1_score))
        print('TPR:', mean(self.true_positive_rate))
        print('FPR:', mean(self.false_positive_rate))
        print("------------------------------------")

    def show_deviation(self):
        print("DEVIATION:")
        print('Accuracy:', pstdev(self.accuracy))
        print('Precision:', pstdev(self.precision))
        print('Sensitivity:', pstdev(self.sensitivity))
        print('Specificity:', pstdev(self.specificity))
        print('F1-Score:', pstdev(self.f1_score))
        print('TPR:', pstdev(self.true_positive_rate))
        print('FPR:', pstdev(self.false_positive_rate))
        print("------------------------------------")

    def show(self):
        print("MODEL:", self.model_name)
        print("DATA DOMAIN:", self.model_data_domain)
        print("WINDOW SIZE:", self.model_window_length)
        print("SAMPLES:", len(self.evaluations))
        print("MEAN +- DEVIATION:")
        print('Accuracy:', mean(self.accuracy)*100, "+-", pstdev(self.accuracy)*100)
        print('Precision:', mean(self.precision)*100, "+-", pstdev(self.precision)*100)
        print('Sensitivity:', mean(self.sensitivity)*100, "+-", pstdev(self.sensitivity)*100)
        print('Specificity:', mean(self.specificity)*100, "+-", pstdev(self.specificity)*100)
        print('F1-Score:', mean(self.f1_score)*100, "+-", pstdev(self.f1_score)*100)
        print('TPR:', mean(self.true_positive_rate)*100, "+-", pstdev(self.true_positive_rate)*100)
        print('FPR:', mean(self.false_positive_rate)*100, "+-", pstdev(self.false_positive_rate)*100)
        print("------------------------------------")

    def show_median(self):
        print("MEDIAN:")
        print('Accuracy:', median(self.accuracy))
        print('Precision:', median(self.precision))
        print('Sensitivity:', median(self.sensitivity))
        print('Specificity:', median(self.specificity))
        print('F1-Score:', median(self.f1_score))
        print('TPR:', median(self.true_positive_rate))
        print('FPR:', median(self.false_positive_rate))
        print("------------------------------------")

    def generate_roc_auc_data(self):
        tpr = median(self.true_positive_rate)
        fpr = median(self.false_positive_rate)

        tpr_result = np.concatenate([np.linspace(0, tpr, num=50), np.linspace(tpr, 1, num=50)])
        fpr_result = np.concatenate([np.linspace(0, fpr, num=50), np.linspace(fpr, 1, num=50)])

        auc = metrics.auc(fpr_result, tpr_result)

        return tpr_result, fpr_result, auc
