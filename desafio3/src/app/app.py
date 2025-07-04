import streamlit as st

st.set_page_config(
    page_title="Book",
    layout="wide"
)

pages = st.navigation(
    [
        st.Page(page="create_contact.py", title="Create Contact"), 
        st.Page(page="contacts.py", title="Contact list")
    ]
)

pages.run()