from langchain.chains import ConversationalRetrievalChain
from embed import load_vector_db

def get_rag_chain(llm):
    db = load_vector_db()
    retriever = db.as_retriever(search_kwargs={"k": 3})
    qa_chain = ConversationalRetrievalChain.from_llm(llm=llm, retriever=retriever, return_source_documents=True)
    return qa_chain


# import os
# from dotenv import load_dotenv
# from langchain_core.prompts import PromptTemplate
# from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain_core.output_parsers import StrOutputParser
# from langchain.chains import LLMChain
# from langchain.memory import ConversationBufferMemory

# load_dotenv()

# def create_rag_chain():
#     llm = ChatGoogleGenerativeAI(
#         model="gemini-pro",
#         google_api_key=os.getenv("GEMINI_API_KEY"),
#         temperature=0.4
#     )

#     memory = ConversationBufferMemory(
#         memory_key="chat_history",
#         return_messages=True
#     )

#     template = """You are a helpful assistant that answers user questions about loan approval using the context below.

# Chat history:
# {chat_history}

# Context:
# {context}

# Question:
# {question}

# Answer:"""

#     prompt = PromptTemplate.from_template(template)

#     chain = LLMChain(
#         llm=llm,
#         prompt=prompt,
#         memory=memory,
#         output_parser=StrOutputParser()
#     )

#     return chain
