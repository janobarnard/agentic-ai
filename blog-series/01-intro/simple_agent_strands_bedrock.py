"""
Simple conversational agent using Strands with Amazon Bedrock.
This demonstrates the basic agent loop without tools.
"""

from strands import Agent
from strands.models.bedrock import BedrockModel

# Create model and agent
model = BedrockModel(model_id="us.anthropic.claude-haiku-4-5-20251001-v1:0")
agent = Agent(model=model)

# Chat with the agent
response = agent("Tell me about Cape Town")
print(response)
