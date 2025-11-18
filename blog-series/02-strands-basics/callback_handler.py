"""
Callback Handler - Customizing Output

Shows how to control agent output behavior.
By default, agents print to stdout. Set callback_handler=None to disable.
"""

from strands import Agent
from strands.models.ollama import OllamaModel

model = OllamaModel(host="http://localhost:11434", model_id="llama3.2")

# Get the response without printing
agent = Agent(model=model, callback_handler=None)
response = agent("What is 2+2?")
print(f"Agent said: {response}")
