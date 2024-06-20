from typing import Optional, Union 
from sanskriti_bench.db.common import logger, DataBaseContextManager

class BaseModel:
    def __init__(self, payload: dict, table_name: str) -> None:
        self._payload = payload
        self.table_name = table_name
    
    def create_table(self, fields_dict: dict) -> bool:
        fields_str = ",\n".join([f"    {field} {data_type} {constraint}" for field, (data_type, constraint) in fields_dict.items()])
        sql_string = f"""CREATE TABLE IF NOT EXISTS {self.table_name} ({fields_str});
        """
        try:
            with DataBaseContextManager(self._payload) as cursor:
                cursor.execute(sql_string)
            logger.info(f"Table '{self.table_name}' created successfully.")
            return True
        except Exception as e:
            logger.error(f"Failed to create table '{self.table_name}': {e}")
            return False 
    
    def insert(self, data: dict):
        keys = list(data.keys())
        values_to_insert = tuple([data.get(key, None) for key in keys])
        keys_string = ", ".join(keys)
        value_placeholder_str = ", ".join(["%s"]*len(keys))

        sql_string = f"""INSERT INTO {self.table_name} (
            {keys_string}    
        ) VALUES ({value_placeholder_str})
        """
        try:
            with DataBaseContextManager(self._payload) as cursor:
                cursor.execute(sql_string, values_to_insert)
            logger.info(f"Data inserted successfully in table: {self.table_name}")
            return True 
        except Exception as e:
            logger.error(f"Failed to insert data into table '{self.table_name}': {e}")
            return False 

    def fetch(
        self,
        columns: Optional[Union[str, list]] = None,
        key: Optional[str] = None,
        value: Optional[str] = None,
    ):
        # handle columns
        columns = "*" if columns is None else columns
        if isinstance(columns, str):
            columns = [columns]
        columns_str = columns if columns == "*" else ", ".join(columns)

        # handle conditional
        assert (key is None) == (value is None), "Both key and value must be None or neither."

        if key and value:
            sql_string = f"SELECT {columns_str} FROM {self.table_name} WHERE {key} = %s"
        else:
            sql_string = f"SELECT {columns_str} FROM {self.table_name}"

        # Final execution from cursor
        rows, columns_names = None, None
        try:
            with DataBaseContextManager(self._payload) as cursor:
                if key and value:
                    cursor.execute(sql_string, (value,))
                else:
                    cursor.execute(sql_string)
                rows = cursor.fetchall()
                columns_names = [desc[0] for desc in cursor.description]
            logger.info(f"Fetched successfully from table: {self.table_name}")
        except Exception as e:
            logger.error(f"Unable to fetch data from table '{self.table_name}': {e}")
        return rows, columns_names         

    def get_count(self, key: Optional[str] = None, value: Optional[str] = None) -> int:
        assert (key is None) == (value is None), "Both key and value must be None or neither."

        if key and value:
            sql_string = f"SELECT COUNT(*) FROM {self.table_name} WHERE {key} = %s"
        else:
            sql_string = f"SELECT COUNT(*) FROM {self.table_name}"

        count = 0
        try:
            with DataBaseContextManager(self._payload) as cursor:
                if key and value:
                    cursor.execute(sql_string, (value,))
                else:
                    cursor.execute(sql_string)
                count = cursor.fetchone()[0]
            logger.info(f"Count fetched successfully from table: {self.table_name}")
        except Exception as e:
            logger.error(f"Unable to fetch count from table '{self.table_name}': {e}")
        return count 
    
    def alter_table(self, select_by: str, key: str, value: str):
        try:
            with DataBaseContextManager(self._payload) as cursor:
                cursor.execute(
                    f"""UPDATE {self.table_name} SET {key} = %s WHERE {select_by} = %s""",(value, select_by)
                )
            logger.info(f"Table: {self.table_name} altered successfully")
            return True 
        except Exception as e:
            logger.info(f"Unable to alter table: {self.table_name}: {e}")
            return False
    
    def delete_entry(self, key: str, value: str):
        try:
            with DataBaseContextManager(self._payload) as cursor:
                cursor.execute(
                    f"""DELETE FROM {self.table_name} WHERE {key}=%s
                    """, (value)
                ) 
            logger.info(f"Deleted {key} | {value} from table: {self.table_name}")
            return True 
        except Exception as e:
            logger.error(f"Failed to delete entry in table: {self.table_name}")
            return False 