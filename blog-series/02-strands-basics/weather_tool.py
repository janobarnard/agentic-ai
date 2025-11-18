"""
Module-Based Tool - Framework Independent

This tool doesn't depend on the Strands SDK and can be used with any framework.

NOTE: This file defines a tool module but is not directly runnable.
      Run tools_module.py to see this tool in action.
"""

TOOL_SPEC = {
    "name": "weather_tool",
    "description": "Get current weather for a city",
    "inputSchema": {
        "json": {
            "type": "object",
            "properties": {
                "city": {
                    "type": "string",
                    "description": "The city name"
                },
                "units": {
                    "type": "string",
                    "enum": ["celsius", "fahrenheit"],
                    "description": "Temperature units"
                }
            },
            "required": ["city"]
        }
    }
}

def weather_tool(tool, **kwargs):
    tool_input = tool["input"]
    city = tool_input.get("city")
    units = tool_input.get("units", "celsius")

    # Your implementation here
    result = f"Weather in {city}: 22°{units[0].upper()}"

    return {
        "toolUseId": tool["toolUseId"],
        "status": "success",
        "content": [{"text": result}]
    }
