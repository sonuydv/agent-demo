
from pathlib import Path

BASE_DIR = Path(__file__).parent

class PromptBuilder:

    def __init__(self):
        print(Path())
        self.system = Path(BASE_DIR / "prompts/system.txt").read_text()

        self.persona = Path(BASE_DIR / "prompts/persona.txt").read_text()

        self.rules = Path(BASE_DIR / "prompts/rules.txt").read_text()

    def build(self,first_name:str, history, message,chat_type):
        history_text = "\n".join(
            [f"{h['role']}: {h['content']}" for h in history]
        )

        prompt = f"""
{self.system}

# PERSONA
{self.persona}

# CHAT HISTORY
{history_text}

# CHAT TYPE - {chat_type or "group"}

# RULES
{self.rules}

# CURRENT MESSAGE
{first_name or "User"}: {message}

Reply as the character.
"""

        return prompt