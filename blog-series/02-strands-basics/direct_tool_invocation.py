"""
Direct Tool Invocation

Shows how to call tools directly without going through the agent loop.
Useful for testing tools or pre-populating agent knowledge.
"""

from strands import Agent
from strands.models.ollama import OllamaModel
from strands_tools import calculator

model = OllamaModel(host="http://localhost:11434", model_id="llama3.2")
agent = Agent(model=model, tools=[calculator])

# Call tool directly (bypasses the agent loop)
print("Direct tool call:")
result = agent.tool.calculator(expression="sin(x)", mode="derive", wrt="x")
print(result)

print("\n" + "="*50 + "\n")

# Then use in conversation
print("Conversational use:")
agent("What's the derivative of sin(x)?")
