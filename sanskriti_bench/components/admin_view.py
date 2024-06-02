import streamlit as st 
import pandas as pd 
import sanskriti_bench.db.auth_functions as auth 
from sanskriti_bench.settings import (
    ROLES, LANGUAGES, DB_NAME, AUTH_TABLE_NAME, DATA_TABLE_NAME
)

def admin_privilages_manager_component():
    st.markdown("Admin Privilages manager")
    
    with st.form("Admin Privilages Form", clear_on_submit=True):
        email = st.text_input(label="Enter email") 
        user_name = st.text_input(label="Create user_name")
        name = st.text_input(label="Enter name")
        password = st.text_input(label="Create password")
        language = st.selectbox(label="select language", options=LANGUAGES)
        role = st.selectbox(label="select role", options=ROLES)

        button = st.form_submit_button(label="Submit")
        if button:
            status = auth.create_new_user(
                database_name=DB_NAME,
                table_name=AUTH_TABLE_NAME,
                values={
                    "email": email,
                    "user_name": user_name, 
                    "name": name, 
                    "password": password,
                    "language": language, 
                    "role": role,
                }
            )

            if status:
                st.toast(body="Successfully created new user", icon="🎊")
            else:
                st.toast(body="Unable to create user. Try again", icon="❌") 

def get_all_users():
    # TODO: We are not grouping by them for now 
    all_users, columns = auth.fetch_all_users(
        database_name=DB_NAME, table_name=AUTH_TABLE_NAME
    )

    if all_users:
        df = pd.DataFrame(all_users, columns=columns)
        st.write(df)
    else:
        st.toast(body="No user found. Try again", icon="❌")


def see_contributions():
    # TODO: on the top some dashboard cards will go 
    # and may be some graphs 
    
    # TODO: Need to handle this with rows and columns
    st.write("### Contributions in different languages")
    with st.container(border=10):
        cols = st.columns(4)
        for i, col in enumerate(cols):
            col.metric(
                f"Total: {LANGUAGES[i]}",
                len(auth.fetch_lang_table(DB_NAME, DATA_TABLE_NAME, LANGUAGES[i])[0])
            )
    
    # Similar for next four languages will go into a different container 
    # TODO here 
    
    language = st.selectbox(
        label="Please select the language", 
        options=LANGUAGES
    )
    fetched_lang_data, columns = auth.fetch_lang_table(
        database_name=DB_NAME, table_name=DATA_TABLE_NAME, language=language
    ) 


    if fetched_lang_data:
        df = pd.DataFrame(fetched_lang_data, columns=columns)
        st.write(df)
    else:
        st.error("No Data Found")


def full_admin_view():
    actions = st.selectbox(
        label="Please select the action",
        options=["Create User", "All Users", "Contributions"]
    )
    if actions == "Create User":
        admin_privilages_manager_component()
    elif actions == "All Users":
        get_all_users()
    elif actions == "Contributions":
        see_contributions() 