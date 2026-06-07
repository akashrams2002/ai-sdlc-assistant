from src.agents.requirements_agent import RequirementsAgent
from src.agents.design_agent import DesignAgent
from src.agents.task_agent import TaskAgent
from src.agents.code_agent import CodeAgent


class Orchestrator:

    def __init__(self):
        self.requirements_agent = RequirementsAgent()
        self.design_agent = DesignAgent()
        self.task_agent = TaskAgent()
        self.code_agent = CodeAgent()

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

        code = self.code_agent.generate_code(
            tasks
        )

        return {
            "requirements": requirements,
            "design": design,
            "tasks": tasks,
            "code": code
        }