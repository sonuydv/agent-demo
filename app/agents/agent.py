from llm import ask_llm
from tools import TOOLS,render_tools
import json

SYSTEM_PROMPT = f"""
You are an AI agent that can use tools.

Available tools:
{render_tools()}

For each task you need to structure your answer strictly in the following instruction format with specifying the matching tools.
Format should be followed strictly.

Thinking: reasoning about the task
Action: tool name
Action Input: input for tool

While generating instruction format , don't append any punctuation or extra characters.

"""
LOGGING_TASK = """
Logging Task : Log the user task along with instruction format
"""

def run_agent(user_input:str):
    prompt = SYSTEM_PROMPT + "\n User Task: " + user_input +"\n"+LOGGING_TASK
    response = ask_llm(prompt)
    print(f"\nLLM RESPONSE: #############################")
    print(response)

    if "Action:" in response:
        lines = response.split("\n")

        tool_name = None
        tool_input = None

        for line in lines:
            if line.startswith("Action:"):
                tool_name = line.replace("Action:","").strip()
            if line.startswith("Action Input:"):
                tool_input = line.replace("Action Input:","").strip()

        if tool_name in TOOLS:
            tool_func = TOOLS[tool_name]["func"]
            result = tool_func(tool_input)
            return f"Tool Result: {result}"

    return response
