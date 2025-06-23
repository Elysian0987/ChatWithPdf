import streamlit as st
from pdf_utils import extract_text_from_pdf
from rag_utils import split_text, add_chunks_to_chroma, query_gpt

st.set_page_config(page_title="AskMyPDF", layout="centered")
st.title("📄 AskMyPDF – Chat with your PDF!")

uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if uploaded_file:
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.read())
    
    with st.spinner("Extracting text..."):
        text = extract_text_from_pdf("temp.pdf")
        chunks = split_text(text)
        add_chunks_to_chroma(chunks)
    st.success("PDF uploaded and processed!")

    question = st.text_input("❓ Ask a question about your PDF")
    if question:
        with st.spinner("Searching..."):
            answer = query_gpt(question)
        st.markdown("### 🧠 Answer:")
        st.write(answer)
