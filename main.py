import streamlit as st

st.set_page_config(layout="wide")
col1,col2 = st.columns(2)
with col1 :
    st.image("images/photo.jpg" )
with col2 :
    st.title("Atishay Jain")
    content = """Hi my name is AJ and this is my portfolio website for the 
                60 days 20 apps python project from udemy here i learn to use 
                different python packages that are usually used to code amazing
                applications in different desktop or web based graphical user interface."""
    st.info(content)