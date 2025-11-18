"""
Switching Models at Runtime

Shows how to update model configuration on the fly.
Demonstrates temperature differences: low (factual) vs high (creative).
"""

from strands import Agent, tool
from strands.models.ollama import OllamaModel

# Start with low temperature (more factual, consistent)
model = OllamaModel(host="http://localhost:11434", model_id="llama3.2", temperature=0.1)
agent = Agent(model=model)

print("Using temperature 0.1 (factual, consistent):")
agent("Write a creative opening line for a story about a robot")

print("\n" + "="*50 + "\n")

# Switch to high temperature (more creative, varied)
model.update_config(temperature=1.0)

print("Switched to temperature 1.0 (creative, varied):")
agent("Write a creative opening line for a story about a robot")

print("\n" + "="*50 + "\n")

# Or even let a tool change the configuration
@tool
def switch_to_creative_mode(agent: Agent) -> str:
    """Switch to a more creative model configuration."""
    agent.model.update_config(temperature=1.0)
    return "Switched to creative mode with temperature 1.0!"

agent_with_tool = Agent(model=model, tools=[switch_to_creative_mode])
agent_with_tool("Switch to creative mode and write an opening line for a story about a robot")
