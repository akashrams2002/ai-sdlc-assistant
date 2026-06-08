from src.models.llm import LLM


class CodeAgent:
    """
    Generates starter code using AI.
    """

    def __init__(self):
        self.llm = LLM()

    def generate_code(self, tasks):

        tasks_text = "\n".join(tasks)

        prompt = f"""
        Based on these software development tasks,
        generate Python starter code.

        Tasks:
        {tasks_text}

        Generate simple Python classes and methods.

        Return only code.
        """

        response = self.llm.generate(
            prompt
        )

        return [response]
