class Evaluation:
    """
    """
    def __init__(self, dataset_name, model_name, model_data_domain, model_window_length,
                true_positives, true_negatives, false_positives, false_negatives, total_samples,
                accuracy, precision, sensitivity, specificity, true_positive_rate, false_positive_rate, f1_score):
        """
        """
        self.dataset_name = dataset_name
        self.model_name = model_name
        self.model_data_domain = model_data_domain
        self.model_window_length = model_window_length

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
