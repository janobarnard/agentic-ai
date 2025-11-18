"""
System Prompt - Guiding Agent Behavior

Shows how to use a system prompt to set the agent's personality and response style.
"""

from strands import Agent
from strands.models.ollama import OllamaModel

model = OllamaModel(host="http://localhost:11434", model_id="llama3.2")

agent = Agent(
    model=model,
    system_prompt="You are a helpful assistant that provides concise, technical responses.",
)

agent("Explain what an API is")
