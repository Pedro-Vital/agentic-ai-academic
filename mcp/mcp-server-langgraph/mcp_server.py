from mcp.server.fastmcp import FastMCP

mcp = FastMCP("StreamingServer")

@mcp.tool()
def get_hbo_show(streaming: str) -> str:
    """Return the best HBO show for the given streaming service"""
    if "hbo" in streaming.lower():
        return "Game of Thrones"
    return "Not available"

if __name__ == "__main__":
    mcp.run(transport="stdio")