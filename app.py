import streamlit as st
from pdf_reader import extract_text_from_pdf
from quiz_maker import generate_quiz

st.title('Quiz Generator from PDF')

uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")
if uploaded_file is not None:
    text = extract_text_from_pdf(uploaded_file)
    if text:
        st.write("Text Extracted: ")
        st.write(text[:1000])  # Display first 1000 characters of the extracted text
        if st.button("Generate Quiz"):
            quiz_questions = generate_quiz(text)
            st.write("Quiz Questions:")
            for question in quiz_questions:
                st.write(question)
