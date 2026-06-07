from src.orchestrator.orchestrator import Orchestrator


def save_to_file(filename, title, items):

    with open(filename, "w", encoding="utf-8") as file:

        file.write(f"# {title}\n\n")

        for item in items:
            file.write(f"- {item}\n")


def main():

    project_idea = input(
        "Enter Project Idea: "
    )

    orchestrator = Orchestrator()

    result = orchestrator.execute(
        project_idea
    )

    print("\nGenerated Requirements:\n")
    for req in result["requirements"]:
        print("-", req)

    print("\nGenerated Design:\n")
    for item in result["design"]:
        print("-", item)

    print("\nGenerated Tasks:\n")
    for task in result["tasks"]:
        print("-", task)

    print("\nGenerated Code:\n")
    for item in result["code"]:
        print(item)
        print()

    # Save outputs to files
    save_to_file(
        "docs/requirements.md",
        "Requirements",
        result["requirements"]
    )

    save_to_file(
        "docs/design.md",
        "Design",
        result["design"]
    )

    save_to_file(
        "docs/tasks.md",
        "Tasks",
        result["tasks"]
    )

    print("\nDocumentation saved to docs folder.")


if __name__ == "__main__":
    main()