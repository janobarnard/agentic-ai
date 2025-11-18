"""
Tools - Class-Based Approach (Stateful)

Shows how to create tools that share state using classes.
Best for tools that need to share resources or maintain state.
"""

from strands import Agent, tool
from strands.models.ollama import OllamaModel

class DatabaseTools:
    def __init__(self, connection_string: str):
        self.connection = self._connect(connection_string)
        self.query_count = 0

    def _connect(self, connection_string: str):
        # Simulate database connection
        return {"connected": True, "db": "mydb"}

    @tool
    def query_users(self, limit: int = 10) -> dict:
        """Query users from the database.

        Args:
            limit: Maximum number of users to return
        """
        self.query_count += 1
        return {
            "users": [f"user{i}" for i in range(limit)],
            "query_count": self.query_count
        }

    @tool
    def get_stats(self) -> str:
        """Get database statistics."""
        return f"Total queries executed: {self.query_count}"

# Initialize tools with shared state
db_tools = DatabaseTools("postgresql://localhost/mydb")

# Pass tool methods to agent
model = OllamaModel(host="http://localhost:11434", model_id="llama3.2")
agent = Agent(
    model=model,
    tools=[db_tools.query_users, db_tools.get_stats]
)

response = agent("Show me 5 users, then tell me the stats")
print(response)
