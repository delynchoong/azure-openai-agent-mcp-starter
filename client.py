import asyncio
import os
from dotenv import load_dotenv
from mcp import ClientSession, StdioServerParameters
from langchain_openai import AzureChatOpenAI
from mcp.client.stdio import stdio_client
from langchain_mcp_adapters.tools import load_mcp_tools
from langgraph.prebuilt import create_react_agent
from langchain_mcp_adapters.client import MultiServerMCPClient

# Load environment variables from .env file
load_dotenv()

client = MultiServerMCPClient(
    {
        "math": {
            "command": "python",
            # Make sure to update to the full absolute path to your math_server.py file
            "args": ["math_server.py"],
            "transport": "stdio",
        },
        "fabric": {
            "command": "python",
            # make sure you start your fabric server on port 8001
            "args": ["fabric_server.py"],
            "transport": "stdio",
        }
    }
)

# Define the model
model = AzureChatOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    deployment_name="gpt-4o",
    api_version=os.getenv("AZURE_OPENAI_VERSION")
)
async def run_agent(message = "what is 2+2?"):
       async with MultiServerMCPClient(
        {
            
            "math": {
                "command": "python",
                "args": ["math_server.py"],
                "transport": "stdio",
            },
            "fabric": {
                "command": "python",
                "args": ["fabric_server.py"],
                "transport": "stdio",
            }
        }
    ) as client:
           
        tools = client.get_tools()
        print("********* TOOLS ************")
        print(tools)    
        agent = create_react_agent(model, tools)
        agent_response = await agent.ainvoke({"messages": message})
        return agent_response["messages"][3].content

if __name__ == "__main__":
    result = asyncio.run(run_agent())
    print(result)

