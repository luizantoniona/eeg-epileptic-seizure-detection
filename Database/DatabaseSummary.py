from Database.Database import Database


class DatabaseSummary(Database):
    """
    Class: DatabaseSummary
    """

    def __init__(self):
        super().__init__()

    def insert_sumarry_data(self, dataset_name, record_name, file_name, start_time, end_time, nr_occurrence, start_occurrence, end_occurrence, nr_channels, ds_channels, disease_type):
        """
        Insert summary data into the database.
        """
        fd = open("./Database/SQL/Summary/insert_summary.sql", "r")
        sql_file = fd.read()
        fd.close()

        try:
            self.cursor.execute(
                sql_file,
                (
                    dataset_name,
                    record_name,
                    file_name,
                    start_time,
                    end_time,
                    nr_occurrence,
                    start_occurrence,
                    end_occurrence,
                    nr_channels,
                    ds_channels,
                    disease_type,
                ),
            )
            self.db.commit()

        except:
            print("Registro já existe:", file_name)

    def summary_by_name(self, file_name) -> object:
        """
        Retrieve summary data from the database based on the file name.
        """
        fd = open("./Database/SQL/Summary/select_summary_by_name.sql", "r")
        sql_file = fd.read()
        fd.close()

        try:
            self.cursor.execute(sql_file, (file_name,))
            return self.cursor.fetchone()

        except:
            print("Não há registro para o nome:", file_name)

    def summaries(self, dataset_name) -> list[object]:
        """
        Retrieve all summary data from the database.
        """
        fd = open("./Database/SQL/Summary/select_all_summaries.sql", "r")
        sql_file = fd.read()
        fd.close()

        try:
            self.cursor.execute(sql_file, (dataset_name,))
            return self.cursor.fetchall()

        except:
            print("Não há registros")
            return []

    def summaries_with_anomaly(self, dataset_name) -> list[object]:
        """
        Retrieve all summary data with anomaly information from the database.
        """
        fd = open("./Database/SQL/Summary/select_all_summaries_with_anomaly.sql", "r")
        sql_file = fd.read()
        fd.close()

        try:
            self.cursor.execute(sql_file, (dataset_name,))
            return self.cursor.fetchall()

        except:
            print("Não há registros")
            return []
