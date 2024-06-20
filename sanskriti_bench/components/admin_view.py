import time 
import json
from typing import Union 
from datetime import datetime

import pandas as pd 
import streamlit as st
from sanskriti_bench.db.auth import AuthTable
from sanskriti_bench.db.data import DataTable
from sanskriti_bench.settings import (
    AUTH_TABLE_NAME, DATA_TABLE_NAME,
    ROLES, LANGUAGES, ALL_INDIAN_STATES, db_payload
)

# Helper functions
def create_batches(lst, batch_size):
    return [lst[i:i + batch_size] for i in range(0, len(lst), batch_size)]

@st.cache_data
def convert_df(df):
   return df.to_csv(index=False).encode('utf-8')

class AdminView:
    auth = AuthTable(payload=db_payload, table_name=AUTH_TABLE_NAME)
    data = DataTable(payload=db_payload, table_name=DATA_TABLE_NAME)

    @classmethod
    def admin_privilages_manager_component(cls):
        st.markdown("Admin Privilages manager")

        with st.form("Admin Privilages Form", clear_on_submit=True):
            email = st.text_input(label="Enter email") 
            user_name = st.text_input(label="Create user_name")
            name = st.text_input(label="Enter name")
            password = st.text_input(label="Create password")
            language = st.selectbox(label="select language", options=LANGUAGES)
            role = st.selectbox(label="select role", options=ROLES)
            region = st.selectbox(
                label="Choose your region", options=ALL_INDIAN_STATES
            )
            affiliation = st.text_input(label="What is your affiliation school/uninversity/company", value="null")
            
            button = st.form_submit_button(label="Submit")
            if button:
                if not all([email, user_name, name, password, language, role]):
                    st.error("Other than affiliation, all other inputs are mandatory")
                else:
                    status = cls.auth.insert_new_user(data={
                        "email": email,
                        "user_name": user_name, 
                        "name": name, 
                        "password": password,
                        "language": language, 
                        "role": role,
                        "region": region,
                        "affiliation": affiliation
                    })
                    if status:
                        st.toast(body="Successfully created new user", icon="🎊")
                    else:
                        st.toast(body="Unable to create user. Try again", icon="❌") 

    @classmethod
    def get_all_users(cls):
        all_users, columns = cls.auth.fetch_all_users()
        if all_users:
            df = pd.DataFrame(all_users, columns=columns)
            st.write(df)
        else:
            st.toast(body="No user found. Try again", icon="❌")
    
    @classmethod
    # TODO: This will be from DataTable 
    def see_contributions(cls):
        st.write("### Contributions in different languages")
        all_batches = create_batches(LANGUAGES, batch_size=4)

        with st.expander():
            for batch in all_batches:
                cols = st.columns(len(batch))
                for i, col in enumerate(cols):
                    language = batch[i]
                    total_contributions = cls.data.get_count(key="language", value=language)
                    col.metric(f"Total: {language}", total_contributions)
        
        language = st.selectbox(
            label="Please select the language", 
            options=LANGUAGES
        )
        
        fetched_lang_data, columns = cls.data.fetch(key="language", value=language)
        if fetched_lang_data:
            df = pd.DataFrame(fetched_lang_data, columns=columns)
            st.write(df)
        else:
            st.error("No Data Found")
    
    @classmethod
    def delete_single_user(cls, user_id: str):
        status = cls.auth.delete_by_id(user_name_or_id=user_id)
        if status:
            st.toast(f"Deleted user: {user_id}", icon="🥹")
        else:
            st.toast("Unable to delete", icon="❌")
    
    @classmethod
    def delete_user_view(cls):
        with st.form(key="Delete a user", clear_on_submit=True):
            st.write(
                "You can either type the UID you want to delete for a single user "
                "or type in the range to delete in bulk. For example, "
                "if you want to delete from UID 5 to 29, just type 5-29."
            )
            user_name_or_id = st.text_input("Enter a valid user name or ID")
            submit = st.form_submit_button("Submit")

            if submit:
                user_name_or_id = user_name_or_id.strip()
                if "-" in user_name_or_id:
                    try:
                        upper, lower = map(int, user_name_or_id.split("-"))
                        gather_user_to_delete = list(range(upper, lower + 1))
                        all_user_ids = [element[0] for element in cls.auth.fetch(columns="uid")[0] if element]

                        for user in gather_user_to_delete:
                            if user in all_user_ids:
                                cls.delete_single_user(user_id=str(user))
                                time.sleep(0.1)
                            else:
                                st.toast(f"User ID {user} not found", icon="❌")
                    except ValueError:
                        st.toast("Invalid range format. Please use valid numbers.", icon="❌")
                else:
                    cls.delete_single_user(user_id=user_name_or_id)
    
    @classmethod
    def alter_user_information(cls, user_name_or_id: Union[str, int]):
        column_key = "user_name" if isinstance(user_name_or_id, str) else "uid"
        rows, _ = cls.auth.fetch(key=column_key, value=user_name_or_id)
        print(rows)
        rows = rows[0]

        with st.form(key="Update user information", clear_on_submit=True):
            email = st.text_input(label="email", placeholder=rows[1]) or rows[1]
            user_name = st.text_input(label="user_name", placeholder=rows[2]) or  rows[2]
            name = st.text_input(label="name", placeholder=rows[3]) or rows[3]
            password = st.text_input(label="password", placeholder=rows[4]) or rows[4]
            language = st.selectbox(label="language", options=LANGUAGES, index=LANGUAGES.index(rows[5])) 
            role = st.selectbox(label="role", options=ROLES, index=ROLES.index(rows[6]))
            region = st.selectbox(label="region", options=ALL_INDIAN_STATES, index=ALL_INDIAN_STATES.index(rows[7]))
            affiliation = st.text_input(label="Affiliation", placeholder=rows[8]) or rows[8]
            
            # Button
            update = st.form_submit_button(label="Update")
        
        if update:
            user_id = rows[0]
            new_values={
                "email": email,
                "user_name": user_name, 
                "name": name, 
                "password": password,
                "language": language, 
                "role": role,
                "region": region, 
                "affiliation": affiliation
            }

            for i, (key, new_value) in enumerate(new_values.items()):
                if new_values != rows[i+1]:
                    status = cls.auth.alter_user_information(
                        user_name=user_id,
                        key=key,
                        value=new_value
                    )
                    if status:
                        st.toast("Sucessfully updated user info", icon="🎉")
                    else:
                        st.toast(f"Unable to update: {key} to {new_value}", icon="❌")
        
    @classmethod
    def upload_auth_csv(cls):
        with st.container(border=True):
            uploader = st.file_uploader("Upload external CSV", type=[".csv"])
            st.warning("Please make sure the schema of csv matches with user table.")

            if uploader:
                csv = pd.read_csv(uploader)
                expected_schema = ['uid', 'email', 'user_name', 'name', 'password', 'language', 'role', 'region', 'affiliation']
                if all([element in csv.columns for element in expected_schema]): 
                    csv = csv[expected_schema]
                else:
                    st.error(csv)
            
            submit = st.button("Submit")
            if submit:
                all_user_names = [element[0] for element in cls.auth.fetch(
                    columns="user_name"
                )[0] if element]
                all_user_ids = [element[0] for element in cls.auth.fetch(
                    columns="uid"
                )[0] if element]

                user_names_to_skip = []
                for _, row in csv.iterrows():
                    if row["uid"] not in all_user_ids and row["user_name"] not in all_user_names:
                        cls.auth.insert(data={
                            "email": row["email"],
                            "user_name": row["user_name"],
                            "name": row["name"],
                            "password": row["password"],
                            "language": row["language"],
                            "role": row["role"],
                            "region": row["region"],
                            "affiliation": row["affiliation"] 
                        })
                    else:
                        user_names_to_skip.append({row["uid"]: row["user_name"]})
                st.success("Updated database with new user, please refresh")
                with st.expander("Duplicate users are skipped"):
                    st.json(json.dumps(user_names_to_skip))
    
    @classmethod
    def upload_data_csv(cls):
        uploader = st.file_uploader("Upload external CSV", type=[".csv"])
        if uploader:
            csv = pd.read_csv(uploader)
            expected_schema = ['user_name', 'language', 'question', 'answer']
            if all([element in csv.columns for element in expected_schema]):
                csv = csv[expected_schema]
                st.write(csv)
            else:
                st.error("Schema did not match")
        
        submit = st.button("Submit")
        if submit:
            for _, row in csv.iterrows():
                cls.data.insert_new_data(data={
                    "user_name": row["user_name"],
                    "language": row["language"],
                    "question": row["question"],
                    "answer": row["answer"]
                })
        st.success("Updated database with new user, please refresh")
    
    @classmethod
    def export_all_user_information(cls, table_type: str):
        export_button = st.button("Export all user information")
        file_name = "auth" if type == "auth" else "contributions"
        if export_button:
            rows, columns = cls.auth.fetch() if table_type == "auth" else cls.data.fetch()
            if rows:
                df = pd.DataFrame(rows, columns=columns)
                csv = convert_df(df)
                st.download_button(
                    "Press to Download",
                    csv,
                    f"all_{file_name}_exported_{str(datetime.now())}.csv",
                    "text/csv",
                    key='download-csv'
                )


def full_admin_view():
    actions = st.selectbox(
        label="Please select the action",
        options=["Create User", "All Users", "Contributions"]
    )
    
    if actions == "Create User":
        AdminView.admin_privilages_manager_component()
    elif actions == "All Users":
        AdminView.get_all_users()
        AdminView.export_all_user_information(table_type="auth")

        st.write("##### Update user information")
        with st.container(border=True):
            user_name_or_id = st.text_input(label="Enter the User ID (uid)")
        if user_name_or_id:
            AdminView.alter_user_information(user_name_or_id=user_name_or_id)
        
        st.write("#### Upload external CSV to user database")
        AdminView.upload_auth_csv()

        st.write("##### Danger zone: Delete user information")
        AdminView.delete_user_view()
    
    elif actions == "Contributions":
        AdminView.see_contributions()
        AdminView.export_all_user_information(table_type="data")
        st.write("#### Upload external data from CSV")
        AdminView.upload_data_csv()
        st.write("#### Warning: Delete a row")
        st.write("Select sid to remove the entire row. Do only if it is necessary (like removing duplicates)")
        # TODO: This needs to be changed to delete a data view not from user 
        AdminView.delete_user_view()