from langchain.agents import create_agent
from langchain_core.messages import SystemMessage
from langchain_core.tools import tool

from langchain_openai import ChatOpenAI
from langchain_community.tools.tavily_search import TavilySearchResults
from dotenv import load_dotenv
load_dotenv()

model = ChatOpenAI(model="gpt-o4-mini")

system_message = SystemMessage(content="""
You are a helpful researcher.
Use the 'search' tool whenever necessary, 
specially with questions depending on web.
"""
)

@tool("search")
def search_web(query: str = "") -> str:
    """
    Search for information in web.
    
    Args:
        query: Keywords to search in the web
        
    Returns: 
        The information resulting from the web search 
        or a message indicating that nothing was found.
    """
    tavily_search = TavilySearchResults(max_results=3)
    search_docs = tavily_search.invoke(query)
    return search_docs
    
tools = [search_web]
graph = create_agent(
    model, 
    tools=tools,
    system_prompt=system_message
)

export_graph = graph