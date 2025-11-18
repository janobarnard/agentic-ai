"""
Weather Assistant - Comprehensive Example

Combines everything: tools, hooks, and multi-step reasoning.
A practical weather assistant agent.
"""

from strands import Agent, tool
from strands.models.ollama import OllamaModel
from strands.hooks import HookProvider, HookRegistry, BeforeToolCallEvent

# Define tools
@tool
def get_weather(city: str) -> dict:
    """Get current weather for a city.

    Args:
        city: The city name
    """
    # Using a real weather API (you'll need an API key)
    # For demo, we'll simulate the response
    return {
        "city": city,
        "temperature": 22,
        "condition": "Partly cloudy",
        "humidity": 65,
        "wind_speed": 15
    }

@tool
def get_forecast(city: str, days: int = 3) -> dict:
    """Get weather forecast for a city.

    Args:
        city: The city name
        days: Number of days to forecast (1-7)
    """
    return {
        "city": city,
        "forecast": [
            {"day": 1, "temp": 23, "condition": "Sunny"},
            {"day": 2, "temp": 21, "condition": "Cloudy"},
            {"day": 3, "temp": 19, "condition": "Rainy"}
        ][:days]
    }

@tool
def convert_temperature(temp: float, from_unit: str, to_unit: str) -> float:
    """Convert temperature between Celsius and Fahrenheit.

    Args:
        temp: Temperature value
        from_unit: Source unit (celsius or fahrenheit)
        to_unit: Target unit (celsius or fahrenheit)
    """
    if from_unit == "celsius" and to_unit == "fahrenheit":
        return (temp * 9/5) + 32
    elif from_unit == "fahrenheit" and to_unit == "celsius":
        return (temp - 32) * 5/9
    return temp

# Create a logging hook
class WeatherAgentHook(HookProvider):
    def register_hooks(self, registry: HookRegistry) -> None:
        registry.add_callback(BeforeToolCallEvent, self.log_tool)

    def log_tool(self, event: BeforeToolCallEvent) -> None:
        tool_name = event.tool_use["name"]
        tool_input = event.tool_use["input"]
        print(f"📍 Using {tool_name} with: {tool_input}")

# Create the agent with Ollama
model = OllamaModel(host="http://localhost:11434", model_id="llama3.2")
agent = Agent(
    model=model,
    name="WeatherAssistant",
    description="A helpful weather assistant that provides current weather and forecasts",
    tools=[get_weather, get_forecast, convert_temperature],
    hooks=[WeatherAgentHook()]
)

# Use the agent
print("=== Weather Assistant ===\n")

# Simple query
agent("What's the weather in London?")

print("\n" + "="*50 + "\n")

# Complex query requiring multiple tools
agent("Get the 3-day forecast for Tokyo and convert the temperatures to Fahrenheit")

print("\n" + "="*50 + "\n")

# Conversational follow-up
agent("What about Paris?")
