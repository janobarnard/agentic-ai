"""
Synchronous Streaming - Simple Real-Time Output

Shows the simplest way to stream responses using the default callback handler.
"""

from strands import Agent
from strands.models.ollama import OllamaModel

model = OllamaModel(host="http://localhost:11434", model_id="llama3.2")
agent = Agent(model=model)

# Stream with default callback handler (prints to stdout)
agent("Write a short story about an AI agent")

# The response streams to the console in real-time!
