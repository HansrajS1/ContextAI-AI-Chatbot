from pathlib import Path

from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_community.document_loaders import (
    PyPDFLoader,
    CSVLoader,
    TextLoader,
)

from models.embeddings import get_embeddings


def load_documents(path="data/docs"):
    documents = []

    for file_path in Path(path).rglob("*"):
        ext = file_path.suffix.lower()

        try:
            if ext == ".pdf":
                loader = PyPDFLoader(str(file_path))
                documents.extend(loader.load())

            elif ext == ".csv":
                loader = CSVLoader(
                    file_path=str(file_path),
                    encoding="utf-8"
                )
                documents.extend(loader.load())

            elif ext == ".txt":
                loader = TextLoader(
                    file_path=str(file_path),
                    encoding="utf-8"
                )
                documents.extend(loader.load())

        except Exception as e:
            print(f"Failed to load {file_path}: {e}")

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    return splitter.split_documents(documents)


def build_vector_store(docs):
    return FAISS.from_documents(docs, get_embeddings())


def retrieve_context(store, query, k=3):
    return store.similarity_search(query, k=k)
