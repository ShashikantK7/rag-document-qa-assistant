from langchain_community.vectorstores import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings


def create_vector_store(chunks, api_key):
    embeddings = GoogleGenerativeAIEmbeddings(
        model='text-embedding-004',
        google_api_key=api_key
    )

    vector_store = Chroma.from_texts(
        texts=chunks,
        embedding=embeddings,
        persist_directory='chroma_db'
    )

    return vector_store
