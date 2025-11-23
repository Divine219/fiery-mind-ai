from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Message(BaseModel):
    text: str

@app.get("/")
def home():
    return {"status": "🔥 Fiery Mind AI Activated — The Mind Behind the Flame 🔥"}

@app.post("/talk")
def talk(message: Message):
    user = message.text.lower()

    if "hello" in user or "hey" in user:
        return {"reply": "🔥 Fiery Mind AI here. What do you need, King?"}

    if "who are you" in user:
        return {"reply": "I am Fiery Mind AI — the intelligence that burns through limits."}

    return {"reply": "Your thoughts are received. Tell me more."}
