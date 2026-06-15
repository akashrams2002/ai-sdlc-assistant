import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from src.agents.requirements_agent import RequirementsAgent


def test_food_delivery_requirements():

    agent = RequirementsAgent()

    result = agent.generate_requirements(
        "Online Food Delivery App"
    )

    assert isinstance(result, list)
    assert len(result) >= 3


def test_chat_application_requirements():

    agent = RequirementsAgent()

    result = agent.generate_requirements(
        "Chat Application"
    )

    assert isinstance(result, list)
    assert len(result) >= 3