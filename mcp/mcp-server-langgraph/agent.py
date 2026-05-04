import asyncio
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langchain_core.messages import SystemMessage
from langchain_mcp_adapters.client import MultiServerMCPClient
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini")

system_message=SystemMessage("""
You're an assistant capable of providing information about shows on streaming services.

Available tools on MCP Server: get_hbo_show(streaming: str) -> str 

You are the bridge between the user and the MCP tool.""")

async def build_agent():
    client = MultiServerMCPClient(
        {
            "streaming": {
                "command": "python",
                "args": ["mcp_server.py"],
                "transport": "stdio",
            }
        }
    )

    tools = await client.get_tools()

    agent = create_agent(
        llm,
        tools=tools,
        system_prompt=system_message
    )

    return agent