import streamlit as st 

initial_body = """
## Resources

Here are some list of resources which will help you to get started. 

#### Contributing through Mobile 

You can contribut to mobile by using Google voice typing. If you do not have
voice typing you can download it from [playstore](https://play.google.com/store/apps/details?id=com.google.android.inputmethod.latin&hl=en_IN)
"""


markdown_body = """
#### Contributing through Desktop 

For those who want to conrtribute in desktop mode (with a keyboard) here are some list of 
source which can help to input your indic language keyboard. 

##### [Google Input Tools](https://www.google.com/intl/en/inputtools/try/)

This is one of the most popular multi-lingual keyboard input supported 
"""

ginput = """
Google Input tools is very easy. Just select the language and start writing in english and it will give you suggestion of the corresponding selected language character by character. 

Once you type in the question ans answer, copy the question, answer and paste it to our "Question" and "Answer" fields.

We also recommend to see this [YouTube tutorial](https://www.youtube.com/watch?v=5aRPY1bMvXI)

##### [Lexilogos](https://www.lexilogos.com/english/index.htm)
"""

lexilogos_input  = """
Lexilogos provide a very basic multilingual keyboard input support. So if you want to type in this method, you can check out lexilogos. 
"""

def tutorials():
    st.markdown(initial_body)
    st.video("https://www.youtube.com/watch?v=uUSiuKp5zf8")
    st.markdown(markdown_body) 
    st.image("./assets/g_input.png")
    st.markdown(ginput)
    st.image("./assets/lexilogos.png")
    st.markdown(lexilogos_input)
