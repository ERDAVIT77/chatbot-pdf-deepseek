import requests
import os

DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY", "your-deepseek-api-key")

def ask_deepseek(question, context):
    url = "https://api.deepseek.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
        "Content-Type": "application/json"
    }
    body = {
        "model": "deepseek-chat",
        "messages": [
            {"role": "system", "content": "Responde de forma clara y precisa según el contexto proporcionado."},
            {"role": "user", "content": f"Contexto: {context}\n\nPregunta: {question}"}
        ]
    }
    response = requests.post(url, headers=headers, json=body)
    return response.json().get("choices", [{}])[0].get("message", {}).get("content", "Sin respuesta.")
