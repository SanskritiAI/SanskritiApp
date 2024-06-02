import sys 
import os 
sys.path.append(os.getcwd())

import streamlit as st
from sanskriti_bench.components.auth import UserAuth
from sanskriti_bench.components.about import about
from sanskriti_bench.components.guidelines import guidelines
from sanskriti_bench.components.tutorials import tutorials

def show_before_login():
    with st.container(border=10):
        st.write(
            "Welcome to Sanskriti Bench. To your left side you will "
            "find navigation. Please check out the guidelines before contributing"
            "Also you can find our tutorials on how to contribute question ans answer"
            "in your language through phone and web platform."
            "You should have got your username and password from our admin, if not"
            "please contact them in discord or mail them. You can find more info about"
            "that in our guidelines section."
        )


with st.sidebar:
    st.image("./assets/logo.png", use_column_width=True)
    st.header("Sanskriti Bench")

sidebar_options = ["Menu", "Guidelines", "Tutorials", "About"]
selected_option = st.sidebar.selectbox("Navigation", sidebar_options)

# TODO: Need to check for direct duplicates ASAP

if selected_option == "Menu":
    auth = UserAuth().create_widget()
    name, authentication_status, username = auth.authenticator.login()
    st.header(f"Welcome {name if name else ""}")
    st.markdown(
        "[![Discord](https://img.shields.io/badge/Discord-%235865F2.svg?style=for-the-badge&logo=discord&logoColor=white)](https://discord.gg/BK8UmK3xZC)"
    )
    if st.session_state["authentication_status"] is None:
        show_before_login()
    auth.configure_privilages(user_name=username)

elif selected_option == "Guidelines":
    guidelines()

elif selected_option == "About":
    about()

elif selected_option == "Tutorials":
    tutorials()