"""
Ollama Model - Local, Free Models

Perfect for development and learning.
Requires Ollama installed and model pulled.
"""

from strands import Agent
from strands.models.ollama import OllamaModel

model = OllamaModel(
    host="http://localhost:11434",
    model_id="llama3.2",
    temperature=0.7,
    keep_alive="10m",
    max_tokens=2000
)

agent = Agent(model=model)
agent("What is agentic AI?")
