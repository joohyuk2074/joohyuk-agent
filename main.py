from fastapi import FastAPI 

app = FastAPI

@app.post("/v1/chat/completions")
async def chat():
    return {"Hello Fast API"}


@app.get("/v1/models")
async def llmList():
    return {"list"}