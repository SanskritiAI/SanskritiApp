from tabulate import tabulate
from sanskriti_bench.db.common import logger, DataBaseContextManager

def create_table(database_name: str, table_name: str):
    try:
        with DataBaseContextManager(
            database_name=database_name
        ) as cursor:
            cursor.execute(
                f"""CREATE TABLE IF NOT EXISTS {table_name} (
                    sid INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_name TEXT NOT NULL, 
                    language TEXT NOT NULL,
                    question TEXT NOT NULL, 
                    answer TEXT NOT NULL,
                    created_at DATETIME DEFAULT CURRENT_TIMESTAMP 
                )
                """
            )
        logger.info(f"Table '{table_name}' created successfully.")
        return True 
    except Exception as e:
        logger.error(f"Failed to create table '{table_name}': {e}")
        return False 

def insert(database_name: str, table_name: str, values: dict):
    try:
        with DataBaseContextManager(database_name) as cursor:
            user_name = values.get("user_name", "null")
            language = values.get("language", "null")
            question = values.get("question", "null")
            answer = values.get("answer", "null")
            values_to_insert = (user_name, language, question, answer)

            cursor.execute(
                f"""INSERT INTO {table_name} (
                    user_name, language, question, answer
                ) VALUES (?, ?, ?, ?)
                """, values_to_insert
            )
        logger.info("Data inserted successfully.")
        return True 
    except Exception as e:
        logger.error(f"Failed to insert data into table '{table_name}': {e}")
        return False 


def read_table(database_name: str, table_name: str):
    try:
        with DataBaseContextManager(database_name) as cursor:
            cursor.execute(f"SELECT * FROM {table_name}")
            rows = cursor.fetchall()

        if len(rows) == 0:
            print("No data available in the table.")
        else:
            headers = ["SID", "Contributor Email", "Language", "Question", "Answer", "Created At"]
            print(tabulate(rows, headers=headers, tablefmt="grid"))
        logger.info(f"Data retrieved from table '{table_name}' successfully.")
    except Exception as e:
        logger.error(f"Failed to read data from table '{table_name}': {e}")



# Stats based functions 

def get_total_contributions_all_languages(database_name: str, table_name: str):
    try:
        with DataBaseContextManager(database_name=database_name) as cursor:
            cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
            total_contributions = cursor.fetchone()[0]
    except Exception as e:
        logger.error(f"Failed to get total contributions across all languages: {e}")
        total_contributions = None 
    return total_contributions
        

def get_all_contributions_by_contributor(database_name: str, table_name: str, user_name: str):
    try:
        with DataBaseContextManager(database_name) as cursor:
            cursor.execute(f"SELECT question, answer, created_at FROM {table_name} WHERE user_name=?", (user_name,))
            contributions = cursor.fetchall()
            headers = [desc[0] for desc in cursor.description]
        logger.info(f"Contributions by contributor '{user_name}' retrieved successfully")
        return contributions, headers
    except Exception as e:
        logger.error(f"Failed to get total contributions by contributor '{user_name}': {e}")
        return None, None


