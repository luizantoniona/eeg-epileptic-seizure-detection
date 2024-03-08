CREATE TABLE metrics_info
(
    model_name VARCHAR(20),
    model_data_domain VARCHAR(20),
    accuracy FLOAT,
    `precision` FLOAT,
    sensitivity FLOAT,
    specificity FLOAT,
    true_positive_rate FLOAT,
    false_positive_rate FLOAT,
    f1_score FLOAT,
    true_positives INTEGER,
	true_negatives INTEGER,
	false_positives INTEGER,
	false_negatives INTEGER,
	total_samples INTEGER
);