class DesignAgent:
    """
    Converts requirements into a high-level design.
    """

    def generate_design(self, requirements):

        project_name = requirements[0]

        design = [
            f"Architecture for: {project_name}"
        ]

        requirements_text = " ".join(requirements).lower()

        if "restaurant" in requirements_text:

            design.extend([
                "User Interface Layer",
                "Restaurant Management Module",
                "Order Processing Module",
                "Delivery Tracking Module",
                "Payment Module",
                "Database Layer"
            ])

        elif "message" in requirements_text:

            design.extend([
                "User Interface Layer",
                "Messaging Module",
                "Chat Room Module",
                "Notification Module",
                "Chat History Module",
                "Database Layer"
            ])

        else:

            design.extend([
                "User Interface Layer",
                "Business Logic Layer",
                "Service Layer",
                "Database Layer"
            ])

        return design