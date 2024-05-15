import mysql.connector

class Database:
    """
    Class: Database
    
    Packages: mysql-connector-python
    """

    def __init__(self):
        self.db = self.connect()

    def connect(self):
        """
        Establish a connection to the MySQL database.
        """
        return mysql.connector.connect(user=self.username(),
                                    password=self.password(),                              
                                    host=self.ip(),
                                    database=self.name(),
                                    auth_plugin='mysql_native_password')

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
                self.db.cursor().execute(command)
            except:
                print("Erro ao executar")

    def execute(self, query : str):
        """
        Execute SQL query.
        """
        try:
            self.db.cursor().execute(query)
        except:
            print("Can't run!")

    def name(self):
        """
        Returns the name of the MySQL database.
        """
        return "eeg_data"

    def username(self):
        """
        Returns the username used for connecting to the MySQL database.
        """
        return "root"

    def password(self):
        """
        Returns the password used for connecting to the MySQL database.
        """
        return "luiz"

    def ip(self):
        """
        Returns the IP address or hostname of the MySQL database server.
        """
        return "127.0.0.1"