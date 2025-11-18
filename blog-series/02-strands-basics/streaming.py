"""
Streaming Responses - Real-Time Output

Shows how to stream responses as they're generated for better UX.
"""

import asyncio
from strands import Agent
from strands.models.ollama import OllamaModel

async def stream_example():
    model = OllamaModel(host="http://localhost:11434", model_id="llama3.2")
    agent = Agent(model=model, callback_handler=None)

    print("Streaming response:\n")
    async for event in agent.stream_async("Tell me about Cape Town"):
        if "data" in event:
            # Stream text chunks
            print(event["data"], end="", flush=True)
        elif "current_tool_use" in event:
            # Tool is being used
            tool_name = event["current_tool_use"].get("name")
            if tool_name:
                print(f"\n[Using tool: {tool_name}]\n")
    
    print("\n\nDone!")

asyncio.run(stream_example())
