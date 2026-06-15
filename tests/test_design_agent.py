import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from src.agents.design_agent import DesignAgent


def test_food_delivery_design():

    agent = DesignAgent()

    requirements = [
        "Project Idea: Online Food Delivery App"
    ]

    result = agent.generate_design(
        requirements
    )

    assert isinstance(result, list)
    assert len(result) >= 3


def test_chat_application_design():

    agent = DesignAgent()

    requirements = [
        "Project Idea: Chat Application"
    ]

    result = agent.generate_design(
        requirements
    )

    assert isinstance(result, list)
    assert len(result) >= 3