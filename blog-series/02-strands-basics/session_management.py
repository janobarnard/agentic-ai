"""
Session Management - Agents That Remember

Shows how to persist conversation history across restarts using FileSessionManager.

For production deployments, consider using S3SessionManager for distributed environments:
https://strandsagents.com/latest/documentation/docs/user-guide/concepts/agents/session-management/
"""

from strands import Agent
from strands.models.ollama import OllamaModel
from strands.session.file_session_manager import FileSessionManager

# Create a session manager
session_manager = FileSessionManager(session_id="user-123")

model = OllamaModel(host="http://localhost:11434", model_id="llama3.2")

# Agent with memory
agent = Agent(model=model, session_manager=session_manager)

# First conversation
print("First conversation:")
agent("My name is Alice and I love Python")

# Later (even after restart)...
print("\nSecond conversation:")
agent("What's my name?")  # "Your name is Alice"

print("\nThird conversation:")
agent("What do I love?")  # "You love Python"
