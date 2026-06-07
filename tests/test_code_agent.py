import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from src.agents.code_agent import CodeAgent


def test_food_delivery_code():

    agent = CodeAgent()

    tasks = [
        "Implement Restaurant Management Module",
        "Implement Order Processing Module",
        "Implement Delivery Tracking Module",
        "Implement Payment Module"
    ]

    result = agent.generate_code(tasks)

    generated_code = "\n".join(result)

    assert "class RestaurantManagement" in generated_code
    assert "class OrderProcessing" in generated_code
    assert "class DeliveryTracking" in generated_code
    assert "class Payment" in generated_code


def test_chat_application_code():

    agent = CodeAgent()

    tasks = [
        "Implement Messaging Module",
        "Implement Chat Room Module",
        "Implement Notification Module",
        "Implement Chat History Module"
    ]

    result = agent.generate_code(tasks)

    generated_code = "\n".join(result)

    assert "class Messaging" in generated_code
    assert "class ChatRoom" in generated_code
    assert "class Notification" in generated_code
    assert "class ChatHistory" in generated_code