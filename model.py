from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings,ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate





# api of hack_club
API_KEY  = "sk-hc-v1-d8fc9e3a93924a1a9033b783cec593ad6b6f572b141f43eaa80d03f0934545f7"
BASE_URL = "https://ai.hackclub.com/proxy/v1"

# rag


embedding_model= OpenAIEmbeddings(
    model="openai/text-embedding-3-small",
    api_key=API_KEY,
    base_url=BASE_URL
)

# pdfs=["CAP_Proposal.pdf","protof.pdf"]
# print(embedding_model.embed_query("hello"))
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
    ("system","""
     You are a helpful assistant. Use only the context.
     """),
    ("human","""
     context:
     {context}
     
     
     question: 
     {question}
     
     """)]
)

def context(qs):
    
    retriever_data=data_rag.as_retriever(search_kwargs={"k":5}).invoke(qs)
    
    retriever_data= "\n\n".join([
        f"{doc.page_content}" for doc in retriever_data
    ])
    
    return retriever_data

def response(user_input):
    message=prompt.format_messages(
        context=context(user_input),
        question=user_input)
    
    response=llm.invoke(message)
    
    return response.content


