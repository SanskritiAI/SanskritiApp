from sanskriti_bench.db.base import BaseModel

class DataTable(BaseModel):
    def __init__(self, payload: dict, table_name: str):
        super().__init__(payload=payload, table_name=table_name)

    def _create_data_table(self) -> bool:
        self.create_table(
            fields_dict={
                "sid": ("SERIAL", "PRIMARY KEY"),
                "user_name": ("TEXT", "NOT NULL"),
                "language": ("TEXT", "NOT NULL"),
                "question": ("TEXT", "NOT NULL"),
                "answer": ("TEXT", "NOT NULL"),
                "created_at": ("TIMESTAMPTZ", "DEFAULT CURRENT_TIMESTAMP")
            }
        ) 
    
    def insert_new_data(self, data: dict):
        return self.insert(data=data)
    
    def get_all_contributions_all_languages(self):
        count = self.get_count()
        return count 
    
    def get_all_contributions_by_contributor(self, user_name: str):
        rows, column_names = self.fetch(
            columns=["question", "answer", "created_at"],
            key="user_name",
            value=user_name
        ) 
        return rows, column_names