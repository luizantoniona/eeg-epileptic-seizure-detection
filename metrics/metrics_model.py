"""

"""

from statistics import mean 
from statistics import median
from statistics import pstdev

class MetricsModel:
    """
    
    """
    def __init__(self, model_name, model_data_domain,
                true_positives, true_negatives, false_positives, false_negatives, total_samples,
                accuracy, precision, sensitivity, specificity, true_positive_rate, false_positive_rate, f1_score):
        """
        
        """
        self.model_name = model_name
        self.model_data_domain = model_data_domain
        self.true_positives = true_positives
        self.true_negatives = true_negatives
        self.false_positives = false_positives
        self.false_negatives = false_negatives
        self.total_samples = total_samples
        self.accuracy = accuracy
        self.precision = precision
        self.sensitivity = sensitivity
        self.specificity = specificity
        self.true_positive_rate = true_positive_rate
        self.false_positive_rate = false_positive_rate
        self.f1_score = f1_score

    def show_name(self):
        print("MODEL:", self.model_name)
        print("DATA DOMAIN:", self.model_data_domain)
        print("------------------------------------")
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
        print('TPR:', mean(self.true_positive_rate))
        print('FPR:', mean(self.false_positive_rate))
        print('F1-Score:', mean(self.f1_score))
        print("------------------------------------")

    def show_deviation(self):
        print("DEVIATION:")
        print('Accuracy:', pstdev(self.accuracy))
        print('Precision:', pstdev(self.precision))
        print('Sensitivity:', pstdev(self.sensitivity))
        print('Specificity:', pstdev(self.specificity))
        print('TPR:', pstdev(self.true_positive_rate))
        print('FPR:', pstdev(self.false_positive_rate))
        print('F1-Score:', pstdev(self.f1_score))
        print("------------------------------------")

    def show_median(self):
        print("MEDIAN:")
        print('Accuracy:', median(self.accuracy))
        print('Precision:', median(self.precision))
        print('Sensitivity:', median(self.sensitivity))
        print('Specificity:', median(self.specificity))
        print('TPR:', median(self.true_positive_rate))
        print('FPR:', median(self.false_positive_rate))
        print('F1-Score:', median(self.f1_score))
        print("------------------------------------")
