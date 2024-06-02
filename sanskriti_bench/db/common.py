import os 
import csv
import shutil
import sqlite3
import logging 

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DataBaseContextManager:
    def __init__(self, database_name: str) -> None:
        self.database_name = database_name
    
    def __enter__(self):
        self.conn = sqlite3.connect(self.database_name+".db")
        self.cursor = self.conn.cursor()
        return self.cursor
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            logger.error("An error occurred:", exc_info=(exc_type, exc_val, exc_tb))
        self.conn.commit() 
        self.conn.close() 


def create_database(database_name: str):
    try:
        with DataBaseContextManager(database_name=database_name) as cursor:
            pass
        logger.info(f"Database '{database_name}' created successfully.")
        return True
    except Exception as e:
        logger.error(f"Failed to create database '{database_name}': {e}")
        return False 


def backup_database(database_name: str, backup_path: str):
    if not os.path.isdir(backup_path):
        os.makedirs(backup_path, exist_ok=True)
    try:
        shutil.copyfile(database_name + ".db", os.path.join(backup_path, database_name + ".db"))
        logger.info(f"Database '{database_name}' backed up successfully to '{backup_path}'.")
        return True
    except Exception as e:
        logger.error(f"Failed to backup database '{database_name}': {e}")
        return False 


def restore_database(backup_path: str, restored_database_name: str):
    try:
        shutil.copyfile(backup_path, restored_database_name + ".db")
        logger.info(f"Database '{restored_database_name}' restored successfully from '{backup_path}'.")
        return True
    except Exception as e:
        logger.error(f"Failed to restore database '{restored_database_name}': {e}")
        return False 

def import_from_csv(database_name: str, table_name: str, csv_file_path: str):
    try:
        with open(csv_file_path, "r") as file:
            csv_reader = csv.reader(file)
            next(csv_reader)
            data_to_insert = [tuple(row) for row in csv_reader]
        with DataBaseContextManager(database_name=database_name) as cursor:
            cursor.executemany(f"INSERT INTO {table_name} VALUES (?, ?, ?, ?, ?)", data_to_insert)
        logger.info(f"Data imported successfully from '{csv_file_path}' into table '{table_name}'.")
        return True 
    except Exception as e:
        logger.error(f"Failed to import data from CSV into table '{table_name}': {e}")
        return False 

# TODO: Instead of full path export, make it a tempfile  
def export_data_to_csv(database_name: str, table_name: str, csv_file_path: str):
    try:
        with DataBaseContextManager(database_name) as cursor:
            cursor.execute(f"SELECT * FROM {table_name}")
            rows = cursor.fetchall()

        with open(csv_file_path, 'w', newline='') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(["SID", "Contributor Email", "Language", "Question", "Answer", "Created At"])
            csv_writer.writerows(rows)
        logger.info(f"Data exported successfully from table '{table_name}' to '{csv_file_path}'.")
        return True 
    except Exception as e:
        logger.error(f"Failed to export data from table '{table_name}' to CSV: {e}")
        return False 


def db_exists(db_path: str):
    return os.path.exists(db_path)

def table_exists(db_path: str, table_name: str):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    return cursor.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name=?", (table_name,)
    ).fetchone() is not None 
