import streamlit as st 

markdown_body = """
### Rules
- Reach out to <@693870619967881244> <@773807047866449933> for participating in your language groups, becoming language managers, mentors or sponsors 
- Each language groups are private channels
- Every Week on Friday, we will have a catch-up to understand the progress. Each Language Manager will share the status of their language
- In case your language is not currently being worked upon, pls reach out so that we can start the progress
- Be kind to all. It's an open science; our work is for the Indian Language and our cultures. 
- Mentors would be available for any help related to data building
### Rules for Data Construction

### Nature of Questions:
- Questions should blend subjective and factual elements, avoiding purely factual queries.
- Avoid direct "what" questions (e.g., "What is this?" or "What is that?").

### Examples to Avoid:
- Do not create overly general knowledge questions (e.g., "What is the capital of India?").
   - The general knowledge questions that are very native to your region or state will still be better to focus on
- Avoid questions related to personal biases and views.
- Refrain from questions related to recent politics (post-2000).

### Content Guidelines:
- Slang is allowed but should be used constructively and contextually.
- Questions can be related to daily lives and relatable scenarios.
- You can include questions about your culture and history, ensuring you know the answers.

### Contribution Rules:
- Do not repeat or copy questions from others. Each question should be unique.
- This is a community effort, not a competition. There is no pressure to compete.
"""


def guidelines():
    st.markdown(markdown_body)