import streamlit as st
import pandas as pd

df = pd.read_csv("data.csv" , sep = ";")

st.set_page_config(layout="wide")
col1,col2 = st.columns(2)
with col1 :
    st.image("images/photo.jpg" )
with col2 :
    st.title("Atishay Jain")
    content = """Hi my name is AJ and this is my portfolio website for the 
                60 days 20 apps python project from udemy here i learn to use 
                different python pack ages that are usually used to code amazing
                applications in different desktop or web based graphical user interface."""
    st.info(content)
st.write("Below you can find some of the apps i built in Python. Feel free to contact me !")
col3,col4 = st.columns(2)
with col3 :
    for index , row in df[:10].iterrows():
        st.header(row["title"])
with col4 :
    for index , row in df[10:].iterrows():
        st.header(row["title"])