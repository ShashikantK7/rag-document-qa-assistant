import importlib


def test_basic_imports():
    modules = [
        'streamlit',
        'langchain',
        'chromadb',
        'pypdf'
    ]

    for module in modules:
        importlib.import_module(module)
