from dotenv import load_dotenv
from openai import OpenAI
import json
import requests
import os

# --------------------------------------------------
# Load Environment Variables
# --------------------------------------------------
load_dotenv()

# --------------------------------------------------
# Ollama Client
# --------------------------------------------------
client = OpenAI(
    base_url="http://localhost:11434/v1/",
    api_key="ollama"
)

# --------------------------------------------------
# Tools
# --------------------------------------------------
def get_weather(city: str):
    try:
        url = f"https://wttr.in/{city}?format=%C+%t"
        response = requests.get(url, timeout=10)

        if response.status_code == 200:
            return f"The weather in {city} is {response.text}"

        return "Unable to fetch weather data."

    except Exception as e:
        return f"Weather Error: {str(e)}"


def run_command(cmd: str):
    try:
        result = os.popen(cmd).read()
        return result if result else "Command executed."
    except Exception as e:
        return f"Command Error: {str(e)}"


def get_stock_price(symbol: str):
    try:
        url = (
            f"https://www.alphavantage.co/query?"
            f"function=GLOBAL_QUOTE&symbol={symbol}"
            f"&apikey=HZOYTONOYXAP32VO"
        )

        response = requests.get(url, timeout=10)
        data = response.json()

        price = data["Global Quote"]["05. price"]

        return f"The current stock price of {symbol.upper()} is ${price}"

    except Exception:
        return f"Could not fetch stock price for {symbol}"


available_tools = {
    "get_weather": get_weather,
    "run_command": run_command,
    "get_stock_price": get_stock_price
}
# --------------------------------------------------
# System Prompt
# --------------------------------------------------
SYSTEM_PROMPT = """
You are a helpful AI Assistant.

You operate in four steps:

1. plan
2. action
3. observe
4. output

Rules:
- Always return valid JSON.
- Perform one step at a time.
- Use available tools whenever needed.

JSON Format:

{
    "step":"plan/action/output",
    "content":"text",
    "function":"tool_name",
    "input":"tool_input"
}

Available Tools:

1. get_weather(city)
   Returns weather information.

2. get_stock_price(symbol)
   Returns stock price.

3. run_command(command)
   Executes a system command.
"""

# --------------------------------------------------
# Main Agent Function
# --------------------------------------------------
def run_agent(query):

    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        },
        {
            "role": "user",
            "content": query
        }
    ]

    max_iterations = 10

    for _ in range(max_iterations):

        response = client.chat.completions.create(
            model="qwen2.5-coder:3b",
            response_format={"type": "json_object"},
            messages=messages
        )

        assistant_message = response.choices[0].message.content
        print(f"\nIteration {_+1}")
        print(assistant_message)
        print("-" * 50)             
        messages.append(
            {
                "role": "assistant",
                "content": assistant_message
            }
        )

        try:
            parsed_response = json.loads(assistant_message)

        except Exception:
            return assistant_message

        step = parsed_response.get("step")

        # ---------------- PLAN ----------------
        if step == "plan":
            continue

        # ---------------- ACTION ----------------
        elif step == "action":

            tool_name = parsed_response.get("function")
            tool_input = parsed_response.get("input")

            if tool_name not in available_tools:
                return f"Unknown tool: {tool_name}"

            tool_output = available_tools[tool_name](tool_input)

            messages.append(
                {
                    "role": "user",
                    "content": json.dumps(
                        {
                            "step": "observe",
                            "output": tool_output
                        }
                    )
                }
            )

            continue

        # ---------------- OUTPUT ----------------
        elif step == "output":
            return parsed_response.get("content")

    return "Agent exceeded maximum iterations."