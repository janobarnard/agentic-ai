"""
Structured Output - Type-Safe Responses

Shows how to get structured, type-safe responses using Pydantic models.
"""

from strands import Agent
from strands.models.ollama import OllamaModel
from pydantic import BaseModel, Field

# Define the structure you want
class WeatherData(BaseModel):
    """Structured weather information"""
    city: str = Field(description="City name")
    temperature: int = Field(description="Temperature in Celsius")
    condition: str = Field(description="Weather condition")
    humidity: int = Field(description="Humidity percentage")

model = OllamaModel(host="http://localhost:11434", model_id="llama3.2")
agent = Agent(model=model)

# Get structured output instead of text
result = agent(
    "The weather in London is 18°C, partly cloudy with 65% humidity",
    structured_output_model=WeatherData
)

# Access typed fields directly
weather: WeatherData = result.structured_output
print(f"{weather.city}: {weather.temperature}°C, {weather.condition}")
print(f"Humidity: {weather.humidity}%")
