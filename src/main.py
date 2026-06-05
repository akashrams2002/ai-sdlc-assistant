from agents.requirements_agent import RequirementsAgent


def main():
    agent = RequirementsAgent()

    project_idea = "AI SDLC Assistant"

    requirements = agent.generate_requirements(project_idea)

    print("\nGenerated Requirements:\n")

    for req in requirements:
        print("-", req)


if __name__ == "__main__":
    main()