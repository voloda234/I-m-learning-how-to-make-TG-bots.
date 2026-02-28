import asyncio

from openai import AsyncOpenAI

from config import AITOKEN


client = AsyncOpenAI(api_key=AITOKEN)


async def gpt_text(req, model):
    completion = await client.responses.create(
        input=req,
        model=model
    )
    return completion.output_text
