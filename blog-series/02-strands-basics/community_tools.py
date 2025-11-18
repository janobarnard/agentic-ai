"""
Community Tools - Pre-Built Tools

Shows how to use pre-built tools from the strands-agents-tools package.
"""

from strands import Agent
from strands.models.ollama import OllamaModel
from strands_tools import calculator, current_time

# You might notice that this Ollama model with tools is much slower than without tools
# Use a more capable model for better performance with tools or use a remote API-based model
model = OllamaModel(host="http://localhost:11434", model_id="llama3.2")

agent = Agent(model=model, tools=[calculator, current_time], callback_handler=None)

response = agent("What is the current UTC time?")
print(response)

print("-" * 50)

response = agent("What is 12345 multiplied by 6789?")
print(response)
