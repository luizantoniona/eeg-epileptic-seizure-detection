import sqlite3

class Database:
    """
    Class: Database
    
    Packages: sqlite3
    """

    def __init__(self):
        self.db = self.connect()
        self.db.row_factory = sqlite3.Row
        self.cursor = self.db.cursor()

    def connect(self):
        """
        Establish a connection to the SQLite database.
        """
        return sqlite3.connect("data/" + self.name() + '.db')

    def execute_from_file(self, filename):
        """
        Execute SQL commands from a file.
        """
        fd = open(filename, 'r')
        sql_file = fd.read()
        fd.close()

        sql_commands = sql_file.split(';')

        for command in sql_commands:
            try:
                self.cursor.execute(command)
            except:
                print("Erro ao executar")

    def verify_table(self, table_name) -> bool:
        fd = open("./Database/SQL/Structure/verify_table_by_name.sql", 'r')
        sql_file = fd.read()
        fd.close()

        try:
            self.cursor.execute(sql_file, (table_name,))
            return self.cursor.fetchone()
        except:
            return False

    @staticmethod
    def name():
        """
        Returns the name of the SQLite database.
        """
        return "eeg_data"
