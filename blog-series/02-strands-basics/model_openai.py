"""
OpenAI Model - Industry-Standard Models

Requires OpenAI API key and credits.
Install with: pip install 'strands-agents[openai]'
"""

from strands import Agent
from strands.models.openai import OpenAIModel

model = OpenAIModel(
    model_id="gpt-5-nano",
    params={
        "max_completion_tokens": 2000
    }
)  # Set OPENAI_API_KEY env var

agent = Agent(model=model)
agent("What is agentic AI?")
