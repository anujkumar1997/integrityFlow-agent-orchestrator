from __future__ import annotations
import requests

OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL = "llama3.1:8b"

def chat(prompt:str) -> str:
    payload = {
        "model": MODEL,
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "stream": False,
    }

## Call requests.post with the correct parameters to send the payload to the OLLAMA_URL
    response = requests.post(OLLAMA_URL, json=payload, timeout=30)

## if response status is not 200, raise RuntimeError with response text
    if response.status_code != 200:
        raise RuntimeError(f"Request failed with status {response.status_code}: {response.text}")
    
## return the content of the first choice message from the response json
    return response.json()["message"]["content"]

    