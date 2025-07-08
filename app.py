# app.py

import streamlit as st
from recommender import recommend_careers
from utils import extract_text_from_pdf, extract_text_from_docx

st.set_page_config(page_title="AI Career Recommender", layout="centered")

# UI Header
st.title("🌟 AI-Based Career Recommendation System")
st.markdown("Upload your resume or tell us about your **skills & interests**, and we'll suggest the best careers for you!")

# Input Choice
input_method = st.radio("How would you like to provide your information?", ["Upload Resume", "Type Manually"])

user_text = ""

# Resume Upload Option
if input_method == "Upload Resume":
    uploaded_file = st.file_uploader("Upload your resume (PDF or DOCX)", type=["pdf", "docx"])
    if uploaded_file:
        file_ext = uploaded_file.name.split(".")[-1]
        if file_ext == "pdf":
            user_text = extract_text_from_pdf(uploaded_file)
        elif file_ext == "docx":
            user_text = extract_text_from_docx(uploaded_file)
        else:
            st.error("Unsupported file format!")

# Manual Input Option
else:
    user_text = st.text_area("Tell us about your skills, interests, and experience:")

# Recommend Button
if st.button("🎯 Recommend Careers"):
    if user_text.strip() == "":
        st.warning("Please upload a resume or enter some text.")
    else:
        recommendations = recommend_careers(user_text)
        st.success("✅ Based on your profile, here are some suggested careers:")
        for career in recommendations:
            st.markdown(f"- **{career}**")
