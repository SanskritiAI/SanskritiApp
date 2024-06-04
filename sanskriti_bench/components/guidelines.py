import streamlit as st 

BODY = """

## Guidelines
We expect you to follow these guidelines when you start contributing to this project. 

### General rules

- It would be best if you join the discord [server](https://discord.gg/rGyyDjEgzS) and request in the #general chat discussion regarding which group you want to contribute to and what role you are interested in. 

- After that we will message you on discord with a user_id and password which you will use to login in this platform and start contributing. Please make sure that you do not share this password to anyone else. 

- If you are not comfortable with discord messaging platform then kindly mail us at `proanindyadeep@gmail.com` or `guneetsk99@gmail.com` for enquiring the same. 

- If you apply as a `contributor` role, then you need to just log in to the platform and contribute as many examples as possible. You need to provide the question and answer in your indic / native language. Please make sure the answer you put is correct. 

- Be kind to all. It's an open science; our work is for the Indian Language and our cultures. 

- Mentors would be available for any help related to data building

- All the contributor's contribution will be mentioned and shown publicly in the hall of fame once the project is completed. Contributors with
most numbers of contributions will be rewarded with some incentive. 

### How you should frame the question:

Here are some rules and suggestions on how you should make different questions:

1. DO NOT include any topic which are super controversial or very political in nature. Like asking for opinions etc. You can alaways ask 
questions related to political facts or anything related to history. Refrain from questions related to recent politics (post-2000).

2. Please DO NOT question super generic question. For example: What is the captical of India or Who created Taj Mahal? etc etc. Ask questions
which are related to your culture and questions which are not often asked for daily lives. Example: Question related to Durga Puja, when language is bengali, because it is an important cultural part for Bengal. 

3. It would be GREAT if you ask questions starting with a negation or the answer should start with No. For example: Instead of asking
Is Onam celebrated on Kerala?, ask this question: Is Onam not celebrated on Kerala? 

4. Always ask questions using your indic / native language. 

5. Do not repeat or copy questions from others. Each question should be unique. Please remmember this is not a competition. There is 
absolutely no pressure. 

6. Avoid questions related to personal biases and views.
"""


def guidelines():
    st.markdown(BODY)