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


async def gpt_image(req, model):
    response = await client.images.generate(
        model='dall-e-3',
        prompt=req,
        size='1024x1024',
        quality='standard',
        n=1
    )
    return {'response':response.data[0].url,
            'usege': 1}
