from src.models.llm import LLM


class TaskAgent:
    """
    Converts design into development tasks using AI.
    """

    def __init__(self):
        self.llm = LLM()

    def generate_tasks(self, design):

        design_text = "\n".join(design)

        prompt = f"""
        Based on this software architecture, generate a list of software development tasks.

        Architecture:
        {design_text}

        Return only the tasks as a numbered list.
        """

        response = self.llm.generate(prompt)

        tasks = [
            f"Review {design[0]}"
        ]

        for line in response.split("\n"):

            line = line.strip()

            if line:
                tasks.append(line)

        tasks.extend([
            "Write unit tests",
            "Deploy application"
        ])

        return tasks