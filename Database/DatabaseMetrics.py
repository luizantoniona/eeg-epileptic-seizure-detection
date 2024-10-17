from Database.Database import Database


class DatabaseMetrics(Database):
    """
    Class: DatabaseMetrics
    """

    def __init__(self):
        super().__init__()

    def insert_metrics_data(
        self,
        dataset_name,
        model_name,
        model_data_domain,
        model_window_length,
        accuracy,
        precision,
        sensitivity,
        specificity,
        true_positive_rate,
        false_positive_rate,
        f1_score,
        true_positives,
        true_negatives,
        false_positives,
        false_negatives,
        total_samples,
    ):
        """
        Insert metrics data into the database.
        """
        fd = open("./Database/SQL/Metrics/insert_metric.sql", "r")
        sql_file = fd.read()
        fd.close()

        try:
            self.cursor.execute(
                sql_file,
                (
                    dataset_name,
                    model_name,
                    model_data_domain,
                    model_window_length,
                    accuracy,
                    precision,
                    sensitivity,
                    specificity,
                    true_positive_rate,
                    false_positive_rate,
                    f1_score,
                    true_positives,
                    true_negatives,
                    false_positives,
                    false_negatives,
                    total_samples,
                ),
            )
            self.db.commit()
        except:
            print("DatabaseMetrics [ERROR]")

    def metrics_by_model_domain_window(self, dataset_name, model_name, domain_name, window_length) -> list[object]:
        """
        Retrieve metrics by model, domain and window_length.
        """
        fd = open("./Database/SQL/Metrics/select_metrics_by_model_domain_window.sql", "r")
        sql_file = fd.read()
        fd.close()

        try:
            self.cursor.execute(
                sql_file,
                (
                    dataset_name,
                    model_name,
                    domain_name,
                    window_length,
                ),
            )
            return self.cursor.fetchall()

        except:
            print("DatabaseMetrics [EMPTY]")
            return []
