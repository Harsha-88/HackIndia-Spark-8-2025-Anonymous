import streamlit as st
import pdfplumber
import json
import re
import os

st.set_page_config(page_title="LLM Form Filler", layout="centered")

st.markdown("""
    <h1 style='text-align: center; color: #4B8BBE;'>🤖 LLM-Powered Form Filler</h1>
    <p style='text-align: center;'>Upload any PDF form and a user profile (JSON), and let AI auto-fill it for you!</p>
    <hr style="border-top: 1px solid #bbb;">
""", unsafe_allow_html=True)

# Sample default user profile
default_profile = {
    "Name": "xyz",
    "DOB": "15/08/2000",
    "Email": "harsha@example.com",
    "Phone": "+91-9876543210",
    "Address": "Nalanda Parisar, Kesar Bagh, Indore",
    "Gender": "Female",
    "Aadhaar": "1234-5678-9012"
}

# Upload Section
st.sidebar.header("Upload Inputs")
pdf_file = st.sidebar.file_uploader("📄 Upload PDF Form", type="pdf")
json_file = st.sidebar.file_uploader("🧾 Upload User Profile (.json)", type="json")

# Smart field detection
def detect_fields(text):
    possible_fields = re.findall(r"([A-Za-z ]+):", text)
    cleaned = sorted(set([f.strip() for f in possible_fields if len(f.strip()) > 2]))
    return cleaned

# Logging status
log = st.empty()
def log_step(msg):
    log.markdown(f"🟢 **Status:** {msg}")

# Extract text from PDF
def extract_text(pdf_file):
    log_step("🔍 Extracting text from PDF...")
    text = ""
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text.strip()

# Autofill fields
def autofill_fields(fields, profile):
    log_step("✍️ Auto-filling fields using profile data...")
    filled_lines = []
    for field in fields:
        key = field.strip()
        value = profile.get(key, "[Not Available]")
        filled_lines.append(f"{key}: {value}")
    return "\n".join(filled_lines)

# Main UI Logic
if pdf_file:
    extracted_text = extract_text(pdf_file)
    suggested_fields = detect_fields(extracted_text)
    st.success("✅ PDF loaded and fields detected!")

    st.markdown("### ✏️ Select Fields to Auto-Fill")
    selected_fields = st.multiselect("Suggested fields:", options=suggested_fields, default=suggested_fields[:4])

    st.markdown("---")

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

    if st.button("🚀 Auto-Fill Form"):
        if not selected_fields:
            st.warning("Please select at least one field to fill.")
        else:
            filled_output = autofill_fields(selected_fields, user_profile)
            st.success("🎉 Form filled successfully!")

            st.markdown("### 🔍 Preview")
            st.text_area("Autofilled Output", filled_output, height=300)
            st.download_button("⬇️ Download Filled Form", filled_output, file_name="autofilled_form.txt")

else:
    st.info("Please upload a PDF form from the sidebar to begin.")

st.markdown("<hr style='border-top: 1px solid #bbb;'>", unsafe_allow_html=True)

