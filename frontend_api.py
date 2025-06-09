from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, FileResponse
import uvicorn
import asyncio
import os
from client import run_agent

app = FastAPI()

@app.post("/ask")
async def ask(request: Request):
    data = await request.json()
    message = data.get("message", "")
    # Patch run_agent to accept message
    result = await run_agent(message)
    return JSONResponse(content={"result": result})

@app.get("/")
async def root():
    frontend_path = os.path.join(os.path.dirname(__file__), "frontend.html")
    return FileResponse(frontend_path, media_type="text/html")

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
   