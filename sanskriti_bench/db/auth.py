from typing import Union
from sanskriti_bench.db.common import logger
from sanskriti_bench.db.base import BaseModel

class AuthTable(BaseModel):
    def __init__(self, payload: dict, table_name: str) -> None:
        super().__init__(payload=payload, table_name=table_name) 
    
    def _create_user_table(self) -> bool:
        self.create_table(
            fields_dict={
                "uid": ("SERIAL", "PRIMARY KEY"),
                "email": ("TEXT", "NOT NULL"),
                "user_name": ("TEXT", "NOT NULL"),
                "name": ("TEXT", "NOT NULL"),
                "password": ("TEXT", "NOT NULL"),
                "language": ("TEXT", "NOT NULL"),
                "role": ("TEXT", "NOT NULL"),
                "region": ("TEXT", "NOT NULL"),
                "affiliation": ("TEXT", "NOT NULL"),
                "created_at": ("TIMESTAMPTZ", "DEFAULT CURRENT_TIMESTAMP")
            }
        )
    
    def insert_new_user(self, data: dict) -> bool:
        return self.insert(data=data)
    
    def export_all_users_as_st_auth_dict(self) -> dict:
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
        rows, _ = self.fetch()
        if (rows is None) or len(rows) == 0:
            logger.warn("Table is empty")
            return dict_skeleton
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
    
    def fetch_all_users(self):
        return self.fetch()
    
    def fetch_all_users_by_lang(self, language: str):
        return self.fetch(
            key="language", value=language
        ) 
    
    def fetch_all_users_by_role(self, role: str):
        rows, _ = self.fetch(
            columns=["user_name", "role"], key="role", value=role
        )
        if rows is None or len(rows) == 0:
            logger.warn("Nothing fetched")
            return None 
        users = {name: role for name, role in rows}
        return users 
    
    def alter_user_information(self, user_name: str, key: str, value: str):
        return self.alter_table(
            select_by=user_name, key=key, value=value
        )
    
    def delete_by_id(self, user_name_or_id: Union[int, str]):
        key = "uid" if isinstance(user_name_or_id, int) else "user_name"
        return self.delete_entry(key=key, value=user_name_or_id)
    
    def get_all_user_info(self, user_name_or_id: Union[int, str]):
        key = "uid" if isinstance(user_name_or_id, int) else "user_name"
        return self.fetch(key=key, value=user_name_or_id)