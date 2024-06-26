"""

"""

from Metric.Evaluator import Evaluator

def model_from_tuple( metric_tuple ) -> Evaluator:
    """
    
    """
    model = Evaluator (
        metric_tuple['model_name'],
        metric_tuple['model_data_domain'],
        metric_tuple['true_positives'],
        metric_tuple['true_negatives'],
        metric_tuple['false_positives'],
        metric_tuple['false_negatives'],
        metric_tuple['total_samples'],
        metric_tuple['accuracy'],
        metric_tuple['precision'],
        metric_tuple['sensitivity'],
        metric_tuple['specificity'],
        metric_tuple['true_positive_rate'],
        metric_tuple['false_positive_rate'],
        metric_tuple['f1_score']
    )

    return model