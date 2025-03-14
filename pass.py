import streamlit as st
import re

st.set_page_config(page_title="Password Strength Checker",page_icon="🔐")

st.title("🔐Password Strength Checker")

st.markdown("""
## An app designed to check the password strength for the ultimate protection of customer's data.""")

password = st.text_input("Enter Your Password",type="password")

suggestion = []

score = 0

if password:
    if(len(password)>=8):
        score += 1
    else:
        suggestion.append("❌ Your password should be atleast 8 characters long")
    if re.search(r'[A-Z]',password) and re.search(r'[a-z]',password):
        score += 1
    else:
        suggestion.append("❌ Your password should contain both lower and upper case characters")
    if re.search(r'\d',password):
        score += 1
    else:
        suggestion.append("❌ Your password must contain altleast one digit")
    if re.search(r'[@#$%&*^]',password):
        score += 1
    else:
        suggestion.append("❌ Your password must contain atleast one special character")
    if score == 4:
        suggestion.append("✅ Your password is strong!🎉")
    elif score == 3:
        suggestion.append("🟨 Your password is medium in strength.It could be stronger")
    else:
        suggestion.append("🟥 Your password is weak.Please write a strong password")

    if suggestion:
        st.markdown("# Improvement Suggestions")
        for tip in suggestion:
            st.write(tip)
else:
    st.info("Please enter a password to get checked")