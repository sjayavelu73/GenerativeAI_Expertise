import os
from dotenv import load_dotenv
from openai import AsyncOpenAI

load_dotenv()

async_client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

async def call_llm(prompt, json_mode=False):
    # Build params dynamically inside the function
    params = {
        "model": "gpt-4o-mini",
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.2
    }

    # Force JSON output if needed
    if json_mode:
        params["response_format"] = {"type": "json_object"}

    # Use params when calling async client
    response = await async_client.chat.completions.create(**params)
    return response.choices[0].message.content

