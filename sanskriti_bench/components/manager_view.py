import pandas as pd 
import streamlit as st 
from sanskriti_bench.db.auth_functions import  fetch_lang_table, fetch_all_users_by_lang
from sanskriti_bench.settings import DB_NAME, DATA_TABLE_NAME, AUTH_TABLE_NAME

def get_all_users_under_manager(language: str):
    fetched_lang_data, columns = fetch_lang_table(
        database_name=DB_NAME, table_name=AUTH_TABLE_NAME,
        language=language
    ) 
    if fetched_lang_data:
        df = pd.DataFrame(fetched_lang_data, columns=columns)
        st.write(df)
    else:
        st.error("No Data Found")
    
def get_contributions_by_lang(language: str):
    fetched_lang_data, columns = fetch_all_users_by_lang(
        database_name=DB_NAME, table_name=DATA_TABLE_NAME,
        language=language
    ) 

    if fetched_lang_data:
        df = pd.DataFrame(fetched_lang_data, columns=columns)
        st.write(df)
    else:
        st.error("No Data Found")


def full_manager_view(language: str):
    actions = st.selectbox(
        label="Please select the action",
        options=["All Users", "Contributions"]
    )
    if actions == "All Users":
        get_all_users_under_manager(language=language)
    elif actions == "Contributions":
        get_contributions_by_lang(language=language)