import requests

OLLAMA_URL = "http://localhost:11434/api/generate"


def run_llm(prompt, content):
    response = requests.post(
        OLLAMA_URL,
        json={
            "model": "llama3",
            "prompt": prompt + "\n\n" + content,
            "stream": False
        }
    )

    return response.json()["response"]
