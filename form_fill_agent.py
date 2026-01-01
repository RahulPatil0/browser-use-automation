import asyncio
from browser_use import Agent, Browser, ChatBrowserUse


async def main():
    browser = Browser()
    llm = ChatBrowserUse()

    agent = Agent(
        task=(
            "Open https://www.techlistic.com/p/selenium-practice-form.html\n"
            "Fill the form with the following details exactly:\n"
            "- First Name: Rahul\n"
            "- Last Name: Patil\n"
            "- Country: India\n"
            "- Website: example.com\n"
            "- Comments: Testing automated form filling using browser agent\n"
            "Submit the form.\n"
            "Do NOT switch to any other website."
        ),
        llm=llm,
        browser=browser,
    )

    await agent.run()
    print("✅ Form filled and submitted successfully")


if __name__ == "__main__":
    asyncio.run(main())
