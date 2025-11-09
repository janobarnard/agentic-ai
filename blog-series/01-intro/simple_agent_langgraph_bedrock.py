"""
Simple conversational agent using LangGraph with Amazon Bedrock.
This demonstrates the basic agent loop without tools.
"""

from langchain.agents import create_agent
from langchain_aws import ChatBedrock

# Create model and agent
model = ChatBedrock(model_id="us.anthropic.claude-haiku-4-5-20251001-v1:0", region_name="us-east-1")
agent = create_agent(model, tools=[])

# Chat with the agent
response = agent.invoke({"messages": [("user", "Tell me about Cape Town")]})
print(response["messages"][-1].content)
