from src.models.llm import LLM


class DesignAgent:
    """
    Converts requirements into a high-level design using AI.
    """

    def __init__(self):
        self.llm = LLM()

    def generate_design(self, requirements):

        requirements_text = "\n".join(requirements)

        prompt = f"""
        Based on these software requirements, generate a high-level system design.

        Requirements:
        {requirements_text}

        Return only the architecture components as a numbered list.
        """

        response = self.llm.generate(prompt)

        design = [
            f"Architecture for: {requirements[0]}"
        ]

        for line in response.split("\n"):

            line = line.strip()

            if line:
                design.append(line)

        return design