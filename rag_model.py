from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings,ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
import streamlit as st




# api of hack_club
API_KEY  =st.secrets["OPENAI_API_KEY"]
BASE_URL = "https://ai.hackclub.com/proxy/v1"

# rag


embedding_model= OpenAIEmbeddings(
    model="openai/text-embedding-3-small",
    api_key=API_KEY,
    base_url=BASE_URL
)

# pdfs=["a4.pdf","busi.pdf","poster.pdf","CAP_Proposal.pdf","proto.pdf"]
# # print(embedding_model.embed_query("hello"))
# all_pages=[]
# for file in pdfs:
#     loader=PyPDFLoader(file)
#     pages=loader.load()
#     all_pages.extend(pages)
    

# pages_splitter=RecursiveCharacterTextSplitter(
#     chunk_size=500,
#     chunk_overlap=100
# )

# chunks= pages_splitter.split_documents(all_pages)

# data_rag = Chroma.from_documents(
#     chunks,
#     embedding=embedding_model,
#     persist_directory="./db"
# )

data_rag = Chroma(
    persist_directory="./db",
    embedding_function=embedding_model
)

# LLM

llm=ChatOpenAI(
    model="gemini-3-flash-preview",
    api_key=API_KEY,
    base_url=BASE_URL
)





prompt=ChatPromptTemplate.from_messages([
   ("system", """
You are AquaBot, an intelligent assistant for the CAP project team.
You answer questions strictly based on the provided context extracted from the project documents.

Rules you must follow:
- Answer ONLY using information from the context. Never use outside knowledge.
- If the context does not contain enough information to answer, say: "I don't have enough information in the documents to answer this."
- Be concise and precise. Avoid unnecessary filler or repetition.
- When referencing specific details (numbers, dates, names), quote them exactly as they appear in the context.
- If the question is unclear, ask for clarification before answering.
- Always respond in the same language the user is using (Arabic or English).
- Never make up facts, names, or figures.
- You can just answer the relative question to the prototype and project and the normal message like "hello"
- NEVER use Markdown formatting of any kind: no **, no *, no #, no -, no backticks, no bullet points.

"""),
    
    ("human","""
     context:
     {context}
     
     
     question: 
     {question}
     
     """)]
)

def context(qs):
    
    retriever_data=data_rag.as_retriever(search_kwargs={"k":15}).invoke(qs)
    
    retriever_data= "\n\n".join([
        f"{doc.page_content}" for doc in retriever_data
    ])
    
    return retriever_data

def response(user_input):
    
    # response_prompt=llm.invoke(f"edit the prompt to be small and clear and if the question is daily questio like hello don't change it and if the related to my project redfine it  good to can get the data from the rag system {user_input}")
    # response_prompt=response_prompt.content
    
    message=prompt.format_messages(
        context=context(user_input),
        question=user_input)
    
    response=llm.invoke(message)
    
    return response.content   #,response_prompt


# input_user=input("enter the qs\n")

# x=response(input_user)

# print(x)





