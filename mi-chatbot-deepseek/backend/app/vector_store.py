from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.document_loaders import PyPDFLoader
import os

def load_vector_store():
    docs = []
    for filename in os.listdir("data"):
        if filename.endswith(".pdf"):
            loader = PyPDFLoader(f"data/{filename}")
            pages = loader.load_and_split()
            docs.extend(pages)

    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    splits = text_splitter.split_documents(docs)

    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_documents(splits, embeddings)
    return vectorstore

def query_vector_store(query, vectorstore):
    return vectorstore.similarity_search(query, k=4)
