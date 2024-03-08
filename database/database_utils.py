"""
Module: databaseutils

This module provides a set of functions for interacting with a MySQL database, specifically designed for managing and retrieving summary data related to records.

The module includes functions for establishing a database connection, executing SQL commands from files, inserting summary data, and retrieving summary information from the database.
"""

import mysql.connector
import database.database_info as dbinfo

def connect():
    """
    Establish a connection to the MySQL database.
    """
    return mysql.connector.connect(user=dbinfo.username(),
                              password=dbinfo.password(),                              
                              host=dbinfo.ip(),
                              database=dbinfo.name(),
                              auth_plugin='mysql_native_password')

def execute_from_file(filename):
    """
    Execute SQL commands from a file.
    """
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
    """
    Insert summary data into the database.
    """
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
    """
    Retrieve summary data from the database based on the file name.
    """
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

def summaries():
    """
    Retrieve all summary data from the database.
    """
    fd = open("./database/sql/select_all_summaries.sql", 'r')
    sql_file = fd.read()
    fd.close()

    db = connect()
    cursor = db.cursor(buffered=True, dictionary=True)

    try:
        cursor.execute(sql_file)
        return cursor.fetchall()
    except:
        print("Não há registros")

def summaries_with_anomaly():
    """
    Retrieve all summary data with anomaly information from the database.
    """
    fd = open("./database/sql/select_all_summaries_with_anomaly.sql", 'r')
    sql_file = fd.read()
    fd.close()

    db = connect()
    cursor = db.cursor(buffered=True, dictionary=True)

    try:
        cursor.execute(sql_file)
        return cursor.fetchall()
    except:
        print("Não há registros")

def insert_metrics_data(model_name, model_data_domain,
                        accuracy, precision, sensitivity, specificity, true_positive_rate, false_positive_rate, f1_score,
                        true_positives, true_negatives, false_positives, false_negatives, total_samples ):
    """
    Insert metrics data into the database.
    """
    fd = open("./database/sql/insert_metrics_info.sql", 'r')
    sql_file = fd.read()
    fd.close()

    db = connect()

    try:
        db.cursor().execute(sql_file, [model_name, model_data_domain,
                                       accuracy, precision, sensitivity, specificity, true_positive_rate, false_positive_rate, f1_score,
                                       true_positives, true_negatives, false_positives, false_negatives, total_samples ])
        db.commit()
    except:
        print("Não foi possível inserir")
        