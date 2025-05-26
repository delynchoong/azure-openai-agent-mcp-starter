import asyncio
import os
from dotenv import load_dotenv
from mcp import ClientSession, StdioServerParameters
from langchain_openai import AzureChatOpenAI
from mcp.client.stdio import stdio_client
from langchain_mcp_adapters.tools import load_mcp_tools
from langgraph.prebuilt import create_react_agent

# Load environment variables from .env file
load_dotenv()

# Define server parameters
server_params = StdioServerParameters(
    command="python",
    args=["math_server.py"],
)

# Define the model
model = AzureChatOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    deployment_name="gpt-4o",
    api_version=os.getenv("AZURE_OPENAI_VERSION")
)
async def run_agent():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            tools = await load_mcp_tools(session)
            agent = create_react_agent(model, tools)
            agent_response = await agent.ainvoke({"messages": "what's (4 + 6) x 14?"})
            return agent_response["messages"][3].content

if __name__ == "__main__":
    result = asyncio.run(run_agent())
    print(result)