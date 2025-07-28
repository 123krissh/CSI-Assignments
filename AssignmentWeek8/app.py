import streamlit as st
import os
import tempfile
from dotenv import load_dotenv
from typing import Optional, List, Any

# LangChain & Gemini
from langchain_community.document_loaders import PyPDFLoader, TextLoader, Docx2txtLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA
from langchain.llms.base import LLM
from langchain.vectorstores import Qdrant
from langchain.schema import Document

# Qdrant
from qdrant_client import QdrantClient
from qdrant_client.http.models import Distance, VectorParams

# Google Gemini
import google.generativeai as genai

# ---- Load API Key ----
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY") or st.secrets.get("GEMINI_API_KEY")
genai.configure(api_key=api_key)

# ---- Custom Gemini LLM Wrapper ----
class GeminiLLM(LLM):
    model: Any = genai.GenerativeModel("gemini-1.5-flash")
    temperature: float = 0.7

    @property
    def _llm_type(self) -> str:
        return "google_gemini"

    def _call(self, prompt: str, stop: Optional[List[str]] = None) -> str:
        response = self.model.generate_content(prompt)
        return response.text

# ---- Streamlit UI ----
st.set_page_config(page_title="RAG Chatbot", layout="wide")
st.title("📄 RAG App: Chat with Your Documents")

# ---- Session State ----
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "edit_index" not in st.session_state:
    st.session_state.edit_index = None
if "rag_chain" not in st.session_state:
    st.session_state.rag_chain = None

# ---- Upload Documents ----
uploaded_files = st.file_uploader("Upload PDF, TXT, or DOCX documents", type=["pdf", "txt", "docx"], accept_multiple_files=True)

if uploaded_files:
    raw_text = ""
    for uploaded_file in uploaded_files:
        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            tmp.write(uploaded_file.read())
            tmp_path = tmp.name

        if uploaded_file.name.endswith(".pdf"):
            loader = PyPDFLoader(tmp_path)
        elif uploaded_file.name.endswith(".txt"):
            loader = TextLoader(tmp_path)
        elif uploaded_file.name.endswith(".docx"):
            loader = Docx2txtLoader(tmp_path)
        else:
            continue

        documents = loader.load()
        for doc in documents:
            raw_text += doc.page_content + "\n"

    # ---- Split & Embed ----
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150)
    texts = splitter.split_text(raw_text)
    docs = [Document(page_content=t) for t in texts]

    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    qdrant = QdrantClient(":memory:")
    collection_name = "rag_collection"
    qdrant.recreate_collection(
        collection_name=collection_name,
        vectors_config=VectorParams(size=384, distance=Distance.COSINE)
    )

    vectordb = Qdrant(client=qdrant, collection_name=collection_name, embeddings=embeddings)
    vectordb.add_documents(documents=docs)

    retriever = vectordb.as_retriever(search_type="similarity", search_kwargs={"k": 4})

    # ---- Create RAG Chain ----
    qa_chain = RetrievalQA.from_chain_type(
        llm=GeminiLLM(),
        retriever=retriever,
        return_source_documents=True
    )

    st.session_state.rag_chain = qa_chain
    st.success("✅ Document processed. You can now ask questions!")

# ---- Chat Section ----
st.markdown("### 💬 Chat Interface")

# If RAG chain exists
rag_chain = st.session_state.get("rag_chain", None)

if rag_chain:
    # Edit existing question
    if st.session_state.edit_index is not None:
        idx = st.session_state.edit_index
        old_q = st.session_state.chat_history[idx]['user']
        new_query = st.text_input("📝 Edit your question:", value=old_q)
        if st.button("🔁 Regenerate Answer"):
            with st.spinner("Regenerating..."):
                result = rag_chain({"query": new_query})
                st.session_state.chat_history[idx] = {
                    "user": new_query,
                    "answer": result["result"]
                }
                st.session_state.edit_index = None
                st.rerun()
    else:
        # Ask a new question
        query = st.text_input("❓ Ask a question about your documents:")
        if query:
            with st.spinner("Generating response..."):
                result = rag_chain({"query": query})
                answer = result["result"]

                st.session_state.chat_history.append({
                    "user": query,
                    "answer": answer
                })

                st.markdown(f"**Gemini:** {answer}")

    # ---- Chat History ----
    st.markdown("### 🗂️ Chat History")
    for i, chat in enumerate(st.session_state.chat_history):
        with st.expander(f"Q{i+1}: {chat['user']}"):
            st.markdown(f"**Gemini:** {chat['answer']}")
            if st.button("✏️ Edit", key=f"edit_{i}"):
                st.session_state.edit_index = i
                st.rerun()
