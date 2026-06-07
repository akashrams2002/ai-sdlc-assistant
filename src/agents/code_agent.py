import re


class CodeAgent:
    """
    Generates starter code from tasks.
    """

    def generate_code(self, tasks):

        code = []

        for task in tasks:

            if not task.startswith("Implement"):
                continue

            module_name = task.replace(
                "Implement ",
                ""
            )

            # Remove numbering like "1."
            module_name = re.sub(
                r"^\d+\.\s*",
                "",
                module_name
            )

            # Remove special characters
            module_name = re.sub(
                r"[^a-zA-Z0-9 ]",
                "",
                module_name
            )

            # Convert to PascalCase
            module_name = "".join(
                word.capitalize()
                for word in module_name.split()
            )

            class_code = (
                f"class {module_name}:\n"
                f"    def execute(self):\n"
                f"        pass"
            )

            code.append(class_code)

        return code