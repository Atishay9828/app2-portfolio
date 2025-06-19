import streamlit as st 
from send_email import send_email
import pandas as pd

df = pd.read_csv("topic.csv")

st.set_page_config(layout="wide")
st.header("Contact Me")
with st.form(key = "email_form") :
    user_email = st.text_input("Your Email : ")
    topic = st.selectbox(label = "What topic you want to dicuss : " , options = df["topic"])
    message = st.text_area("Your Message  : " )
    message = f"""\
Subject: New email from {user_email}

From: {user_email}

Topic: {topic} 
Message:  {message} """
    submit_button = st.form_submit_button("Submit")
    if submit_button :
        send_email(message)
        st.info("Your Email was sent sucessfully")