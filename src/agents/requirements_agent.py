class RequirementsAgent:
    """
    Converts a project idea into requirements.
    """

    def generate_requirements(self, project_idea):
        requirements = [
            f"Project Idea: {project_idea}",
            "User can provide a project idea",
            "System generates requirements",
            "Requirements are stored in a document"
        ]

        return requirements