else:
    st.warning("📂 Please upload and process documents first.")





# import streamlit as st
# from embed import embed_and_save_documents
# from rag_pipeline import get_rag_chain
# from llm_providers import get_llm
# from loader import load_documents
# from dotenv import load_dotenv
# import os
# import shutil

# TEMP_DIR = "uploaded_docs"
# if not os.path.exists(TEMP_DIR):
#     os.makedirs(TEMP_DIR)

# def clear_previous_docs():
#     shutil.rmtree(TEMP_DIR)
#     os.makedirs(TEMP_DIR)

# load_dotenv()

# st.set_page_config(page_title="RAG Q&A Chatbot", layout="wide")
# st.title("\U0001F4C4 RAG Q&A Chatbot with LangChain")

# # Sidebar: Upload documents
# docs = st.sidebar.file_uploader(
#     "Upload documents", 
#     type=["pdf", "docx", "txt", "csv", "xlsx", "html", "md"], 
#     accept_multiple_files=True
# )

# if docs:
#     clear_previous_docs()  #  Clear any old files from previous runs
#     raw_docs = load_documents(docs)
#     embed_and_save_documents(raw_docs)
#     st.sidebar.success("\u2705 Documents embedded and stored.")

#     # Rebuild the RAG chain after embedding new documents
#     llm = get_llm()
#     st.session_state.rag_chain = get_rag_chain(llm)
#     st.session_state.chat_history = [] # Reset chat history for new documents


# # Initialize session state
# if "chat_history" not in st.session_state:
#     st.session_state.chat_history = []

# if "editing_index" not in st.session_state:
#     st.session_state.editing_index = None

# # LLM and RAG chain setup (only once)
# if "rag_chain" not in st.session_state:
#     llm = get_llm()
#     st.session_state.rag_chain = get_rag_chain(llm)

# rag_chain = st.session_state.rag_chain

# # Editable chat display
# for i in range(0, len(st.session_state.chat_history), 2):
#     user_msg = st.session_state.chat_history[i]
#     bot_msg = st.session_state.chat_history[i + 1] if i + 1 < len(st.session_state.chat_history) else None

#     if st.session_state.editing_index == i:
#         edited_text = st.text_area("Edit your question:", user_msg["content"], key=f"edit_input_{i}")
#         col1, col2 = st.columns([1, 3])
#         with col1:
#             if st.button("\u2705 Save", key=f"save_{i}"):
#                 st.session_state.chat_history[i]["content"] = edited_text
#                 response = rag_chain.invoke({
#                     "question": edited_text,
#                     "chat_history": st.session_state.chat_history[:i]
#                 })
#                 st.session_state.chat_history[i + 1]["content"] = response["answer"]
#                 st.session_state.editing_index = None
#                 st.rerun()

#         with col2:
#             if st.button("\u274C Cancel", key=f"cancel_{i}"):
#                 st.session_state.editing_index = None
#                 st.rerun()
#     else:
#         with st.chat_message("user"):
#             st.markdown(user_msg["content"])
#             if st.button("\u270F\ufe0f Edit", key=f"edit_btn_{i}"):
#                 st.session_state.editing_index = i
#                 st.rerun()

#         if bot_msg:
#             with st.chat_message("bot"):
#                 st.markdown(bot_msg["content"])

# # New message input
# if st.session_state.editing_index is None:
#     user_input = st.chat_input("Ask a question or just chat...")

#     if user_input:
#         response = rag_chain.invoke({
#             "question": user_input,
#             "chat_history": st.session_state.chat_history
#         })

#         st.session_state.chat_history.append({"role": "user", "content": user_input})
#         st.session_state.chat_history.append({"role": "bot", "content": response["answer"]})
#         st.rerun()
