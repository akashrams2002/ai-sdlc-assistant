from src.models.llm import LLM


class RequirementsAgent:
    """
    Converts a project idea into requirements using AI.
    """

    def __init__(self):
        self.llm = LLM()

    def generate_requirements(self, project_idea):

        prompt = f"""
        Generate 5 software requirements for this project.

        Project Idea:
        {project_idea}

        Return only the requirements as a numbered list.
        """

        response = self.llm.generate(prompt)

        requirements = [
            f"Project Idea: {project_idea}"
        ]

        for line in response.split("\n"):

            line = line.strip()

            if line:
                requirements.append(line)

        return requirements