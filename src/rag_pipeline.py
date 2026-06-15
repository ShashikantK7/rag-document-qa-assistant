from langchain_google_genai import ChatGoogleGenerativeAI


def generate_answer(vector_store, question, api_key):
    docs = vector_store.similarity_search(question, k=3)

    context = "\n\n".join([doc.page_content for doc in docs])

    prompt = f"""
    Answer the question using only the provided context.

    Context:
    {context}

    Question:
    {question}
    """

    # Upgraded from the deprecated 'gemini-1.5-flash' to the active production model
    llm = ChatGoogleGenerativeAI(
        model='gemini-3.5-flash',
        google_api_key=api_key,
        temperature=0
    )

    response = llm.invoke(prompt)
    return response.content
