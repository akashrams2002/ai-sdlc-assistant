class TaskAgent:
    """
    Converts design into development tasks.
    """

    def generate_tasks(self, design):

        tasks = []

        architecture_name = design[0]

        tasks.append(
            f"Review {architecture_name}"
        )

        for component in design[1:]:

            if "Layer" in component:
                continue

            tasks.append(
                f"Implement {component}"
            )

        tasks.extend([
            "Write unit tests",
            "Deploy application"
        ])

        return tasks