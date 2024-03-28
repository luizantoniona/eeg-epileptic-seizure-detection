"""

"""

from metrics.metrics_model import MetricsModel

def model_from_tuple( metrics_tuple ) -> MetricsModel:
    """
    
    """
    model = MetricsModel (
        metrics_tuple['model_name'],
        metrics_tuple['model_data_domain'],
        metrics_tuple['true_positives'],
        metrics_tuple['true_negatives'],
        metrics_tuple['false_positives'],
        metrics_tuple['false_negatives'],
        metrics_tuple['total_samples'],
        metrics_tuple['accuracy'],
        metrics_tuple['precision'],
        metrics_tuple['sensitivity'],
        metrics_tuple['specificity'],
        metrics_tuple['true_positive_rate'],
        metrics_tuple['false_positive_rate'],
        metrics_tuple['f1_score']
    )

    return model