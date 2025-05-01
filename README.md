# HackIndia-Spark-8-2025-Anonymous
Project: LLM-Powered Form Filler

Problem:
        Filling out forms manually is time-consuming and prone to errors. Many documents like Aadhaar, Admit Cards, KYC forms, etc., need to be filled with repetitive information. Automating this process can save time and reduce human errors.

Solution:
         The LLM-Powered Form Filler allows users to upload PDF forms (like Aadhaar or Admit Cards), specify which fields they want to auto-fill, and then download the completed form. The form is automatically filled using the user’s pre-defined profile data (such as name, email, phone number, etc.).

Features:

Upload PDF: Upload any PDF form (e.g., Aadhaar, Admit Card).

Upload User Profile: Upload a user profile in JSON format, or use the default profile.

Auto-fill Fields: Select fields to auto-fill from the uploaded PDF form (e.g., Name, DOB, Email).

Preview and Download: View the autofilled form and download it as a text file.

Smart Field Detection: Automatically detects potential fields in the uploaded PDF form.


Technologies:

Streamlit: For creating an interactive and user-friendly interface.

Hugging Face Transformers: To leverage LLMs for processing and filling form fields.

pdfplumber: For extracting text from PDF documents.

JSON: For handling user profiles.


How it works:
Upload a PDF form in the sidebar.

Upload a user profile in JSON format (or use the default profile).

The fields in the PDF will be automatically detected.

Select which fields you want to auto-fill.

Click on "🚀 Auto-Fill Form" to generate the autofilled form.

Preview the autofilled form and download it.

Impact:
       This tool helps automate the filling of various forms like KYC, tax, visa, and educational forms, reducing manual effort, saving time, and minimizing errors.
