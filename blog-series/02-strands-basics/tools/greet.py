"""Sample tool for hot reload demonstration"""

from strands import tool


@tool
def greet(name: str) -> str:
    """Greet someone by name"""
    return f"Hello, {name}! Welcome to hot reloading."
