from Database.Database import Database

class DatabaseSummary( Database ):
    """

    """

    def __init__(self):
        super().__init__()

    def insert_sumarry_data(self, record_name, file_name, start_time, end_time,
                            nr_occurrence, start_occurrence, end_occurrence, nr_channels, ds_channels, disease_type ):
        """
        Insert summary data into the database.
        """
        fd = open("./Database/SQL/Summary/insert_summary.sql", 'r')
        sql_file = fd.read()
        fd.close()

        try:
            self.db.cursor().execute(sql_file, (record_name, file_name, start_time, end_time,
                                                nr_occurrence, start_occurrence, end_occurrence, nr_channels, ds_channels, disease_type ))
            self.db.commit()
        except:
            print("Registro já existe")

    def summary_by_name(self, file_name):
        """
        Retrieve summary data from the database based on the file name.
        """
        fd = open("./Database/SQL/Summary/select_summary_by_name.sql", 'r')
        sql_file = fd.read()
        fd.close()

        cursor = self.db.cursor(buffered=True, dictionary=True)

        try:
            cursor.execute(sql_file, [file_name])
            return cursor.fetchone()
        except:
            print("Não há registro para o nome")

    def summaries(self):
        """
        Retrieve all summary data from the database.
        """
        fd = open("./Database/SQL/Summary/select_all_summaries.sql", 'r')
        sql_file = fd.read()
        fd.close()

        cursor = self.db.cursor(buffered=True, dictionary=True)

        try:
            cursor.execute(sql_file)
            return cursor.fetchall()
        except:
            print("Não há registros")

    def summaries_with_anomaly(self):
        """
        Retrieve all summary data with anomaly information from the database.
        """
        fd = open("./Database/SQL/Summary/select_all_summaries_with_anomaly.sql", 'r')
        sql_file = fd.read()
        fd.close()

        cursor = self.db.cursor(buffered=True, dictionary=True)

        try:
            cursor.execute(sql_file)
            return cursor.fetchall()
        except:
            print("Não há registros")