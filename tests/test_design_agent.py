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
        "Project Idea: Online Food Delivery App",
        "Users can browse restaurants",
        "Users can place food orders",
        "Users can track deliveries"
    ]

    result = agent.generate_design(requirements)

    assert "Restaurant Management Module" in result
    assert "Order Processing Module" in result
    assert "Delivery Tracking Module" in result
    assert "Payment Module" in result


def test_chat_application_design():

    agent = DesignAgent()

    requirements = [
        "Project Idea: Chat Application",
        "Users can send messages",
        "Users can create chat rooms",
        "Users can view chat history"
    ]

    result = agent.generate_design(requirements)

    assert "Messaging Module" in result
    assert "Chat Room Module" in result
    assert "Notification Module" in result
    assert "Chat History Module" in result