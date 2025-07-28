# import streamlit as st
# from embed import embed_and_save_documents
# from rag_pipeline import get_rag_chain
# from llm_providers import get_llm
# from loader import load_documents
# from dotenv import load_dotenv
# import os

# load_dotenv()

# st.set_page_config(page_title="RAG Q&A Chatbot", layout="wide")
# st.title("📄 RAG Q&A Chatbot with LangChain")

# # Sidebar: Upload documents
# docs = st.sidebar.file_uploader(
#     "Upload documents", 
#     type=["pdf", "docx", "txt", "csv", "xlsx", "html", "md"], 
#     accept_multiple_files=True
# )

# if docs:
#     raw_docs = load_documents(docs)
#     embed_and_save_documents(raw_docs)
#     st.sidebar.success("✅ Documents embedded and stored.")

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

#     # Check if editing this message
#     if st.session_state.editing_index == i:
#         edited_text = st.text_area("Edit your question:", user_msg["content"], key=f"edit_input_{i}")
#         col1, col2 = st.columns([1, 3])
#         with col1:
#             if st.button("✅ Save", key=f"save_{i}"):
#                 # Save and re-generate response
#                 st.session_state.chat_history[i]["content"] = edited_text
#                 response = rag_chain.invoke({
#                     "question": edited_text,
#                     "chat_history": st.session_state.chat_history[:i]
#                 })
#                 st.session_state.chat_history[i + 1]["content"] = response["answer"]
#                 st.session_state.editing_index = None
#                 st.rerun()

#         with col2:
#             if st.button("❌ Cancel", key=f"cancel_{i}"):
#                 st.session_state.editing_index = None
#                 st.rerun()

#     else:
#         with st.chat_message("user"):
#             st.markdown(user_msg["content"])
#             if st.button("✏️ Edit", key=f"edit_btn_{i}"):
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




# app.py
import streamlit as st
from embed import embed_and_save_documents
from rag_pipeline import get_rag_chain
from llm_providers import get_llm
from loader import load_documents
from dotenv import load_dotenv
import os

load_dotenv()

st.set_page_config(page_title="RAG Q&A Chatbot", layout="wide")
st.title("\U0001F4C4 RAG Q&A Chatbot with LangChain")

# Sidebar: Upload documents
docs = st.sidebar.file_uploader(
    "Upload documents", 
    type=["pdf", "docx", "txt", "csv", "xlsx", "html", "md"], 
    accept_multiple_files=True
)

if docs:
    raw_docs = load_documents(docs)
    embed_and_save_documents(raw_docs)
    st.sidebar.success("\u2705 Documents embedded and stored.")

# Initialize session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "editing_index" not in st.session_state:
    st.session_state.editing_index = None

# LLM and RAG chain setup (only once)
if "rag_chain" not in st.session_state:
    llm = get_llm()
    st.session_state.rag_chain = get_rag_chain(llm)

rag_chain = st.session_state.rag_chain

# Editable chat display
for i in range(0, len(st.session_state.chat_history), 2):
    user_msg = st.session_state.chat_history[i]
    bot_msg = st.session_state.chat_history[i + 1] if i + 1 < len(st.session_state.chat_history) else None

    if st.session_state.editing_index == i:
        edited_text = st.text_area("Edit your question:", user_msg["content"], key=f"edit_input_{i}")
        col1, col2 = st.columns([1, 3])
        with col1:
            if st.button("\u2705 Save", key=f"save_{i}"):
                st.session_state.chat_history[i]["content"] = edited_text
                response = rag_chain.invoke({
                    "question": edited_text,
                    "chat_history": st.session_state.chat_history[:i]
                })
                st.session_state.chat_history[i + 1]["content"] = response["answer"]
                st.session_state.editing_index = None
                st.rerun()

        with col2:
            if st.button("\u274C Cancel", key=f"cancel_{i}"):
                st.session_state.editing_index = None
                st.rerun()
    else:
        with st.chat_message("user"):
            st.markdown(user_msg["content"])
            if st.button("\u270F\ufe0f Edit", key=f"edit_btn_{i}"):
                st.session_state.editing_index = i
                st.rerun()

        if bot_msg:
            with st.chat_message("bot"):
                st.markdown(bot_msg["content"])

# New message input
if st.session_state.editing_index is None:
    user_input = st.chat_input("Ask a question or just chat...")

    if user_input:
        response = rag_chain.invoke({
            "question": user_input,
            "chat_history": st.session_state.chat_history
        })

        st.session_state.chat_history.append({"role": "user", "content": user_input})
        st.session_state.chat_history.append({"role": "bot", "content": response["answer"]})
        st.rerun()
