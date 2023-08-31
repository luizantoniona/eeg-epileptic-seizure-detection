import mysql.connector
import database.databaseinfo as dbinfo

def connect():
    return mysql.connector.connect(user=dbinfo.username(),
                              password=dbinfo.password(),                              
                              host=dbinfo.ip(),
                              database=dbinfo.name(),
                              auth_plugin='mysql_native_password')

def execute_from_file(filename):
    fd = open(filename, 'r')
    sql_file = fd.read()
    fd.close()

    db = connect()

    sql_commands = sql_file.split(';')

    for command in sql_commands:
        try:
            db.cursor().execute(command)
        except:
            print("Erro ao executar")

def insert_sumarry_data(record_name, file_name, start_time, end_time, nr_seizures, start_seizure, end_seizure, nr_channels, ds_channels ):

    fd = open("./database/sql/insert_summary_info.sql", 'r')
    sql_file = fd.read()
    fd.close()

    db = connect()

    command = sql_file

    try:
        db.cursor().execute(command, [record_name, file_name, start_time, end_time, nr_seizures, start_seizure, end_seizure, nr_channels, ds_channels ])
        db.commit()
    except:
        print("Registro já existe")