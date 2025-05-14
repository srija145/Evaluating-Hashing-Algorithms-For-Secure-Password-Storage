import streamlit as st
import sqlite3
import bcrypt

# Title
st.title("🔐 Password Verification Demo")

# User input
email = st.text_input("Email")
password = st.text_input("Password", type="password")

# Verify button
if st.button("Check Credentials"):
    # DB connect
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT hash_bcrypt FROM users WHERE email = ?", (email,))
    result = cursor.fetchone()
    conn.close()

    if result:
        stored_hash = result[0]
        if bcrypt.checkpw(password.encode(), stored_hash.encode()):
            st.success("✅  Correct Password!")
        else:
            st.error("❌  Incorrect password.")
    else:
        st.warning("⚠️  Email not found.")
