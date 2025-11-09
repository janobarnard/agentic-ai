# Blog Series: Building Agentic AI Applications

Code examples accompanying the [Agentic AI blog series](https://janobarnard.blog) by Jano Barnard.

## Series Overview

This directory contains hands-on code for each blog post in the series. Each folder corresponds to a blog post with practical, runnable examples.

## Published Posts

### [01-intro - Introduction to Agentic AI & Frameworks](./01-intro)

**Blog Post**: [Introduction to Agentic AI & Frameworks](https://janobarnard.blog)  
**Topics**: LLMs, agent loop, Strands vs LangGraph, framework ecosystem  
**Code**: Simple conversational agents with Ollama, Bedrock, and OpenAI

## Coming Soon

- Tools and function calling
- Deploying to Amazon Bedrock AgentCore
- RAG knowledge bases
- Custom MCP tools
- Multi-agent architectures
- ...and more as the series evolves!

## Getting Started

Each directory contains:

- `README.md` - Setup instructions and prerequisites
- `requirements.txt` - Python dependencies
- Example code files for different model providers

### Prerequisites

- Python 3.10 or later
- VS Code (recommended) or your preferred IDE
- Choose at least one model provider:
  - **Ollama** (free, local)
  - **Amazon Bedrock** (cloud, AWS account required)
  - **OpenAI** (cloud, API key + credits required)

### Setup

```bash
cd blog-series/01-intro
pip install -r requirements.txt
python simple_agent_strands_ollama.py  # or any other example
```

## Tips

- Start with post 01 and work through the series
- Each post builds on previous concepts
- Code is kept minimal for learning
- Check the blog posts for detailed explanations
