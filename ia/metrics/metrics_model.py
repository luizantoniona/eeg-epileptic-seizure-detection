"""

"""

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

    def show(self):
        print("MODEL:", self.model_name)
        print("DATA DOMAIN:", self.model_data_domain)
        print('True Positives:', self.true_positives)
        print('True Negatives:', self.true_negatives)
        print('False Positives:', self.false_positives)
        print('False Negatives:', self.false_negatives)
        print('total Samples:', self.total_samples)
        print('Accuracy:',self.accuracy)
        print('Precision:',self.precision)
        print('Sensitivity:',self.sensitivity)
        print('Specificity:',self.specificity)
        print('TPR:',self.true_positive_rate)
        print('FPR:',self.false_positive_rate)
        print('F1-Score:',self.f1_score)
