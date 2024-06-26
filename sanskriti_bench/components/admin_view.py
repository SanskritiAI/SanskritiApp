import time 
import json 
from datetime import datetime
import streamlit as st 
import pandas as pd 
import sanskriti_bench.db.crud_functions as crud 
import sanskriti_bench.db.auth_functions as auth 
from sanskriti_bench.settings import (
    ROLES, LANGUAGES, DB_NAME, AUTH_TABLE_NAME, DATA_TABLE_NAME, ALL_INDIAN_STATES
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
        region = st.selectbox(
            label="Choose your region", options=ALL_INDIAN_STATES
        )
        affiliation = st.text_input(label="What is your affiliation school/uninversity/company", value="null")

        button = st.form_submit_button(label="Submit")
        if button:
            if not all([email, user_name, name, password, language, role]):
                st.error("Other than affiliation, all other inputs are mandatory")
            else:
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
                        "region": region,
                        "affiliation": affiliation
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

def create_batches(lst, batch_size):
    return [lst[i:i + batch_size] for i in range(0, len(lst), batch_size)]

def see_contributions():
    # TODO: on the top some dashboard cards will go 
    # and may be some graphs 
    
    st.write("### Contributions in different languages")
    all_batches = create_batches(LANGUAGES, batch_size=4)
    k = 0
    with st.container(border=10):
        for _ in range(len(all_batches)):
            cols = st.columns(4)
            for i, col in enumerate(cols):
                col.metric(
                    f"Total: {LANGUAGES[i+k]}",
                    len(auth.fetch_lang_table(DB_NAME, DATA_TABLE_NAME, LANGUAGES[i+k])[0])
                )
            k += 4
    
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


def delete_one_user(table_name, user_id: str):
    status = auth.delete_by_id(
        database_name=DB_NAME, 
        table_name=table_name,
        user_name_or_id=user_id,
        type="auth"
    )
    if status:
        st.toast(f"Deleted user: {user_id}", icon="🥹")
    else:
        st.toast("Unable to delete", icon="❌")


def delete_user_view(type="auth"):
    table_name = AUTH_TABLE_NAME if type == "auth" else DATA_TABLE_NAME

    with st.form(key="Delete an user", clear_on_submit=True):
        st.write(
            "You either type the uid you want to delete for single user "
            "or type in the range to delete in bulk. So let's say "
            "if you want to delte from uid 5 to 29 just type 5-29"
        )
        user_name_or_id = st.text_input("Enter a valid user name or id")
        submit = st.form_submit_button("submit")
        if submit:
            user_name_or_id = user_name_or_id.split("-")
            if len(user_name_or_id) == 1:
                delete_one_user(
                    table_name=table_name, user_id=user_name_or_id[0]
                )
            else:
                # assumption it will always return two values (upper and lower limit)
                upper, lower = user_name_or_id
                upper, lower = int(upper), int(lower)
                gather_user_to_delete = [u for u in range(upper, lower + 1)]
                all_user_ids = [element[0] for element in auth.get_all_rows_of_column(
                    database_name=DB_NAME,
                    table_name=AUTH_TABLE_NAME,
                    column_name="uid"
                )]
                
                print(all_user_ids)
                for user in gather_user_to_delete:
                    if user in all_user_ids:
                        delete_one_user(table_name=table_name, user_id=str(user))
                        time.sleep(0.1)


                

def alter_user_information(user_name_or_id):
    rows, _ = auth.get_full_user_info(
        database_name=DB_NAME, table_name=AUTH_TABLE_NAME,
        user_name_or_id=user_name_or_id
    )
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
            if new_value !=  rows[i+1]:
                print("yes yes")
                status = auth.alter_user_information(
                    database_name=DB_NAME, table_name=AUTH_TABLE_NAME,
                    user_name_or_id=user_id,
                    key=key,
                    value=new_value
                ) 
                if status:
                    st.toast("Sucessfully updated user info", icon="🎉")
                else:
                    st.toast(f"Unable to update: {key} to {new_value}", icon="❌")


def upload_auth_csv():
    with st.container(border=True):
        uploader = st.file_uploader("Upload external CSV", type=[".csv"])
        st.warning("Please make sure the schema of csv matches with user table.")

        # By default we will assume that it uploaded a user table 
        if uploader:
            csv = pd.read_csv(uploader)
            expected_schema = ['uid', 'email', 'user_name', 'name', 'password', 'language', 'role', 'region', 'affiliation']
            if all([element in csv.columns for element in expected_schema]):
                csv = csv[expected_schema]
                st.write(csv)
            else:
                st.error("Schema did not match")

        submit = st.button("Submit")
        if submit:
            all_user_names = [element[0] for element in auth.get_all_rows_of_column(
                database_name=DB_NAME,
                table_name=AUTH_TABLE_NAME,
                column_name="user_name"
            )]
            all_user_ids = [element[0] for element in auth.get_all_rows_of_column(
                database_name=DB_NAME,
                table_name=AUTH_TABLE_NAME,
                column_name="uid"
            )]

            user_names_to_skip = []
            for _, row in csv.iterrows():
                if row["uid"] not in all_user_ids and row["user_name"] not in all_user_names:
                    auth.create_new_user(
                        database_name=DB_NAME,
                        table_name=AUTH_TABLE_NAME,
                        values={
                            "email": row["email"],
                            "user_name": row["user_name"],
                            "name": row["name"],
                            "password": row["password"],
                            "language": row["language"],
                            "role": row["role"],
                            "region": row["region"],
                            "affiliation": row["affiliation"]
                        }
                    ) 
                else:
                    user_names_to_skip.append({row["uid"]: row["user_name"]}) 
            st.success("Updated database with new user, please refresh")
            with st.expander("Duplicate users are skipped"):
                st.json(json.dumps(user_names_to_skip))


def upload_data_csv():
    with st.container(border=True):
        uploader = st.file_uploader("Upload external CSV", type=[".csv"])
        if uploader:
            csv = pd.read_csv(uploader)
            expected_schema = ['user_name', 'language', 'question', 'answer']
            print(csv.columns)
            if all([element in csv.columns for element in expected_schema]):
                csv = csv[expected_schema]
                st.write(csv)
            else:
                st.error("Schema did not match")
        submit = st.button("Submit")
        if submit:
            for _, row in csv.iterrows():
                crud.insert(
                    database_name=DB_NAME,
                    table_name=DATA_TABLE_NAME,
                    values={
                        "user_name": row["user_name"],
                        "language": row["language"],
                        "question": row["question"],
                        "answer": row["answer"]
                    }
                ) 
        st.success("Updated database with new user, please refresh")


@st.cache_data
def convert_df(df):
   return df.to_csv(index=False).encode('utf-8')


def export_all_user_information(type: str):
    export_button = st.button("Export all user information")
    file_name = "auth" if type == "auth" else "contributions"
    if export_button:
        rows, columns = auth.fetch_all_users(
            database_name=DB_NAME, table_name=AUTH_TABLE_NAME if type == "auth" else DATA_TABLE_NAME
        )
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
        admin_privilages_manager_component()
    elif actions == "All Users":
        get_all_users()
        export_all_user_information(type="auth")

        st.write("##### Update user information")
        with st.container(border=True):
            user_name_or_id = st.text_input(label="Enter the User ID (uid)")
        if user_name_or_id:
            alter_user_information(user_name_or_id=user_name_or_id)
        
        st.write("#### Upload external CSV to user database")
        upload_auth_csv()
        
        st.write("##### Danger zone: Delete user information")
        delete_user_view()
    elif actions == "Contributions":
        see_contributions() 
        export_all_user_information(type="contributions")
        st.write("#### Upload external data from CSV")
        upload_data_csv()
        st.write("#### Warning: Delete a row")
        st.write("Select sid to remove the entire row. Do only if it is necessary (like removing duplicates)")
        delete_user_view(type="data")