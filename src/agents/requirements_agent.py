class RequirementsAgent:
    """
    Converts a project idea into requirements.
    """

    def generate_requirements(self, project_idea):

        requirements = [
            f"Project Idea: {project_idea}"
        ]

        project = project_idea.lower()

        if "food" in project:

            requirements.extend([
                "Users can browse restaurants",
                "Users can place food orders",
                "Users can track deliveries",
                "Restaurant owners can manage menus"
            ])

        elif "ecommerce" in project or "shopping" in project:

            requirements.extend([
                "Users can browse products",
                "Users can add products to cart",
                "Users can place orders",
                "Admins can manage inventory"
            ])

        elif "chat" in project:

            requirements.extend([
                "Users can send messages",
                "Users can create chat rooms",
                "Users can view chat history",
                "Users receive notifications"
            ])

        else:

            requirements.extend([
                "Users can interact with the system",
                "System processes requests",
                "System stores data",
                "Admins can manage the application"
            ])

        return requirements