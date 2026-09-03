import asyncio

async def stream_words():
    words = ["Python", "Streams", "Are", "Fast", "Token"]

    for word in words:
        await asyncio.sleep(0.5)
        yield word + " "

async def stream_for_user(username: str):
   async for words in stream_words():
        print(f"[{username}]: {words}")

async def main():
    await asyncio.gather(
        stream_for_user("Anna"),
        stream_for_user("Bob"),
        stream_for_user("Sonia")
    )
    

asyncio.run(main())