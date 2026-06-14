# 📄 RAG Document Q&A Assistant

A Generative AI application that allows users to upload PDF documents and ask questions about their content using Retrieval-Augmented Generation (RAG).

## Features

- Upload PDF documents
- Extract and process document text
- Intelligent text chunking
- Semantic search using vector embeddings
- ChromaDB vector storage
- Question answering using Google Gemini
- Retrieval-Augmented Generation (RAG)
- Streamlit web interface
- GitHub Actions CI/CD

## Tech Stack

- Python
- Streamlit
- LangChain
- ChromaDB
- Google Gemini API
- PyPDF
- GitHub Actions

## Project Architecture

PDF Upload
→ Text Extraction
→ Chunking
→ Embeddings
→ ChromaDB
→ Similarity Search
→ Gemini LLM
→ Grounded Answer

## Project Structure

```text
rag-document-qa-assistant/
├── app.py
├── requirements.txt
├── .env.example
├── src/
│   ├── config.py
│   ├── pdf_loader.py
│   ├── text_processor.py
│   ├── vector_store.py
│   └── rag_pipeline.py
├── chroma_db/
└── .github/workflows/
```

## Setup

1. Clone the repository
2. Create a virtual environment
3. Install dependencies
4. Copy `.env.example` to `.env`
5. Add your Gemini API key
6. Run:

```bash
streamlit run app.py
```

## Skills Demonstrated

- Retrieval-Augmented Generation (RAG)
- Vector Databases
- Prompt Engineering
- LLM Integration
- LangChain
- ChromaDB
- Streamlit Development
- CI/CD with GitHub Actions

## Future Improvements

- Chat history support
- Source citation display
- Multiple document support
- Cloud deployment
- User authentication

## Author

Shashikant Kamble
