import asyncio
import os

from openai import AsyncOpenAI
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

client = AsyncOpenAI(api_key=api_key)

async def call_async_openai(prompt: str, model: str = "gpt-5-mini") -> str:
    response = await client.chat.completions.create(
        model=model,
        messages=[{"role":"user", "content":prompt}],
    )
    
    return response.choices[0].message.content

async def main():
    prompt = "비동기 프로그래밍에 대해 두세 문장으로 설명해 주세요."
    openai_task = call_async_openai(prompt)
    print(f"응답: {openai_task}")

if __name__ == "__main__":
    asyncio.run(main())