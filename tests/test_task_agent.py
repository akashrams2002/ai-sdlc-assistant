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
        "Architecture for: Project Idea: Online Food Delivery App",
        "User Interface Layer",
        "Restaurant Management Module",
        "Order Processing Module",
        "Delivery Tracking Module",
        "Payment Module",
        "Database Layer"
    ]

    result = agent.generate_tasks(design)

    assert "Implement Restaurant Management Module" in result
    assert "Implement Order Processing Module" in result
    assert "Implement Delivery Tracking Module" in result
    assert "Implement Payment Module" in result


def test_chat_application_tasks():

    agent = TaskAgent()

    design = [
        "Architecture for: Project Idea: Chat Application",
        "User Interface Layer",
        "Messaging Module",
        "Chat Room Module",
        "Notification Module",
        "Chat History Module",
        "Database Layer"
    ]

    result = agent.generate_tasks(design)

    assert "Implement Messaging Module" in result
    assert "Implement Chat Room Module" in result
    assert "Implement Notification Module" in result
    assert "Implement Chat History Module" in result