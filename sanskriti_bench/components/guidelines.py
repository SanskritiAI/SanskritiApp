import streamlit as st 

BODY = """

## Guidelines
We expect you to follow these guidelines when contributing to this project. 

### General rules

- It would be best to join the Discord [server](https://discord.gg/rGyyDjEgzS) and request in the #general chat discussion regarding which group you want to contribute to and what role you are interested in. 

- After that, we will message you on Discord with a user_id and password, which you will use to log in to this platform and start contributing. Please make sure that you do not share this password with anyone else. 

- If you are not comfortable with discord messaging platform then kindly mail us at `proanindyadeep@gmail.com` or `guneetsk99@gmail.com` for enquiring the same. 

- If you apply as a `contributor` role, you need to log in to the platform and contribute as many examples as possible. You need to provide the question and answer in your indic / native language. Please make sure the answer you put is correct. 

- Be kind to all. It's an open science; our work is for the Indian Language and our cultures. 

- Mentors would be available for any help related to data building

- All the contributor's contributions will be mentioned and shown publicly in the Hall of Fame once the project is completed. Contributors with
the most number of contributions will be rewarded with some incentive. 

### How you should frame the question:

Here are some rules and suggestions on how you should make different questions:

1. DO NOT include any topics that are super controversial or very political. Like asking for opinions, etc. You can always ask 
questions related to political facts or anything related to history. Refrain from questions related to recent politics (post-2000).

2. Please DO NOT question super generic questions. For example, what is the capital of India, and who created the Taj Mahal? Etc etc. Ask questions
which are related to your culture and questions that are not often asked for daily lives. Example: Question related to Durga Puja, when the language is Bengali, because it is an essential cultural part of Bengal. 

3. It would be great to ask questions starting with a negation or the answer should start with No. For example, Instead of asking
Is Onam celebrated on Kerala?, ask: Is Onam not celebrated on Kerala? 

4. Always ask questions using your indic / native language. 

5. Do not repeat or copy questions from others. Each question should be unique. Please remember this is not a competition. There is 
absolutely no pressure. 

6. Avoid questions related to personal biases and views.
"""


def guidelines():
    st.markdown(BODY)