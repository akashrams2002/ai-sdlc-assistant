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

    assert isinstance(result, list)
    assert len(result) > 0
    assert len(generated_code) > 0

    # AI-generated code should contain at least one class
    assert "class" in generated_code


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

    assert isinstance(result, list)
    assert len(result) > 0
    assert len(generated_code) > 0

    # AI-generated code should contain at least one class
    assert "class" in generated_code