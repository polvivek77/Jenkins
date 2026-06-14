import streamlit as st

st.title("Jenkins Demo")

name = st.text_input("Enter your name")

if st.button("Submit"):
    st.success(f"Hello {name}")
    