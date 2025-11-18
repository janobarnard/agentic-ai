"""
FastAPI Integration - Streaming API Endpoint

Shows how to build a streaming API endpoint with FastAPI and Strands.

Install dependencies:
    pip install fastapi uvicorn

Run the server:
    uvicorn fastapi_streaming:app --reload

Test the endpoint:
    curl -X POST http://localhost:8000/stream -H "Content-Type: application/json" -d '{"prompt": "Tell me a joke"}'
"""

from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from strands import Agent
from strands.models.ollama import OllamaModel

app = FastAPI()

class PromptRequest(BaseModel):
    prompt: str

@app.post("/stream")
async def stream_response(request: PromptRequest):
    async def generate():
        model = OllamaModel(host="http://localhost:11434", model_id="llama3.2")
        agent = Agent(model=model, callback_handler=None)

        async for event in agent.stream_async(request.prompt):
            if "data" in event:
                yield event["data"]

    return StreamingResponse(generate(), media_type="text/plain")
