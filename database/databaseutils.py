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

    try:
        db.cursor().execute(sql_file, [record_name, file_name, start_time, end_time, nr_seizures, start_seizure, end_seizure, nr_channels, ds_channels ])
        db.commit()
    except:
        print("Registro já existe")

def summary_by_name(file_name):
        
    fd = open("./database/sql/select_summary_by_name.sql", 'r')
    sql_file = fd.read()
    fd.close()

    db = connect()
    cursor = db.cursor(buffered=True, dictionary=True)

    try:
        cursor.execute(sql_file, [file_name])
        return cursor.fetchone()
    except:
        print("Não há registro para o nome")

def all_summary():

    fd = open("./database/sql/select_all_summary.sql", 'r')
    sql_file = fd.read()
    fd.close()

    db = connect()
    cursor = db.cursor(buffered=True, dictionary=True)

    try:
        cursor.execute(sql_file)
        return cursor.fetchall()
    except:
        print("Não há registros")