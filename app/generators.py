import asyncio

from openai import AsyncOpenAI

from config import AITOKEN


client = AsyncOpenAI(api_key=AITOKEN)


async def gpt_text(req, model):
    completion = await client.responses.create(
        input=req,
        model=model
    )
    return {'response':completion.output_text,
            'usege': completion.usage.total_tokens}
