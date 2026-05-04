import asyncio
from agents import Agent, Runner, function_tool
from dotenv import load_dotenv
load_dotenv()

@function_tool
def history_fun_fact() -> str:
    """Return a short history fact."""
    return "Sharks are older than trees."


agent = Agent(
    name="History Tutor",
    instructions="Answer history questions clearly. Use history_fun_fact when it helps.",
    tools=[history_fun_fact],
    model="gpt-4o-mini",
)


async def main():
    result = await Runner.run(
        agent,       
        "Tell me something surprising about ancient life on Earth.",  
    )

    print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())
