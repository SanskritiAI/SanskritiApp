import pandas as pd
import streamlit as st 
import sanskriti_bench.db.auth_functions as auth
import sanskriti_bench.db.crud_functions as crud 
from sanskriti_bench.settings import DB_NAME, DATA_TABLE_NAME

# TODO: See your last 10 /5contributions (Editable? )

def show_on_top():
    with st.container(border=10):
        st.write(
            "Your every contribution counts. Once you hit submit, your contribution"
            "will go under review. Please make sure you follow the guidelines. If you"
            "cross a certain threshold of valid contributions, you will be eligible for"
            "incentives.",

            "\n\nBefore hitting the submit button, make sure you have no mistakes, once you"
            "hit submit, the process can not be undone. So please take your time"
        )

def view_past_contributions(user_name: str, language: str):
    contributions, columns = crud.get_all_contributions_by_contributor(
        database_name=DB_NAME, 
        table_name=DATA_TABLE_NAME,
        user_name=user_name
    )

    all_from_lang, _ = auth.fetch_lang_table(
        database_name=DB_NAME, table_name=DATA_TABLE_NAME,
        language=language
    )

    all_ = crud.get_total_contributions_all_languages(database_name=DB_NAME, table_name=DATA_TABLE_NAME)

    if contributions is not None:
        st.write("### We appreciate your contributions")
        st.write("Once you cross 200 contributions, you will be eligible for incentive from our side. Thanks again for contributing")
        with st.container(border=10):
            col1, col2, col3 = st.columns(3)
            col1.metric(f"Total Contributions (out of 200)", len(contributions))
            col2.metric(f"Total in {language}", len(all_from_lang) if all_from_lang else 0)
            col3.metric("Total in all languages", all_ if all_ else 0)

            st.write(
                pd.DataFrame(contributions, columns=columns)
            )



def contribution_view(user_name: str, language: str):
    with st.form("form", clear_on_submit=True):
        question = st.text_area(
            label="Question",
            height=100,
            key="user_question"
        )

        answer = st.text_area(
            label="Answer",
            height=400,
            key="user_answer"
        )        

        submit = st.form_submit_button("Submit")
        if submit:
            if question == "" or answer == "":
                st.toast(
                    body="Please enter a valid response",
                    icon="🥹"
                )
            else:
                status = crud.insert(
                    database_name=DB_NAME, 
                    table_name=DATA_TABLE_NAME,
                    values={
                        "user_name": user_name,
                        "language": language, 
                        "question": question,
                        "answer": answer
                    }
                )
                if status:
                    st.balloons()
                    st.toast(
                        body="Thank you for your contribution.",
                        icon="🎉"
                    )
                else:
                    st.toast(
                        body="Something went wrong",
                        icon="❌"
                    )


def full_contributor_view(user_name: str, language: str):
    show_on_top()
    action = st.selectbox("Please select", options=["Contribute", "Your Contributions"])
    if action == "Contribute":
        contribution_view(user_name=user_name, language=language)
    elif action == "Your Contributions":
        view_past_contributions(user_name=user_name, language=language)