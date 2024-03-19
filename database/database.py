"""

"""

import mysql.connector
import database.database_info as dbinfo

class Database:

    def __init__(self):
        self.db = self.connect()

    def connect(self):
        """
        Establish a connection to the MySQL database.
        """
        return mysql.connector.connect(user=dbinfo.username(),
                                    password=dbinfo.password(),                              
                                    host=dbinfo.ip(),
                                    database=dbinfo.name(),
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