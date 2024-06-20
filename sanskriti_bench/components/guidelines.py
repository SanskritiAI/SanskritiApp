import streamlit as st 

BODY = """

### Guidelines
We expect you to follow these guidelines when contributing to this project. 

#### General rules

- It would be best to join the Discord [server](https://discord.gg/rGyyDjEgzS) and request in the #general chat discussion regarding which group you want to contribute to and what role you are interested in. 

- Fill out this [google form](https://forms.gle/nVsXbsgkY4U2nvL79) if you do not have your credentials for contributing.

- Please mail us at: `guneetsk99@gmail.com` / `proanindyadeep@gmail.com` / `ashishvashist024@gmail.com` for any kind of personal questions or ask that in discord.

- If you apply as a `contributor` role, you need to log in to the platform and contribute as many examples as possible. You need to provide the question and answer in your indic / native language. Please make sure the answer you put is correct. 

- Be kind to all. It's an open science; our work is for the Indian Language and our cultures. 

- Mentors would be available for any help related to data building

- All the contributor's contributions will be mentioned and shown publicly in the Hall of Fame once the project is completed.

#### How you should frame the question:

Here are some rules and suggestions on how you should make different questions:

1. DO NOT include any topics that are super controversial or very political. Like asking for opinions, etc. You can always ask 
questions related to political facts or anything related to history. Refrain from questions related to recent politics (post-2000).

2. Please DO NOT question super generic questions. For example, what is the capital of India, and who created the Taj Mahal? Etc etc. Ask questions
which are related to your culture and questions that are not often asked for daily lives. Example: Question related to Durga Puja, when the language is Bengali, because it is an essential cultural part of Bengal. 

3. It would be great to ask questions starting with a negation or the answer should start with No. For example, Instead of asking
Is Onam celebrated on Kerala?, ask: Is Onam not celebrated on Kerala? 

4. Always ask questions using your indic / native language. It should not be any mixture of two languages. Complete question and answer in native language. 

5. Do not repeat or copy questions from others. Each question should be unique. Please remember this is not a competition. There is absolutely no pressure. 

6. Avoid questions related to personal biases and views.

#### Some suggestion for question and answer

1. One of popular question you can frame is topics on folklore you have heard in your childhood. 
2. Another type of question could be any kind of local historical or political facts. 
3. One popular type is to ask tricky questions. For example question related to family relationship. Example:

```
Question: What relation does my uncle's son have with me?
Answer: Cousin (paternal)
```

Note: I intentionally wrote the translated version of Hindi, so that almost 
all of the contributors can understand. 
4. Any question to religious facts. Be careful when asking religious question, it SHOULD NOT be OPINION BASED question. For example:

```
Question: How many lotus flowers are used for Durga Puja
Answer: 108
```
Note: I intentionally wrote this in english so that everyone can understand this. 


5. There is another type of question we can suggest which are question that intentionally asked with wrong answer. For example:

```
Question: Are't 110 lotus flower used in Durga Puja?
Answer (expected): No, 108 is used
```

This is also known as: "leading question" with an incorrect presumption. The above question is intentionally phrased to prompt a correction, leading the respondent to provide the accurate information.

Other than this, the sky is your limit, use your creativity and ask as many question you 
would like to ask. 
"""


def guidelines():
    st.markdown(BODY)