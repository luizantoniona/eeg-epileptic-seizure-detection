from Database.DatabaseMetrics import DatabaseMetrics


class Metric:
    """
    Class: Metric
    """

    def __init__(self, test, predictions, dataset_name: str, model_name: str, model_data_domain: str, model_window_length: int):

        self.dataset_name = dataset_name
        self.model_name = model_name
        self.model_data_domain = model_data_domain
        self.model_window_length = model_window_length

        self.true_positives = 0
        self.true_negatives = 0
        self.false_positives = 0
        self.false_negatives = 0
        self.total_samples = len(test)

        for i in range(self.total_samples):
            if test[i] == True and predictions[i] == True:
                self.true_positives += 1
            elif test[i] == False and predictions[i] == False:
                self.true_negatives += 1
            elif test[i] == True and predictions[i] == False:
                self.false_positives += 1
            elif test[i] == False and predictions[i] == True:
                self.false_negatives += 1

        self.accuracy = (self.true_positives + self.true_negatives) / (self.total_samples)
        self.precision = (self.true_positives) / (self.true_positives + self.false_positives)
        self.sensitivity = (self.true_positives) / (self.false_negatives + self.true_positives)
        self.specificity = (self.true_negatives) / (self.true_negatives + self.false_positives)
        self.true_positive_rate = (self.true_positives) / (self.true_positives + self.false_positives)
        self.false_positive_rate = (self.false_positives) / (self.false_positives + self.true_negatives)
        self.f1_score = (2 * self.accuracy * self.sensitivity) / (self.accuracy + self.sensitivity)

    def all_metrics(self):
        print(f"[True Positives]: {self.true_positives}")
        print(f"[True Negatives]: {self.true_negatives}")
        print(f"[False Positives]: {self.false_positives}")
        print(f"[False Negatives]: {self.false_negatives}")
        print(f"[Total Samples]: {self.total_samples}")
        print(f"[Accuracy]: {self.accuracy}")
        print(f"[Precision]: {self.precision}")
        print(f"[Sensitivity]: {self.sensitivity}")
        print(f"[Specificity]: {self.specificity}")
        print(f"[F1-Score]: {self.f1_score}")
        print(f"[TPR]: {self.true_positive_rate}")
        print(f"[FPR]: {self.false_positive_rate}")

    def metrics_to_database(self):
        database = DatabaseMetrics()
        database.insert_metrics_data(
            self.dataset_name,
            self.model_name,
            self.model_data_domain,
            self.model_window_length,
            self.accuracy,
            self.precision,
            self.sensitivity,
            self.specificity,
            self.true_positive_rate,
            self.false_positive_rate,
            self.f1_score,
            self.true_positives,
            self.true_negatives,
            self.false_positives,
            self.false_negatives,
            self.total_samples,
        )
