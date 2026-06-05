from agents.requirements_agent import RequirementsAgent
from agents.design_agent import DesignAgent
from agents.task_agent import TaskAgent


def main():

    requirements_agent = RequirementsAgent()
    design_agent = DesignAgent()
    task_agent = TaskAgent()

    project_idea = "AI SDLC Assistant"

    requirements = requirements_agent.generate_requirements(project_idea)

    design = design_agent.generate_design(requirements)

    tasks = task_agent.generate_tasks(design)

    print("\nGenerated Requirements:\n")
    for req in requirements:
        print("-", req)

    print("\nGenerated Design:\n")
    for item in design:
        print("-", item)

    print("\nGenerated Tasks:\n")
    for task in tasks:
        print("-", task)


if __name__ == "__main__":
    main()