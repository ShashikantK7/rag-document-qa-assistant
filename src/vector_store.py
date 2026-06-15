from langchain_community.vectorstores import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings


def create_vector_store(chunks, api_key):
    # Upgraded to an active model and restored the required 'models/' prefix
    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/gemini-embedding-2",
        google_api_key=api_key
    )

    # In-memory ephemeral storage (from our previous caching fix)
    vector_store = Chroma.from_texts(
        texts=chunks,
        embedding=embeddings
    )

    return vector_store
