import streamlit as st 
from sanskriti_bench.db.auth import AuthTable
from sanskriti_bench.db.data import DataTable
from sanskriti_bench.settings import AUTH_TABLE_NAME, DATA_TABLE_NAME

connection_ip=st.secrets.connection_ip
user=st.secrets.user 
password=st.secrets.password
db_name=st.secrets.db_name 
port=st.secrets.db_port

payload={
    "host": connection_ip,
    "user": user,
    "password": password,
    "db_name": db_name,
    "port": port 
}

auth = AuthTable(payload=payload, table_name=AUTH_TABLE_NAME)
auth._create_user_table()
status = auth.insert_new_user(
    data={
        "email": "proanindyadeep@gmail.com",
        "user_name": "anindya_admin",
        "name": "Anindyadeep",
        "password": "anindya_admin", 
        "language": "Bengali",
        "role": "admin",
        "region": "West Bengal",
        "affiliation": "null"
    }
)
print("TEST USER TABLE CREATION STATUS: ", status)
status = auth.insert_new_user(
    data={
        "email": "proanindyadeep@gmail.com",
        "user_name": "anindya_contri",
        "name": "Anindyadeep",
        "password": "anindya_contri", 
        "language": "Bengali",
        "role": "contributor",
        "region": "West Bengal",
        "affiliation": "null"
    }
)
print("TEST USER TABLE CREATION STATUS: ", status)

data = DataTable(payload=payload, table_name=DATA_TABLE_NAME)
data._create_data_table()

status = data.insert_new_data(
    data={
        "user_name": "anindya_contri",
        "language": "Bengali",
        "question": "Hello how are you",
        "answer": "I am good",
    }
)

print("TEST DATA TABLE CREATION STATUS: ", status)


