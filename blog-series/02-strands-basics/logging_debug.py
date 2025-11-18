"""
Logging and Debugging - Monitor Agent Behavior

Shows how to enable debug logging and inspect agent metrics.
"""

import logging
from strands import Agent, tool
from strands.models.ollama import OllamaModel

# Enable Strands debug logs
logging.getLogger("strands").setLevel(logging.DEBUG)

# Configure log format
logging.basicConfig(
    format="%(levelname)s | %(name)s | %(message)s",
    handlers=[logging.StreamHandler()]
)

@tool
def my_tool(value: int) -> int:
    """Multiply a value by 2"""
    return value * 2

model = OllamaModel(host="http://localhost:11434", model_id="llama3.2")
agent = Agent(model=model, tools=[my_tool])

result = agent("Use my_tool to double the number 21")

# Check metrics
print("\n" + "="*50)
print("METRICS:")
print(f"Total tokens: {result.metrics.accumulated_usage['totalTokens']}")
print(f"Input tokens: {result.metrics.accumulated_usage['inputTokens']}")
print(f"Output tokens: {result.metrics.accumulated_usage['outputTokens']}")
print(f"Latency: {result.metrics.accumulated_metrics['latencyMs']}ms")
print(f"Cycles: {result.metrics.cycle_count}")
print(f"Tool calls: {len(result.metrics.tool_metrics)}")

# Inspect conversation history
print("\n" + "="*50)
print("CONVERSATION HISTORY:")
for msg in agent.messages:
    print(f"{msg['role']}: {msg['content'][:100]}...")
