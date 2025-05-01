# HackIndia-Spark-8-2025-Anonymous
Project: LLM-Powered Form Filler

Problem:
        Filling out forms manually is time-consuming and prone to errors. Many documents like Aadhaar, Admit Cards, KYC forms, etc., need to be filled with repetitive information. Automating this process can save time and reduce human errors.

Solution:
         The LLM-Powered Form Filler allows users to upload PDF forms (like Aadhaar or Admit Cards), specify which fields they want to auto-fill, and then download the completed form. The form is automatically filled using the user’s pre-defined profile data (such as name, email, phone number, etc.).

Features:
-Upload PDF: Upload a PDF form (Aadhaar, Admit Card, etc.).
         
Auto-fill Fields: Specify which fields to auto-fill (e.g., Name, DOB, Email).

-Download Completed Form: After auto-filling, the form can be downloaded with the filled data.


Technologies:
            -Streamlit: For creating an interactive and user-friendly interface.
            -Hugging Face Transformers: To leverage LLMs for processing and filling form fields.
            -pdfplumber: For extracting text from PDF documents.


How it Works:
1. Extract Text: Extract text from the uploaded PDF form.
2. Match Fields: Match the fields to be filled with data from the user profile.
3. Auto-fill: Automatically fill the specified fields with the profile data.
4. Download: Download the auto-filled PDF form.

Impact:
       This tool helps automate the filling of various forms like KYC, tax, visa, and educational forms, reducing manual effort, saving time, and minimizing errors.
