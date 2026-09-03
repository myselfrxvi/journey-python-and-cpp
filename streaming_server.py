import asyncio
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import json

app = FastAPI(title="Live AI Streaming API")

async def genllm(prompt: str):
    message = f"AI thinking about: '{prompt}'... Here is the live streamed output: PyTorch tensors converge with gradient descent!"
    for word in message.split():
        await asyncio.sleep(0.5)
        yield word + " "

@app.get("/stream")
async def stream_chat(prompt: str = 'Deep learning'):
     return StreamingResponse(genllm(prompt), media_type="text/plain")
     
async def gen_sse(prompt: str):
    words = ["OpenAI", "and", "Claude", "stream", "tokens", "using", "Server-Sent", "Events!"]
    for word in words:
        await asyncio.sleep(0.3)
        payload = json.dumps({"token": word})
        yield f"data: {payload}\n\n"
        
    yield "data: [DONE]\n\n"

@app.get("/stream-sse")
async def stream_sse():
    return StreamingResponse(gen_sse("AI"), media_type="text/event-stream")
