import streamlit as st 

# ---- Table Names ----
AUTH_TABLE_NAME="test_auth_v2"
DATA_TABLE_NAME="test_contributions_v2"
METADATA_TABLE_NAME="test_meta"

# ---- Roles ----
ROLES = [
    "contributor", 
    "manager", 
    "admin"
]

# ---- Supported Languages ----
LANGUAGES = [
    "Maithili", "Odia", "Hindi", "Bengali", "Punjabi", "Assamese", "Gujarati",
    "Kannada", "Kashmiri", "Konkani", "Malayalam", "Manipuri", "Marathi",
    "Sanskrit", "Tamil", "Telugu",
    "Rajasthani"
]

# ---- Supported States ----
ALL_INDIAN_STATES = [
    "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh",
    "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand", "Karnataka",
    "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya", "Mizoram",
    "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu",
    "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal",
    "Andaman and Nicobar Islands", "Chandigarh", "Dadra and Nagar Haveli and Daman and Diu",
    "Lakshadweep", "Delhi", "Puducherry", "Ladakh", "Jammu and Kashmir"
]

# ---- Payload ----
connection_ip=st.secrets.connection_ip
user=st.secrets.user 
password=st.secrets.password
db_name=st.secrets.db_name 
port=st.secrets.db_port

db_payload={
    "host": connection_ip,
    "user": user,
    "password": password,
    "db_name": db_name,
    "port": port 
}



