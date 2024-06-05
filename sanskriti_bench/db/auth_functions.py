from typing import Union
from sanskriti_bench.db.common import logger, DataBaseContextManager

# TODO: We might need to make some update functions 

def create_table(database_name: str, table_name: str) -> bool:
    try:
        with DataBaseContextManager(
            database_name=database_name
        ) as cursor:
            cursor.execute(
                f"""CREATE TABLE IF NOT EXISTS {table_name} (
                    uid INTEGER PRIMARY KEY AUTOINCREMENT, 
                    email TEXT NOT NULL,
                    user_name TEXT NOT NULL, 
                    name TEXT NOT NULL, 
                    password TEXT NOT NULL,
                    language TEXT NOT NULL, 
                    role TEXT NOT NULL, 
                    affiliation TEXT,
                    created_at DATETIME DEFAULT CURRENT_TIMESTAMP 
                )
                """
            )
        logger.info(f"Table '{table_name}' created successfully.")
        return True 
    except Exception as e:
        logger.error(f"Failed to create table '{table_name}': {e}")
        return False 

def create_new_user(database_name: str, table_name: str, values: dict) -> bool:
    try:
        with DataBaseContextManager(
            database_name=database_name
        )  as cursor:
            keys = ["email", "user_name", "name", "password", "language", "role", "affiliation"]
            values_to_insert = tuple([
                values.get(key, "null") for key in keys
            ])            
            cursor.execute(
                f"""INSERT INTO {table_name} (
                    email, user_name, name, password, language, role, affiliation
                ) VALUES (?, ?, ?, ?, ?, ?, ?)
                """, values_to_insert
            )
        logger.info("Data inserted successfully.")
        return True 
    except Exception as e:
        logger.error(f"Failed to insert data into table '{table_name}': {e}")
        return False 


def get_all_users_and_export_as_dict(database_name: str, table_name: str) -> Union[dict, None]:
    dict_skeleton = {
        "credentials": {
            "usernames":{}
        },
            "cookie": {
            "expiry_days": 30,
            "key": "some_signature_key",
            "name": "some_cookie_name"
        }
    }
    try:
        with DataBaseContextManager(
            database_name=database_name
        ) as cursor:
            cursor.execute(f"SELECT * FROM {table_name}")
            rows = cursor.fetchall()
        
        if len(rows) == 0:
            logger.warn("Table is empty")
        else:
            for row in rows:
                email, user_name, name, password = row[1:5] 
                dict_skeleton["credentials"]["usernames"][user_name] = {
                    "email": email, 
                    "failed_login_attempts": 0,
                    "logged_in": False,
                    "name": name, 
                    "password": password
                }
        return dict_skeleton
    except Exception as e:
        logger.error(f"Failed to read data from table '{table_name}': {e}")
        return None 


def fetch_all_users(database_name: str, table_name: str):
    try:
        with DataBaseContextManager(
            database_name=database_name
        ) as cursor:
            cursor.execute(f"SELECT * FROM {table_name}")
            rows = cursor.fetchall()
            columns = [desc[0] for desc in cursor.description]
        return rows, columns
    except Exception as e:
        logger.error(f"Failed to read data from table '{table_name}': {e}")
        return None, None 

def fetch_all_users_by_lang(database_name: str, table_name: str, language: str):
    try:
        with DataBaseContextManager(
            database_name=database_name
        ) as cursor:
            cursor.execute(
                f"SELECT * FROM {table_name} WHERE language=?",
                (language,)
            )
            rows = cursor.fetchall()
            columns = [desc[0] for desc in cursor.description]
        return rows, columns
    except Exception as e:
        logger.error(f"Failed to read data from table '{table_name}': {e}")
        return None, None 


def get_all_user_by_role(database_name: str, table_name: str, role: str):
    try:
        with DataBaseContextManager(
            database_name=database_name
        ) as cursor:
            cursor.execute(
                f"""SELECT user_name, language FROM {table_name} WHERE role=?""",
                (role,)  
            )
            rows = cursor.fetchall()
            users = {name: lang for name, lang in rows}
            return users            
    except Exception as e:
        logger.error(f"Failed to fetch admins: {e}")
        return None 

def get_all_rows_of_column(database_name: str, table_name: str, column_name: str):
    try:
        with DataBaseContextManager(
            database_name=database_name
        ) as cursor:
            cursor.execute(
                f"""SELECT {column_name} FROM {table_name}""" 
            )
            rows = cursor.fetchall()
            return rows          
    except Exception as e:
        logger.error(f"Failed to fetch admins: {e}")
        return None


def fetch_lang_table(database_name: str, table_name: str, language: str):
    try:
        with DataBaseContextManager(
            database_name=database_name
        ) as cursor:
            cursor.execute(
                f"""SELECT * FROM {table_name} WHERE language=?
                """, (language,)
            )
            rows = cursor.fetchall()
            columns = [desc[0] for desc in cursor.description]
            return rows, columns
    except Exception as e:
        logger.error(f"Failed to fetch admins: {e}")
        return None, None 

def alter_user_information(
        database_name: str, 
        table_name: str, 
        user_name_or_id: str,
        key: str, 
        value: str 
):
    print("=======")
    print(value)
    print(user_name_or_id)
    print("***********")

    if isinstance(user_name_or_id, str):
        selection_by = "user_name"
    else:
        selection_by = "uid"
    
    SQL = f"""UPDATE {table_name} SET {key} = ? WHERE {selection_by} = ?
    """
    try:
        with DataBaseContextManager(
            database_name=database_name
        ) as cursor:
            cursor.execute(SQL, (value, user_name_or_id,))
            return True  
    except Exception as e:
        logger.error(f"Unable to alter unser info. Reason: {e}")
        return False 



def delete_by_id(database_name: str, table_name: str, user_name_or_id: Union[str, int]):
    if isinstance(user_name_or_id, int):
        key = "user_name"
    else:
        key = "uid"
    try:
        with DataBaseContextManager(
            database_name=database_name
        ) as cursor:
            cursor.execute(
                f"""DELETE FROM {table_name} WHERE {key} = ?
                """, (user_name_or_id,)
            )
        return True 
    except Exception as e:
        logger.error(f"Not able to delete user/id: {user_name_or_id} reason: {e}")
        return False 


def get_full_user_info(database_name: str, table_name: str, user_name_or_id: Union[str, int]):
    if isinstance(user_name_or_id, int):
        key = "user_name"
    else:
        key = "uid"
    
    try:
        with DataBaseContextManager(
            database_name=database_name
        ) as cursor:
            cursor.execute(
                f"""SELECT * FROM {table_name} WHERE {key} = ?
                """, (user_name_or_id, )
            )
            rows = cursor.fetchall()
            columns = [desc[0] for desc in cursor.description]
            return rows, columns 
    except Exception as e:
        logger.error(f"Error fetching user/id: {user_name_or_id} reason: {e}")
        return None, None  