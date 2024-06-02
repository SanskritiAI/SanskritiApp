import streamlit as st 
import streamlit_authenticator as stauth

import sanskriti_bench.db.auth_functions as auth_fn 
import sanskriti_bench.db.crud_functions as crud_dn 
from sanskriti_bench.db.common import create_database, db_exists, table_exists
from sanskriti_bench.settings import DB_NAME, AUTH_TABLE_NAME, DATA_TABLE_NAME

from sanskriti_bench.components.admin_view import full_admin_view
from sanskriti_bench.components.contributor_view import full_contributor_view
from sanskriti_bench.components.manager_view import full_manager_view

class UserAuth:
    def create_widget(self):
        auth_config = auth_fn.get_all_users_and_export_as_dict(
            database_name=DB_NAME, table_name=AUTH_TABLE_NAME
        )
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
            
            # TODO: Optimize this part (lot of db calls happening here)
            admins = auth_fn.get_all_user_by_role(
                database_name=DB_NAME,
                table_name=AUTH_TABLE_NAME, 
                role="admin"
            )

            contributors = auth_fn.get_all_user_by_role(
                database_name=DB_NAME,
                table_name=AUTH_TABLE_NAME, 
                role="contributor"
            )

            managers = auth_fn.get_all_user_by_role(
                database_name=DB_NAME,
                table_name=AUTH_TABLE_NAME, 
                role="manager"
            )

            try:
                if user_name in list(admins.keys()): 
                    full_admin_view()
                elif user_name in list(contributors.keys()):
                    full_contributor_view(user_name=user_name, language=contributors[user_name])
                elif user_name in list(managers.keys()):
                    full_manager_view(language=managers[user_name])
                else:
                    pass 
            except KeyError:
                st.error("Internal Server Error. Try again later")

        elif st.session_state["authentication_status"] is False:
            st.error('Username/password is incorrect')
        
        elif st.session_state["authentication_status"] is None:
            st.warning('Please enter your username and password')
         