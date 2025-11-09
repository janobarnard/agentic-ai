"""
Simple conversational agent using Strands with Ollama.
This demonstrates the basic agent loop without tools.
"""
from strands import Agent
from strands.models.ollama import OllamaModel

# Create model and agent
model = OllamaModel(host="http://localhost:11434", model_id="llama3.2")
agent = Agent(model=model)

# Chat with the agent
response = agent("Tell me about Cape Town")
print(response)
