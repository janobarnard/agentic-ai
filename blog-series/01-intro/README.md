# Introduction to Agentic AI - Code Examples

Simple conversational agents demonstrating the agent loop using Strands and LangGraph with Ollama, Amazon Bedrock, or OpenAI.

## Cost Overview

- **Ollama**: Free (runs locally on your device)
- **Amazon Bedrock**: ~$0.003 per request with Claude Haiku 4.5 (pay-as-you-go)
- **OpenAI**: ~$0.0003 per request with GPT-4o-mini (requires credits)

Running these simple examples will cost less than $0.01 total for cloud providers.

## Getting the Code

1. **Install VS Code** (recommended): Download from [code.visualstudio.com](https://code.visualstudio.com/) - includes Git built-in

   - Alternatively, install Git separately from [git-scm.com](https://git-scm.com/downloads)

2. **Clone the repository**:

   ```bash
   git clone https://github.com/janobarnard/agentic-ai.git
   cd agentic-ai/blog-series/01-intro
   ```

## Prerequisites

### For Ollama (Local)

1. **Install Ollama**: Download from [ollama.ai](https://ollama.ai/) and install for your OS (Windows, Mac, or Linux)

2. **Pull the model**:

   ```bash
   ollama pull llama3.2
   ```

3. **Ensure Ollama is running**:
   - **Windows/Mac**: Ollama runs automatically (check system tray)
   - **Linux**: Run `ollama serve` in a terminal if it doesn't run automatically

### For Amazon Bedrock (Cloud)

1. **AWS Credentials**: Set your AWS credentials as environment variables:

   ```bash
   # Windows (Command Prompt)
   set AWS_ACCESS_KEY_ID=your_access_key
   set AWS_SECRET_ACCESS_KEY=your_secret_key
   set AWS_SESSION_TOKEN=your_session_token

   # Windows (PowerShell)
   $env:AWS_ACCESS_KEY_ID="your_access_key"
   $env:AWS_SECRET_ACCESS_KEY="your_secret_key"
   $env:AWS_SESSION_TOKEN="your_session_token"

   # Mac/Linux
   export AWS_ACCESS_KEY_ID=your_access_key
   export AWS_SECRET_ACCESS_KEY=your_secret_key
   export AWS_SESSION_TOKEN=your_session_token
   ```

2. **Model Access**: Ensure you have access to Claude Haiku 4.5 in us-east-1 (or any US region with the `us.` prefix)

3. **Region**: Set your AWS region via environment variable if not using `us-east-1`:

   ```bash
   # Windows (Command Prompt)
   set AWS_DEFAULT_REGION=us-east-1

   # Windows (PowerShell)
   $env:AWS_DEFAULT_REGION="us-east-1"

   # Mac/Linux
   export AWS_DEFAULT_REGION=us-east-1
   ```

### For OpenAI (Cloud)

1. **API Key**: Create an API key at [platform.openai.com/api-keys](https://platform.openai.com/api-keys)

2. **Credits**: Add credits to your account at [platform.openai.com/settings/organization/billing/overview](https://platform.openai.com/settings/organization/billing/overview)

3. **Set API Key**: Set your OpenAI API key as an environment variable:

   ```bash
   # Windows (Command Prompt)
   set OPENAI_API_KEY=your_api_key

   # Windows (PowerShell)
   $env:OPENAI_API_KEY="your_api_key"

   # Mac/Linux
   export OPENAI_API_KEY=your_api_key
   ```

4. **Model**: Scripts use `gpt-4o-mini` (cheapest model)

## Installation

```bash
# Windows (Command Prompt or PowerShell)
pip install -r requirements.txt

# Mac/Linux
pip install -r requirements.txt
```

## Running the Examples

### Strands Agent

```bash
# With Ollama
python simple_agent_strands_ollama.py

# With Bedrock
python simple_agent_strands_bedrock.py

# With OpenAI
python simple_agent_strands_openai.py
```

### LangGraph Agent

```bash
# With Ollama
python simple_agent_langgraph_ollama.py

# With Bedrock
python simple_agent_langgraph_bedrock.py

# With OpenAI
python simple_agent_langgraph_openai.py
```

All examples do the same thing - create a simple conversational agent that can answer questions using the LLM's knowledge. No tools or external APIs required!

## What's Next?

In the next posts, we'll add tools to our agents, allowing them to perform calculations, query APIs, and interact with external systems.
