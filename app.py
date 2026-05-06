import streamlit as st

st.title("Streamlit App")
st.markdown("Hello World!")

st.markdown("Hier ist noch nicht viel los!")

firstname = st.text_input("Vorname")
lastname = st.text_input("Nachname")

if st.button("Submit"):
    st.write(firstname + " " + lastname.upper())