# Building Your First Agent with Strands - Code Examples

Practical examples demonstrating Strands core concepts: agents, models, tools, streaming, structured output, sessions, and hooks.

## Cost Overview

- **Ollama**: Free (runs locally on your device)
- **Amazon Bedrock**: ~$0.003-0.015 per request depending on model (pay-as-you-go)

All examples use Ollama by default for free local development.

## Getting the Code

```bash
git clone https://github.com/janobarnard/agentic-ai.git
cd agentic-ai/blog-series/02-strands-basics
```

## Prerequisites

### For Ollama (Local - Recommended)

1. **Install Ollama**: Download from [ollama.ai](https://ollama.ai/) and install for your OS

2. **Pull the model**:
   ```bash
   ollama pull llama3.2
   ```

3. **Ensure Ollama is running**:
   - **Windows/Mac**: Ollama runs automatically (check system tray)
   - **Linux**: Run `ollama serve` in a terminal

### For Amazon Bedrock (Optional)

1. **AWS Credentials**: Set your AWS credentials as environment variables:
   ```bash
   # Mac/Linux
   export AWS_ACCESS_KEY_ID=your_access_key
   export AWS_SECRET_ACCESS_KEY=your_secret_key
   export AWS_DEFAULT_REGION=us-east-1

   # Windows (PowerShell)
   $env:AWS_ACCESS_KEY_ID="your_access_key"
   $env:AWS_SECRET_ACCESS_KEY="your_secret_key"
   $env:AWS_DEFAULT_REGION="us-east-1"
   ```

2. **Model Access**: Bedrock models are auto-enabled as of October 2025

## Installation

```bash
pip install -r requirements.txt
```

## Running the Examples

### Basic Examples

```bash
# Hello Strands (simplest agent)
python hello_strands.py                # Uses Bedrock
python hello_strands_ollama.py         # Uses Ollama

# System Prompt (guide agent behavior)
python system_prompt.py

# Callback Handler (control output)
python callback_handler.py

# Model Providers
python model_bedrock.py                # Amazon Bedrock
python model_ollama.py                 # Ollama (local)
python model_openai.py                 # OpenAI
python model_switching.py              # Switch models at runtime
```

### Tools Examples

```bash
# Decorator approach (simplest)
python tools_decorator.py

# Class-based approach (stateful)
python tools_class.py

# Module-based approach (framework-independent)
python tools_module.py

# Community tools (pre-built)
python community_tools.py

# Direct tool invocation
python direct_tool_invocation.py
```

### Advanced Features

```bash
# Streaming responses (async)
python streaming.py

# Streaming responses (sync)
python streaming_sync.py

# FastAPI streaming endpoint
python fastapi_streaming.py

# Hot reloading tools from directory
python hot_reload.py

# Logging and debugging
python logging_debug.py

# Structured output (type-safe)
python structured_output.py

# Session management (persistence)
python session_management.py

# Hooks (monitoring)
python hooks.py
```

### Comprehensive Example

```bash
# Weather assistant (combines everything)
python weather_assistant.py
```

## What Each Example Demonstrates

| File | Concept | Key Takeaway |
|------|---------|--------------|
| `hello_strands.py` | Basic agent | 3 lines of code to create an agent |
| `hello_strands_ollama.py` | Local models | Free alternative with Ollama |
| `system_prompt.py` | System prompts | Guide agent behavior and personality |
| `callback_handler.py` | Output control | Customize printing behavior |
| `model_bedrock.py` | Bedrock models | AWS-managed models |
| `model_ollama.py` | Ollama models | Local model configuration |
| `model_openai.py` | OpenAI models | Industry-standard models |
| `model_switching.py` | Runtime switching | Change models on the fly |
| `tools_decorator.py` | Tool decorator | Simplest way to add tools |
| `tools_class.py` | Class-based tools | Tools that share state |
| `tools_module.py` | Module tools | Framework-independent tools |
| `weather_tool.py` | Module tool file | Example tool module for tools_module.py |
| `community_tools.py` | Community tools | Pre-built tools package |
| `direct_tool_invocation.py` | Direct tool calls | Call tools without agent loop |
| `streaming.py` | Async streaming | Real-time response streaming (async) |
| `streaming_sync.py` | Sync streaming | Real-time response streaming (sync) |
| `fastapi_streaming.py` | FastAPI integration | Streaming HTTP API endpoint |
| `hot_reload.py` | Hot reloading | Auto-load tools from directory |
| `logging_debug.py` | Logging & debugging | Enable debug logs and inspect metrics |
| `structured_output.py` | Pydantic models | Type-safe structured responses |
| `session_management.py` | Persistence | Agents that remember across restarts |
| `hooks.py` | Lifecycle hooks | Monitor and extend agent behavior |
| `weather_assistant.py` | Full example | Combines all concepts |

## Troubleshooting

### Ollama Connection Error

If you get "Connection refused" errors:
- Ensure Ollama is running (`ollama serve` on Linux)
- Check Ollama is on port 11434: `curl http://localhost:11434`

### Model Not Found

If you get "model not found" errors:
- Pull the model: `ollama pull llama3.2`
- List available models: `ollama list`

### AWS Credentials

If using Bedrock and getting auth errors:
- Verify credentials are set: `echo $AWS_ACCESS_KEY_ID`
- Check region is correct: `echo $AWS_DEFAULT_REGION`

## What's Next?

Check out the blog post for detailed explanations: [Building Your First Agent with Strands](https://janobarnard.com/building-first-agent-strands/)

Next in the series:
- **Post 3**: Deploying to Amazon Bedrock AgentCore
- **Post 4**: Multi-Agent Architectures
- **Post 5**: RAG with Knowledge Bases
