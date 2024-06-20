import os 
import sys 

sys.path.append(os.getcwd())

import pandas as pd 
import streamlit as st 
from sanskriti_bench.components.auth import UserAuth
from sanskriti_bench.components.about import about 
from sanskriti_bench.components.guidelines import guidelines
from sanskriti_bench.components.tutorials import tutorials

def show_before_login():
    with st.container(border=10):
        st.markdown(
            "Welcome to Sanskriti Bench. To your left side you will "
            "find navigation. Please check out the guidelines before contributing."
            " Also you can find our tutorials on how to contribute question and answer"
            " in your language through phone and web platform."
            " You should have got your username and password from our admin, if not"
            " please contact them in discord or fill out this  "
            " [google form](https://forms.gle/nVsXbsgkY4U2nvL79)"
        )
        st.markdown(
            """
            ##### Quick Start:
            Once you join to become a contributor, please do the following:

            1. Join [Discord](https://discord.gg/BK8UmK3xZC)
            2. Fill out this [google form](https://forms.gle/nVsXbsgkY4U2nvL79) if you
            do not have your credentials for contributing.
            3. Join this whatsapp group: [Group Link](https://chat.whatsapp.com/J6HrW6YlaupJMSZh2bTinD). Although we prefer discord, it is only for them
            who are not well versed with Discord. 
            4. Checkout the Guideline section to understand the rules. 

            Mail us at: `guneetsk99@gmail.com` / `proanindyadeep@gmail.com` / `ashishvashist024@gmail.com` for any kind of personal questions or ask that in discord.
            Kindly check out the Guidelines page in the left navigation bar for further questions.  
        """
        )


def show_leaderboard():
    # TODO: This function todo once admin view is fully sorted out 
    st.write("Coming Soon") 


with st.sidebar:
    st.image("https://sanskritiai.github.io/static.sanskriti.app/logo.png", use_column_width=True)
    st.header("Sanskriti Bench")

sidebar_options = ["Menu", "Guidelines", "Tutorials", "About"]
selected_option = st.sidebar.selectbox("Navigation", sidebar_options)

with st.sidebar:
    show_leaderboard()

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