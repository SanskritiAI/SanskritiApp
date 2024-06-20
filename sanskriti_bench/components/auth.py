import streamlit as st 
import streamlit_authenticator as stauth

from sanskriti_bench.db.auth import AuthTable
from sanskriti_bench.settings import AUTH_TABLE_NAME, db_payload
from sanskriti_bench.components.admin_view import full_admin_view

class UserAuth:
    def __init__(self):
        self.auth = AuthTable(payload=db_payload, table_name=AUTH_TABLE_NAME)

    def create_widget(self):
        auth_config = self.auth.export_all_users_as_st_auth_dict()
        if auth_config is not None:
            self.authenticator = stauth.Authenticate(
                auth_config['credentials'],
                auth_config['cookie']['name'],
                auth_config['cookie']['key'],
                auth_config['cookie']['expiry_days'],
            )
        return self 

    def configure_privilages(self, user_name: str):
        if st.session_state["authentication_status"]:
            self.authenticator.logout()

            admins = self.auth.fetch_all_users_by_role(role="admin")
            contributors = self.auth.fetch_all_users_by_role("contributors")
            managers = self.auth.fetch_all_users_by_role("managers")

            try:
                if user_name in list(admins.keys()):
                    full_admin_view()
                elif user_name in list(contributors.keys()):
                    st.write("Coming Soon")
                elif user_name in list(managers.keys()):
                    st.write("Coming Soon")
                else:
                    pass 
            except KeyError:
                st.error("Internal Server Error. Try again later")
        
        elif st.session_state["authentication_status"] is False:
            st.error('Username/password is incorrect')
        
        elif st.session_state["authentication_status"] is None:
            st.warning('Please enter your username and password')