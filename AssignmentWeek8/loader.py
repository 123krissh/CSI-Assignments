from langchain_community.document_loaders import PyMuPDFLoader, Docx2txtLoader, TextLoader, CSVLoader, UnstructuredHTMLLoader
from langchain_community.document_loaders import UnstructuredMarkdownLoader, UnstructuredExcelLoader
import tempfile
import os

LOADER_MAP = {
    ".pdf": PyMuPDFLoader,
    ".docx": Docx2txtLoader,
    ".txt": TextLoader,
    ".csv": CSVLoader,
    ".html": UnstructuredHTMLLoader,
    ".md": UnstructuredMarkdownLoader,
    ".xlsx": UnstructuredExcelLoader
}

def load_documents(uploaded_files):
    documents = []
    for file in uploaded_files:
        suffix = os.path.splitext(file.name)[1].lower()
        if suffix in LOADER_MAP:
            with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
                tmp.write(file.read())
                tmp_path = tmp.name
            loader = LOADER_MAP[suffix](tmp_path)
            documents.extend(loader.load())
    return documents
