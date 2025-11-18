"""
Tools - Decorator Approach (Simplest)

Shows how to create tools using the @tool decorator.
Best for simple, stateless tools.
"""

from strands import Agent, tool
from strands.models.ollama import OllamaModel

@tool
def get_weather(city: str, units: str = "celsius") -> str:
    """Get current weather for a city.

    Args:
        city: The name of the city
        units: Temperature units (celsius or fahrenheit)
    """
    # In a real app, you'd call a weather API
    return f"Weather in {city}: 22°{units[0].upper()}, partly cloudy"

@tool
def calculate(expression: str) -> str:
    """Evaluate a mathematical expression.

    Args:
        expression: The math expression to evaluate (e.g., "2 + 2")
    """
    try:
        result = eval(expression)
        return f"Result: {result}"
    except Exception as e:
        return f"Error: {str(e)}"

# Create agent with tools
model = OllamaModel(host="http://localhost:11434", model_id="llama3.2")
agent = Agent(model=model, tools=[get_weather, calculate])

# The agent will automatically use tools when needed
response = agent("What's the weather in London and what's 15 * 7?")
print(response)
