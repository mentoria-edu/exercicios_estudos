import streamlit as st


st.set_page_config(
    page_title="New Contact",
    layout="wide"
)


st.title("Create Contact")

with st.form("create_contact"):

    row_name, = st.columns(1)
    field_code_area, field_phone_number = st.columns([2,8])
    row_email, = st.columns(1)
    empty_space_1, submit_button_space, empty_space_2 = st.columns([3,3,3])

    with row_name:
        name = st.text_input(label="Name", placeholder="Insert name")
    
    with field_code_area:
        code_area = st.text_input(
            label="Code area", 
            placeholder="00", 
            max_chars=2
        )
    
    with field_phone_number:
        phone_number = st.text_input(
            label="Phone number (just numbers)", 
            placeholder="999999999", 
            max_chars=9
        )

    with row_email:
        email = st.text_input(label="Email", placeholder="email@email.com")
    
    with submit_button_space:
        submitted = st.form_submit_button("Create contact", use_container_width=True)

    if submitted:
        st.success(f" The '{name}' contact has been created!")






