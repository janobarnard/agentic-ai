"""
Hello Strands with Ollama - Free Local Alternative

Uses Ollama to run models locally for free.
Requires: ollama installed and llama3.2 model pulled
"""

from strands import Agent
from strands.models.ollama import OllamaModel

model = OllamaModel(host="http://localhost:11434", model_id="llama3.2")

agent = Agent(model=model)
agent("Tell me a joke about AI agents")
