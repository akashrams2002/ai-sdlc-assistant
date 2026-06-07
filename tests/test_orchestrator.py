import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from src.orchestrator.orchestrator import Orchestrator


def test_chat_application_pipeline():

    orchestrator = Orchestrator()

    result = orchestrator.execute(
        "Chat Application"
    )

    assert "Users can send messages" in result["requirements"]

    assert "Messaging Module" in result["design"]

    assert "Implement Messaging Module" in result["tasks"]

    generated_code = "\n".join(result["code"])

    assert "class Messaging" in generated_code


def test_food_delivery_pipeline():

    orchestrator = Orchestrator()

    result = orchestrator.execute(
        "Online Food Delivery App"
    )

    assert "Users can browse restaurants" in result["requirements"]

    assert "Restaurant Management Module" in result["design"]

    assert "Implement Restaurant Management Module" in result["tasks"]

    generated_code = "\n".join(result["code"])

    assert "class RestaurantManagement" in generated_code