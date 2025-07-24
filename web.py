from main import generate_mdp
import streamlit as st
import time

st.title("Password Generator")
st.write("Click the button below to generate a secure password.")

st.sidebar.header("Settings")
nb_words = int(st.sidebar.radio("**Number of words in password:**", ["2", "3", "4"]))

if st.button("Generate Password"):
    password = generate_mdp(nb_words)

    try:
        with st.spinner("Generating password..."):
            time.sleep(1.5)

            st.markdown("---")
            st.success(f"Generated Password: **{password}**")
            st.info("Nombre de caractères: **" + str(len(password)) + "**")
    
    except Exception as e:
        st.error(f"An error occurred: {e}")