class CodeAgent:
    """
    Generates starter code from tasks.
    """

    def generate_code(self, tasks):

        code = []

        for task in tasks:

            if not task.startswith("Implement"):
                continue

            module_name = (
                task.replace("Implement ", "")
                .replace(" Module", "")
                .replace(" ", "")
            )

            class_code = (
                f"class {module_name}:\n"
                f"    def execute(self):\n"
                f"        pass"
            )

            code.append(class_code)

        return code