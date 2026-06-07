from src.orchestrator.orchestrator import Orchestrator

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


if __name__ == "__main__":
    main()