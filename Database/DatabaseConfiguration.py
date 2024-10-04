import os
from Database.Database import Database

def configure():
    database = Database()
    database.execute_from_file("./Database/SQL/Structure/create_table_summary_info.sql")
    database.execute_from_file("./Database/SQL/Structure/create_table_metrics_info.sql")

def is_configured() -> bool:
    database = Database()
    return database.verify_table("summary_info") and database.verify_table("metrics_info")
