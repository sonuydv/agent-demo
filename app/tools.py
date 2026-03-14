

def calculator(expression:str):
    try:
        result = eval(expression)
        return str(result)
    except Exception as e:
        return f"error: {e}"


def write_log(message:str):
    with open("log.txt","a") as f:
        f.write(message+"\n")


TOOLS = {
    "calculator" : {
        "func":calculator,
        "description":"Evaluate a mathematical expression"
    },
    "write_log" : {
        "func": write_log,
        "description": "Write log message to system"
    }
}

def render_tools():
    tool_descriptions = []

    for name,tool in TOOLS.items():
        tool_descriptions.append(
            f"{name}: {tool['description']}"
        )

    return "\n".join(tool_descriptions)