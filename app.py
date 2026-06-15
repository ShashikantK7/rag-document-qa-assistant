import streamlit as st
import google.generativeai as genai
from src.pdf_loader import extract_text_from_pdf
from src.text_processor import create_chunks
from src.vector_store import create_vector_store
from src.config import GOOGLE_API_KEY
from src.rag_pipeline import generate_answer

st.set_page_config(page_title='RAG Document Q&A Assistant')

st.title('📄 RAG Document Q&A Assistant')
st.caption('Upload a PDF and ask questions using Gemini + RAG')

if not GOOGLE_API_KEY:
    st.error('GOOGLE_API_KEY not found. Create a .env file using .env.example')
    st.stop()

if st.button('Show Available Gemini Models'):
    try:
        genai.configure(api_key=GOOGLE_API_KEY)
        for model in genai.list_models():
            st.write(model.name)
            st.write(model.supported_generation_methods)
    except Exception as e:
        st.error(f'Model diagnostic error: {e}')

uploaded_file = st.file_uploader('Upload a PDF', type=['pdf'])

if uploaded_file:
    try:
        text = extract_text_from_pdf(uploaded_file)
        chunks = create_chunks(text)

        st.info(f'Document split into {len(chunks)} chunks')

        vector_store = create_vector_store(chunks, GOOGLE_API_KEY)

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

    except Exception as e:
        st.error(f'Error: {str(e)}')