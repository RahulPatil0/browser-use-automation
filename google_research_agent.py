import asyncio
from browser_use import Agent, Browser, ChatBrowserUse

async def main():
    # Create browser
    browser = Browser()

    # LLM provided by Browser-Use Cloud
    llm = ChatBrowserUse()

    # Agent with a multi-step task
    agent = Agent(
        task=(
            "Go to google.com, search for 'Proactive Patient Health Monitoring', "
            "open the most relevant result, and explain in simple terms what it is about."
        ),
        llm=llm,
        browser=browser,
    )

    # Run the agent
    result = await agent.run()

    print("\n--- FINAL ANSWER ---")
    print(result)

if __name__ == "__main__":
    asyncio.run(main())
