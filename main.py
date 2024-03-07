import streamlit as st

email = st.text_input('Enter Email')
password = st.text_input('Enter password')


btn = st.button('Login')
if btn:
    if email == 'amangupta@gmail.com' and password == '12345':
       st.balloons()

