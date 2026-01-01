import asyncio
from browser_use import Agent, Browser, ChatBrowserUse


async def main():
    browser = Browser()
    llm = ChatBrowserUse()

    agent = Agent(
        task=(
            "Search Google for 'Proactive Patient Health Monitoring'. "
            "Open ONE reliable article (prefer .gov, .edu, or peer-reviewed sources). "
            "Extract the following ONLY if explicitly stated in the article:\n\n"
            "1. A short definition\n"
            "2. Key benefits (as bullet points)\n"
            "3. Common use cases (as bullet points)\n\n"
            "Return ONLY valid JSON with keys:\n"
            "definition, benefits, use_cases.\n\n"
            "IMPORTANT RULES:\n"
            "- If a definition is NOT explicitly present, set \"definition\": null\n"
            "- Do NOT infer, summarize, or fabricate missing information\n"
            "- Do NOT add explanations, markdown, or extra text\n"
            "- Output JSON only"
        ),
        llm=llm,
        browser=browser,
    )

    # Browser-Use will automatically save JSON as an attachment
    await agent.run()

    print("✅ Task completed. JSON file saved by browser-use (see attachment path above).")


if __name__ == "__main__":
    asyncio.run(main())
