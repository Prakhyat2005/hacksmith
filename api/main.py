from fastapi import FastAPI

app = FastAPI(
    title="HackSmith",
    description="Your AI Blacksmith for Cybersecurity",
    version="0.1.0"
)

@app.get("/")
def root():
    return {"message": "Welcome to HackSmith – Your AI Blacksmith for Cybersecurity"}

@app.post("/ask")
def ask(query: dict):
    # Temporary placeholder until AI integration
    return {"answer": f"Received your query: {query.get('query', '')}"}
