"""
Simple conversational agent using LangGraph with OpenAI.
This demonstrates the basic agent loop without tools.
"""
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI

# Create model and agent
model = ChatOpenAI(model="gpt-4o-mini")
agent = create_agent(model, tools=[])

# Chat with the agent
response = agent.invoke({"messages": [("user", "Tell me about Cape Town")]})
print(response["messages"][-1].content)
