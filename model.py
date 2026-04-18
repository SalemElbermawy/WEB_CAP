from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings,ChatOpenAI




# api of hack_club
API_KEY  = "sk-hc-v1-d8fc9e3a93924a1a9033b783cec593ad6b6f572b141f43eaa80d03f0934545f7"
BASE_URL = "https://ai.hackclub.com/proxy/v1"

# rag

pdfs=["CAP_Proposal.pdf","protof.pdf"]

embedding_model= OpenAIEmbeddings(
    model="openai/text-embedding-3-small",
    api_key=API_KEY,
    base_url=BASE_URL
)

# print(embedding_model.embed_query("hello"))
all_pages=[]
for file in pdfs:
    loader=PyPDFLoader(file)
    pages=loader.load()
    all_pages.extend(pages)
    

pages_splitter=RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)

chunks= pages_splitter.split_documents(all_pages)


data_rag = Chroma.from_documents(
    chunks,
    embedding=embedding_model,
    persist_directory="./db"
)

# LLM

llm=ChatOpenAI(
    model="gemini-3-flash-preview",
    api_key=API_KEY,
    base_url=BASE_URL
)



