import streamlit as st
import pdfplumber
import json
import re
import os

st.set_page_config(page_title="LLM Form Filler", layout="centered")
st.title("LLM-Powered Form Filler")
st.markdown("Upload a PDF form and matching user JSON profile to auto-fill it using AI.")

# Sample default user profile
default_profile = {
    "Name": "Harsha Parashar",
    "DOB": "15/08/2000",
    "Email": "harsha@example.com",
    "Phone": "+91-9876543210",
    "Address": "Nalanda Parisar, Kesar Bagh, Indore",
    "Gender": "Female",
    "Aadhaar": "1234-5678-9012"
}

# Upload section
pdf_file = st.file_uploader("Upload PDF Form", type="pdf")
json_file = st.file_uploader("Upload User Profile (.json)", type="json")

# Manual field input
fields_input = st.text_input("Enter fields to autofill (comma-separated):", "Name, DOB, Email, Phone")

# Progress log window
log = st.empty()

def log_step(msg):
    log.markdown(f"**Status:** {msg}")

# Extract text from PDF
def extract_text(pdf_file):
    log_step("Extracting text from PDF...")
    text = ""
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text.strip()

# Autofill matching fields from profile
def autofill_fields(fields, profile):
    log_step("Matching fields with profile...")
    filled_lines = []
    for field in fields:
        key = field.strip()
        value = profile.get(key, "[Not Available]")
        filled_lines.append(f"{key}: {value}")
    return "\n".join(filled_lines)

# Main logic
if st.button("Auto-Fill Form"):
    if not pdf_file:
        st.warning("No PDF uploaded. Using sample PDF not implemented yet.")
        st.stop()

    # Use uploaded profile or default
    if json_file:
        try:
            user_profile = json.load(json_file)
        except:
            st.error("Invalid JSON file. Using default profile.")
            user_profile = default_profile
    else:
        user_profile = default_profile
        st.info("Using default profile.")

    fields = [f.strip() for f in fields_input.split(",")]
    text = extract_text(pdf_file)
    filled_output = autofill_fields(fields, user_profile)

    log_step("Form filled successfully!")
    st.success("Here is your autofilled form content:")
    st.text_area("Autofilled Output", filled_output, height=300)
    st.download_button("Download Filled Form", filled_output, file_name="autofilled_form.txt")