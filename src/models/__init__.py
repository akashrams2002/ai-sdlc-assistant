# src/models/llm.py

class LLM:
    """
    Future LLM interface.

    OpenAI
    Ollama
    Gemini
    Claude

    will be plugged in here later.
    """

    def generate(self, prompt):
        return "LLM response placeholder"