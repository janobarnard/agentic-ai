"""
Tools - Module-Based Approach (Framework Independent)

Shows how to use module-based tools that don't depend on Strands.
Best for reusable tools across multiple frameworks.
"""

from strands import Agent
from strands.models.ollama import OllamaModel
import weather_tool

model = OllamaModel(host="http://localhost:11434", model_id="llama3.2")

# Load tool from module
agent = Agent(model=model, tools=[weather_tool])

response = agent("What's the weather in Paris?")
print(response)
