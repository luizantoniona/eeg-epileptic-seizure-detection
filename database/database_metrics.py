"""

"""

from database.database import Database

class DatabaseMetrics( Database ):

    def __init__(self):
        super().__init__()

    def insert_metrics_data(self, model_name, model_data_domain,
                            accuracy, precision, sensitivity, specificity, true_positive_rate, false_positive_rate, f1_score,
                            true_positives, true_negatives, false_positives, false_negatives, total_samples):
        """
        Insert metrics data into the database.
        """
        fd = open("./database/sql/insert_metrics_info.sql", 'r')
        sql_file = fd.read()
        fd.close()

        try:
            self.db.cursor().execute(sql_file, [model_name, model_data_domain,
                                                accuracy, precision, sensitivity, specificity, true_positive_rate, false_positive_rate, f1_score,
                                                true_positives, true_negatives, false_positives, false_negatives, total_samples ])
            self.db.commit()
        except:
            print("Não foi possível inserir")