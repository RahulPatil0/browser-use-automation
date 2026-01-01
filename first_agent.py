import asyncio
from browser_use import Agent, Browser, ChatBrowserUse

async def main():
    # Start a browser instance
    browser = Browser()

    # Use default LLM (cloud/local depending on setup)
    llm = ChatBrowserUse()

    # Define a simple task
    agent = Agent(
        task="Open github.com and tell me what this website is about.",
        browser=browser,
        llm=llm,
    )

    # Run the agent
    result = await agent.run()
    print("\n--- AGENT RESULT ---")
    print(result)

if __name__ == "__main__":
    asyncio.run(main())
