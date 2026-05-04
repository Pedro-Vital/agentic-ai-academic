from agents import Agent, ModelSettings, function_tool
from tavily import TavilyClient
import os

client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

@function_tool
def tavily_search(query: str) -> str:
    """
    Perform a web search using Tavily and return a concise summary of results.
    """
    response = client.search(
        query=query,
        search_depth="advanced",
        max_results=5
    )
    
    results = []
    for r in response["results"]:
        results.append(f"{r['title']}\n{r['content']}")
    
    return "\n\n".join(results)


INSTRUCTIONS = "You are a research assistant. Given a search term, you search the web for that term and \
produce a concise summary of the results. The summary must 2-3 paragraphs and less than 300 \
words. Capture the main points. Write succintly, no need to have complete sentences or good \
grammar. This will be consumed by someone synthesizing a report, so it's vital you capture the \
essence and ignore any fluff. Do not include any additional commentary other than the summary itself."

search_agent = Agent(
    name="Search agent",
    instructions=INSTRUCTIONS,
    tools=[tavily_search],
    model="gpt-4o-mini",
    model_settings=ModelSettings(tool_choice="required"),
)
