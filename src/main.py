from orchestrator.orchestrator import Orchestrator


def main():

    orchestrator = Orchestrator()

    result = orchestrator.execute(
        "AI SDLC Assistant"
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


if __name__ == "__main__":
    main()