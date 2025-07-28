# embed.py

from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from huggingface_hub import login
from dotenv import load_dotenv
import os
import shutil

DB_DIR = "faiss_index"

load_dotenv()
login(os.getenv("HUGGINGFACEHUB_API_TOKEN"))

embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)

def embed_and_save_documents(documents):
    if os.path.exists(DB_DIR):
        shutil.rmtree(DB_DIR)
    texts = text_splitter.split_documents(documents)
    db = FAISS.from_documents(texts, embedding_model)
    db.save_local(DB_DIR)

def load_vector_db():
    return FAISS.load_local(DB_DIR, embedding_model, allow_dangerous_deserialization=True)
