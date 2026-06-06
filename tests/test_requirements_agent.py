import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from src.agents.requirements_agent import RequirementsAgent


def test_generate_requirements():

    agent = RequirementsAgent()

    result = agent.generate_requirements(
        "AI SDLC Assistant"
    )

    assert len(result) > 0