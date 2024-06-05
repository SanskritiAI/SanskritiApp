import os 
import sys 

sys.path.append(os.getcwd())

import pandas as pd
import streamlit as st
from sanskriti_bench.components.auth import UserAuth
from sanskriti_bench.components.about import about
from sanskriti_bench.components.guidelines import guidelines
from sanskriti_bench.components.tutorials import tutorials

from sanskriti_bench.db.auth_functions import fetch_lang_table
from sanskriti_bench.settings import LANGUAGES, DB_NAME, DATA_TABLE_NAME

def show_before_login():
    with st.container(border=10):
        st.write(
            "Welcome to Sanskriti Bench. To your left side you will "
            "find navigation. Please check out the guidelines before contributing."
            " Also you can find our tutorials on how to contribute question and answer"
            " in your language through phone and web platform."
            "You should have got your username and password from our admin, if not"
            "please contact them in discord or mail them. You can find more info about "
            "that in our guidelines section."
        )
        st.markdown(
            """
            If you don't have your credentials kindly reach out to us at:

            - [Discord](https://discord.gg/BK8UmK3xZC)
            - Mail us at: `guneetsk99@gmail.com` or `proanindyadeep@gmail.com`
            - Join this whatsapp group: [Group Link](https://chat.whatsapp.com/J6HrW6YlaupJMSZh2bTinD)
            
            When you mail or write in whatsapp, just write the following info:
            1. Your name and email
            2. Any affiliations
            3. What language you wish to contribute
            4. Do you want to manage a language (in this case, we would like to talk more)

            Kindly check out the Guidelines page in the left navigation bar for further questions.  
        """
        )

def show_leaderboard():
    lang_map = {
        "Language": [],
        "Progress": [],
    } 

    for lang in LANGUAGES:
        collected = len(fetch_lang_table(
            database_name=DB_NAME,
            table_name=DATA_TABLE_NAME,
            language=lang
        )[0])
        lang_map["Language"].append(lang)
        lang_map["Progress"].append(collected)
    
    df = pd.DataFrame(lang_map, columns=["Language", "Progress"])
    df = df.sort_values(by='Progress', ascending=False)
    st.write("Our overall community progress")
    st.dataframe(
        df,
        column_config={
            "Language": "Language",
            "Progress": st.column_config.ProgressColumn(
                "Progress",
                help="Progress in percentage",
                format="%d%%",
                min_value=0,
                max_value=500
            )
        },
        hide_index=True,
        width=500
    )


with st.sidebar:
    st.image("./assets/logo.png", use_column_width=True)
    st.header("Sanskriti Bench")

sidebar_options = ["Menu", "Guidelines", "Tutorials", "About"]
selected_option = st.sidebar.selectbox("Navigation", sidebar_options)

with st.sidebar:
    show_leaderboard()

# TODO: Need to check for direct duplicates ASAP

if selected_option == "Menu":
    st.header("Sanskriti Bench App")
    auth = UserAuth().create_widget()
    name, authentication_status, username = auth.authenticator.login()
    st.write(f"#### Welcome {name if name else ''}")
    if st.session_state["authentication_status"] is None:
        show_before_login()
    auth.configure_privilages(user_name=username)

elif selected_option == "Guidelines":
    guidelines()

elif selected_option == "About":
    about()

elif selected_option == "Tutorials":
    tutorials()