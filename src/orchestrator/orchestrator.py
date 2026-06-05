from agents.requirements_agent import RequirementsAgent
from agents.design_agent import DesignAgent
from agents.task_agent import TaskAgent


class Orchestrator:

    def __init__(self):
        self.requirements_agent = RequirementsAgent()
        self.design_agent = DesignAgent()
        self.task_agent = TaskAgent()

    def execute(self, project_idea):

        requirements = self.requirements_agent.generate_requirements(
            project_idea
        )

        design = self.design_agent.generate_design(
            requirements
        )

        tasks = self.task_agent.generate_tasks(
            design
        )

        return {
            "requirements": requirements,
            "design": design,
            "tasks": tasks
        }