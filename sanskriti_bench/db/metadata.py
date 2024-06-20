from sanskriti_bench.db.base import BaseModel

# This MetaData DB acts as an accesible log store
# and also help us to do some more additional operations 

class MetaDataTable(BaseModel):
    def __init__(self, payload: dict, table_name: str):
        super().__init__(payload=payload, table_name=table_name)
    
    def _create_metadata_table(self) -> bool:
        self.create_table(
            fields_dict={
                "mid": ("SERIAL", "PRIMARY KEY"),
                "table_name": ("TEXT", "NOT NULL"),
                "id_type": ("TEXT", "NOT NULL"),
                "action": ("TEXT", "NOT NULL"),
                "created_at": ("TIMESTAMPTZ", "DEFAULT CURRENT_TIMESTAMP")
            }
        ) 
    
    def capture_event(self, table: str, id_type: str, action: str):
        assert id_type in ["sid", "uid"], "id_type can be either sid or uid"
        assert action in ["insert", "delete", "alter"], "action can be either insert, delete or alter"

        return self.insert(
            data={
                "table_name": table,
                "id_type": id_type,
                "action": action
            }
        ) 