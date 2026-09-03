class InMemoryChatSession:
    def __init__(self, sys_prompt: str, max_history: int = 10):
        self.sys_prompt = sys_prompt
        self.max_history = max_history
        self.history: list[dict] = []

    def add_message(self, role:str, content: str):
        self.history.append({"role": role, "content": content})
        if len(self.history) > self.max_history:
            self.history.pop(0)

    def get_message(self):
        system = [{"role": "system", "content": self.sys_prompt}]
        return system + self.history 


# Create memory with a limit of 4 recent messages:
memory = InMemoryChatSession(
    sys_prompt="You are a senior customer support agent.",
    max_history=4
)

# Simulate 3 turns of back-and-forth conversation (6 messages total):
memory.add_message("user", "Hello, I placed order #101.")
memory.add_message("assistant", "I see order #101. How can I help?")

memory.add_message("user", "I want to change my shipping address.")
memory.add_message("assistant", "Sure, what is the new address?")

memory.add_message("user", "742 Evergreen Terrace.")
memory.add_message("assistant", "Address updated!")

# Inspect what gets sent to the LLM:
payload = memory.get_message()
print(f"Total messages in payload: {len(payload)}")
for msg in payload:
    print(f"[{msg['role'].upper()}]: {msg['content']}")
