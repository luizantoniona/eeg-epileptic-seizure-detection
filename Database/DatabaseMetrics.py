from Database.Database import Database

class DatabaseMetrics( Database ):
    """
    Class: DatabaseMetrics
    """

    def __init__(self):
        super().__init__()

    def insert_metrics_data(self, model_name, model_data_domain, model_window_length,
                            accuracy, precision, sensitivity, specificity,
                            true_positive_rate, false_positive_rate, f1_score,
                            true_positives, true_negatives, false_positives, false_negatives, total_samples):
        """
        Insert metrics data into the database.
        """
        fd = open("./Database/SQL/Metrics/insert_metric.sql", 'r')
        sql_file = fd.read()
        fd.close()

        try:
            self.cursor.execute(sql_file, (model_name, model_data_domain, model_window_length,
                                                accuracy, precision, sensitivity, specificity,
                                                true_positive_rate, false_positive_rate, f1_score,
                                                true_positives, true_negatives, false_positives, false_negatives, total_samples,))
            self.db.commit()
        except:
            print("Não foi possível inserir")

    def metrics_by_domain(self, domain):
        """
        Retrieve metrics by domain.
        """
        fd = open("./Database/SQL/Metrics/select_metrics_by_domain.sql", 'r')
        sql_file = fd.read()
        fd.close()

        try:
            self.cursor.execute(sql_file, (domain,))
            return self.cursor.fetchall()
        except:
            print("Não há registros")
    
    def metrics_by_model(self, model_name):
        """
        Retrieve metrics by model.
        """
        fd = open("./Database/SQL/Metrics/select_metrics_by_model.sql", 'r')
        sql_file = fd.read()
        fd.close()

        try:
            self.cursor.execute(sql_file, (model_name,))
            return self.cursor.fetchall()
        except:
            print("Não há registros")

    def metrics_by_model_domain(self, model_name, domain_name):
        """
        Retrieve metrics by model and domain.
        """
        fd = open("./Database/SQL/Metrics/select_metrics_by_model_domain.sql", 'r')
        sql_file = fd.read()
        fd.close()

        try:
            self.cursor.execute(sql_file, (model_name, domain_name,))
            return self.cursor.fetchall()
        except:
            print("Não há registros")

    def metrics_by_model_domain_window(self, model_name, domain_name, window_length):
        """
        Retrieve metrics by model, domain and window_length.
        """
        fd = open("./Database/SQL/Metrics/select_metrics_by_model_domain_window.sql", 'r')
        sql_file = fd.read()
        fd.close()

        try:
            self.cursor.execute(sql_file, (model_name, domain_name, window_length,))
            return self.cursor.fetchall()
        except:
            print("Não há registros")

    def highest_accuracy(self, model_name, domain_name, window_length):
        """
        Retrieve metrics by model, domain and window_length.
        """
        fd = open("./Database/SQL/Metrics/select_metrics_with_highest_accuracy.sql", 'r')
        sql_file = fd.read()
        fd.close()

        try:
            self.cursor.execute(sql_file, (model_name, domain_name, window_length,))
            return self.cursor.fetchall()
        except:
            print("Não há registros")
            return None
