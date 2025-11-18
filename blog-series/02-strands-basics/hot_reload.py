"""
Hot Reloading - Automatic Tool Loading

Shows how to enable automatic tool loading from a directory for rapid development.
Place tool files in ./tools/ directory and they're automatically loaded.
"""

import os
from pathlib import Path

from strands import Agent
from strands.models.bedrock import BedrockModel

# Change to script directory so ./tools/ is found correctly
script_dir = Path(__file__).parent
os.chdir(script_dir)

model = BedrockModel(
    model_id="us.anthropic.claude-sonnet-4-5-20250929-v1:0",
)

# Agent watches ./tools/ directory for changes
agent = Agent(model=model, load_tools_from_directory=True, callback_handler=None)

# Add/modify tools in ./tools/ and they're automatically reloaded!
response = agent("Greet me by name - my name is Alex")
print(response)
