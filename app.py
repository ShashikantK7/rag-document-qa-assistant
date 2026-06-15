import streamlit as st
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

@st.cache_resource
def process_and_embed_document(uploaded_file, api_key):
    """Caches the document extraction and embedding process"""
    # Reset file pointer in case it was read elsewhere
    uploaded_file.seek(0)
    text = extract_text_from_pdf(uploaded_file)
    chunks = create_chunks(text)
    vector_store = create_vector_store(chunks, api_key)
    return vector_store, len(chunks)

uploaded_file = st.file_uploader('Upload a PDF', type=['pdf'])

if uploaded_file:
    try:
        # Calls the cached function
        vector_store, num_chunks = process_and_embed_document(uploaded_file, GOOGLE_API_KEY)

        st.info(f'Document split into {num_chunks} chunks')
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
