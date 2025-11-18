"""
Hello Strands - Your First Agent

Demonstrates the simplest possible Strands agent with just 3 lines of code.
Uses Amazon Bedrock (Claude 4 Sonnet) by default.
"""

from strands import Agent

agent = Agent()
agent("Tell me a joke about AI agents")
