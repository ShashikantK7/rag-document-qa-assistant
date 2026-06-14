import streamlit as st
from src.pdf_loader import extract_text_from_pdf
from src.text_processor import create_chunks
from src.vector_store import create_vector_store
from src.config import GOOGLE_API_KEY
from src.rag_pipeline import generate_answer

st.set_page_config(page_title='RAG Document Q&A Assistant')

st.title('📄 RAG Document Q&A Assistant')

uploaded_file = st.file_uploader('Upload a PDF', type=['pdf'])

if uploaded_file:
    text = extract_text_from_pdf(uploaded_file)
    chunks = create_chunks(text)

    vector_store = create_vector_store(
        chunks,
        GOOGLE_API_KEY
    )

    st.success('Document processed successfully!')

    question = st.text_input('Ask a question about the document')

    if question:
        answer = generate_answer(
            vector_store,
            question,
            GOOGLE_API_KEY
        )

        st.subheader('Answer')
        st.write(answer)
