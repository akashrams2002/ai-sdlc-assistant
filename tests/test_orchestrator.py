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

    assert "requirements" in result
    assert "design" in result
    assert "tasks" in result
    assert "code" in result

    assert len(result["requirements"]) > 0
    assert len(result["design"]) > 0
    assert len(result["tasks"]) > 0


def test_food_delivery_pipeline():

    orchestrator = Orchestrator()

    result = orchestrator.execute(
        "Online Food Delivery App"
    )

    assert "requirements" in result
    assert "design" in result
    assert "tasks" in result
    assert "code" in result

    assert len(result["requirements"]) > 0
    assert len(result["design"]) > 0
    assert len(result["tasks"]) > 0