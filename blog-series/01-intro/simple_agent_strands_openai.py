"""
Simple conversational agent using Strands with OpenAI.
This demonstrates the basic agent loop without tools.
"""
from strands import Agent
from strands.models.openai import OpenAIModel
import os

# Create model and agent
model = OpenAIModel(
    client_args={"api_key": os.environ.get("OPENAI_API_KEY")},
    model_id="gpt-4o-mini"
)
agent = Agent(model=model)

# Chat with the agent
response = agent("Tell me about Cape Town")
print(response)
