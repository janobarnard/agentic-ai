"""
Simple conversational agent using LangGraph with Ollama.
This demonstrates the basic agent loop without tools.
"""
from langchain.agents import create_agent
from langchain_ollama import ChatOllama

# Create model and agent
model = ChatOllama(model="llama3.2", base_url="http://localhost:11434")
agent = create_agent(model, tools=[])

# Chat with the agent
response = agent.invoke({"messages": [("user", "Tell me about Cape Town")]})
print(response["messages"][-1].content)
