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



# Links of spreadsheets

{
    "Maithili": "https://docs.google.com/spreadsheets/d/1e1YOTE3Z5pZ2sfVDe-5MPYFZ4D5yT6O-COUiEv5ykuk/edit?usp=sharing",
    "Odia": "https://docs.google.com/spreadsheets/d/1dQ_bzDtHlvd3R0-0YipVBfoKiB6630fnk9zQgfHpC0g/edit?usp=sharing",
    "Hindi": "https://docs.google.com/spreadsheets/d/1cznJL-NzHlaWCzoRiqKajchcHqmCwxvuPzUlINpc3rM/edit?usp=sharing",
    "Bengali": "https://docs.google.com/spreadsheets/d/1Dz1wvwizuBtudL8Z5XYS2YkJT0YGVnBhM_yvFxGXAT0/edit?usp=sharing",
    "Punjabi": "https://docs.google.com/spreadsheets/d/1J3lHKrvgs1HkAE5kiwLLt-0hC2Bvp2UwDfq9c0ItyE8/edit?usp=sharing",
    "Assamese": "https://docs.google.com/spreadsheets/d/1dhBFmUFuRoY4YuYlZBFWRdzZPsEI1s7uFt20Ttj4NWo/edit?usp=sharing",
    "Gujarati": "https://docs.google.com/spreadsheets/d/1rnwPLNHQtOjf5lwIL3C4jOMqUtl1l0ydEYXNK8O5JDo/edit?usp=sharing",
    "Kannada": "https://docs.google.com/spreadsheets/d/1CsQw5Dm8uCxg9Xym71OQs7vL7gg86PluPy55p4sQRl4/edit?usp=sharing",
    "Kashmiri": "https://docs.google.com/spreadsheets/d/12W-xiT23dlLh5-8lbcuEiDFb2eembk7G9E-cLW4BRAo/edit?usp=sharing",
    "Konkani": "https://docs.google.com/spreadsheets/d/1cPM8CFCt1_pU67-pRiSzsAlaJF8o0RKdSrG-jp0b-hM/edit?usp=sharing",
    "Malayalam": "https://docs.google.com/spreadsheets/d/1pc4P51JH9pYAefTNRlKa4U5VlAddb92PK3AtFeLY5zM/edit?usp=sharing",
    "Manipuri": "https://docs.google.com/spreadsheets/d/1PTLbCdRV8t0FIUX3oNvDRxc50vL0XyTgNjqvTZpZr7U/edit?usp=sharing",
    "Marathi": "https://docs.google.com/spreadsheets/d/1J1lPwxEMIbnlBDGiio2ycqezxaXP5w7xhfz1Y2kNKSs/edit?usp=sharing",
    "Sanskrit": "https://docs.google.com/spreadsheets/d/1Lk8ihp2RPTrtbul_UFghkLTZJREIj6VUr_5IJp-ZuZA/edit?usp=sharing",
    "Tamil": "https://docs.google.com/spreadsheets/d/15dxcUgR7MzxGTlkCRV-3QAu1PyyCLs59Auz4XeClvjE/edit?usp=sharing",
    "Telugu": "https://docs.google.com/spreadsheets/d/16Xghko-MO_ELJ6opcmF9SPRqFaXklVnbk2rmbZT-q6I/edit?usp=sharing",
    "Rajasthani": "https://docs.google.com/spreadsheets/d/1BqLjJYQxSPAKlrLaMIw_xKQK3pN5XhJVee8SNoJfpUg/edit?usp=sharing"
}