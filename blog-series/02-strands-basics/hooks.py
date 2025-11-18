"""
Hooks - Monitoring and Extending Agent Behavior

Shows how to use hooks to add logging and monitoring to agents.
"""

from strands import Agent, tool
from strands.models.ollama import OllamaModel
from strands.hooks import HookProvider, HookRegistry, BeforeInvocationEvent, AfterInvocationEvent, BeforeToolCallEvent, AfterToolCallEvent
import time

@tool
def get_weather(city: str) -> str:
    """Get current weather for a city.
    
    Args:
        city: The city name
    """
    time.sleep(0.1)  # Simulate API call
    return f"Weather in {city}: 22°C, partly cloudy"

class LoggingHook(HookProvider):
    def register_hooks(self, registry: HookRegistry) -> None:
        registry.add_callback(BeforeInvocationEvent, self.log_start)
        registry.add_callback(AfterInvocationEvent, self.log_end)

    def log_start(self, event: BeforeInvocationEvent) -> None:
        print(f"🚀 Agent '{event.agent.name}' starting request")

    def log_end(self, event: AfterInvocationEvent) -> None:
        print(f"✅ Agent '{event.agent.name}' completed request\n")

class ToolMonitor(HookProvider):
    def __init__(self):
        self.tool_times = {}

    def register_hooks(self, registry: HookRegistry) -> None:
        registry.add_callback(BeforeToolCallEvent, self.before_tool)
        registry.add_callback(AfterToolCallEvent, self.after_tool)

    def before_tool(self, event: BeforeToolCallEvent) -> None:
        tool_name = event.tool_use["name"]
        self.tool_times[tool_name] = time.time()
        print(f"🔧 Calling tool: {tool_name}")

    def after_tool(self, event: AfterToolCallEvent) -> None:
        tool_name = event.tool_use["name"]
        elapsed = time.time() - self.tool_times.get(tool_name, 0)
        print(f"✓ Tool {tool_name} completed in {elapsed:.2f}s")

# Create agent with hooks
model = OllamaModel(host="http://localhost:11434", model_id="llama3.2")
agent = Agent(
    model=model,
    name="MyAgent",
    tools=[get_weather],
    hooks=[LoggingHook(), ToolMonitor()]
)

agent("What's the weather in Paris?")
