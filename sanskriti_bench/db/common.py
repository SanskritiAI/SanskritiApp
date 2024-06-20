import logging 
import psycopg2

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DataBaseContextManager:
    def __init__(self, payload: dict):
        self._payload = payload 
    
    def __enter__(self):
        self.conn = psycopg2.connect(
            dbname=self._payload["db_name"],
            user=self._payload["user"],
            password=self._payload["password"],
            host=self._payload["host"],
            port=self._payload["port"]
        )
        self.cursor = self.conn.cursor()
        return self.cursor
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            logger.error(
                "An error occurred:", exc_info=(exc_type, exc_val, exc_tb)
            )
        self.cursor.connection.commit()
        self.cursor.close()
        self.conn.close()


