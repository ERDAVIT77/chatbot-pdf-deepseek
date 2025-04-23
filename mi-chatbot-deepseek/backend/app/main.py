from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.vector_store import load_vector_store, query_vector_store
from app.ai_deepseek import ask_deepseek

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

vector_store = load_vector_store()

@app.get("/ask")
async def ask(q: str):
    docs = query_vector_store(q, vector_store)
    context = "\n".join([doc.page_content for doc in docs])
    answer = ask_deepseek(q, context)
    return {"question": q, "answer": answer}
