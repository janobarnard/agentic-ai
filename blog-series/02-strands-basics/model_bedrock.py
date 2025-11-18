"""
Amazon Bedrock Model - AWS-Managed Models

AWS-managed models with enterprise features.
Requires AWS credentials configured.
"""

from strands import Agent
from strands.models.bedrock import BedrockModel

model = BedrockModel(
    model_id="us.anthropic.claude-sonnet-4-5-20250929-v1:0",
    temperature=0.7,
    max_tokens=4096
)

agent = Agent(model=model)
agent("What is agentic AI?")
