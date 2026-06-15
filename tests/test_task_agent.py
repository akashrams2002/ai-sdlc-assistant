import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from src.agents.task_agent import TaskAgent


def test_food_delivery_tasks():

    agent = TaskAgent()

    design = [
        "Architecture for Food Delivery"
    ]

    result = agent.generate_tasks(
        design
    )

    assert isinstance(result, list)
    assert len(result) > 0


def test_chat_application_tasks():

    agent = TaskAgent()

    design = [
        "Architecture for Chat Application"
    ]

    result = agent.generate_tasks(
        design
    )

    assert isinstance(result, list)
    assert len(result) > 0