from agents.requirements_agent import RequirementsAgent
from agents.design_agent import DesignAgent


def main():

    requirements_agent = RequirementsAgent()
    design_agent = DesignAgent()

    project_idea = "AI SDLC Assistant"

    requirements = requirements_agent.generate_requirements(project_idea)

    design = design_agent.generate_design(requirements)

    print("\nGenerated Requirements:\n")

    for req in requirements:
        print("-", req)

    print("\nGenerated Design:\n")

    for item in design:
        print("-", item)


if __name__ == "__main__":
    main()