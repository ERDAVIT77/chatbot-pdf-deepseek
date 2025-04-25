from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.document_loaders import PyPDFLoader
import os

VECTOR_STORE_PATH = "data/index"

def load_vector_store():
    documents = []
    for filename in os.listdir("data"):
        if filename.endswith(".pdf"):
            loader = PyPDFLoader(os.path.join("data", filename))
            try:
                pages = loader.load_and_split()
                documents.extend(pages)
            except Exception as e:
                print(f"Error cargando {filename}: {e}")

    if not documents:
        raise ValueError("No se cargaron documentos desde los PDFs. Asegúrate de tener archivos válidos en 'data/'.")

    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vector_store = FAISS.from_documents(documents, embeddings)
    vector_store.save_local(VECTOR_STORE_PATH)
    return vector_store

def query_vector_store(query):
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vector_store = FAISS.load_local(VECTOR_STORE_PATH, embeddings, allow_dangerous_deserialization=True)
    results = vector_store.similarity_search(query, k=3)
    return "\n\n".join([r.page_content for r in results])
