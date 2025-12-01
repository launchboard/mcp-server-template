import asyncio
from fastmcp import Client

client = Client("http://localhost:8000/mcp")


async def call_tool():
    async with client:
        result = await client.call_tool("get_introduction")
        print(result)


asyncio.run(call_tool())
