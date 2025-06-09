from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, FileResponse
import uvicorn
import asyncio
import os
import json
from langchain_mcp_adapters.client import MultiServerMCPClient
from client import run_agent

app = FastAPI()

@app.post("/ask")
async def ask(request: Request):
    data = await request.json()
    message = data.get("message", "")
    result = await run_agent(message)
    return JSONResponse(content={"result": result})

@app.get("/")
async def root():
    frontend_path = os.path.join(os.path.dirname(__file__), "frontend.html")
    return FileResponse(frontend_path, media_type="text/html")

@app.get("/tools")
async def get_tools():
    # Load mcp.json for additional MCP servers (e.g., Azure AI Foundry)
    mcp_config = {}
    try:
        with open(os.path.join(".vscode", "mcp.json"), "r") as f:
            mcp_config = json.load(f)
    except Exception:
        pass
    # Build the config dict
    server_configs = {
        "math": {
            "command": "python",
            "args": ["math_server.py"],
            "transport": "stdio",
        },

        #"fabric": {
        #    "command": "python",
        #    "args": ["fabric_server.py"],
        #    "transport": "stdio",
        #}
    }
    # Add servers from mcp.json if present
    if "servers" in mcp_config:
        for name, cfg in mcp_config["servers"].items():
            args = [
                arg.replace("${workspaceFolder}", os.getcwd()) if isinstance(arg, str) else arg
                for arg in cfg["args"]
            ]
            server_configs[name] = {
                "command": cfg["command"],
                "args": args,
                "transport": cfg["type"]
            }
    async with MultiServerMCPClient(server_configs) as client:
        tools = client.get_tools()
        return {"tools": [
            {"name": t.name, "description": getattr(t, "description", "")}
            for t in tools
        ]}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
