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

    assert "Users can browse restaurants" in result
    assert "Users can place food orders" in result
    assert "Users can track deliveries" in result


def test_chat_application_requirements():

    agent = RequirementsAgent()

    result = agent.generate_requirements(
        "Chat Application"
    )

    assert "Users can send messages" in result
    assert "Users can create chat rooms" in result
    assert "Users receive notifications" in result