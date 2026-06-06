import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from src.agents.design_agent import DesignAgent


def test_generate_design():

    agent = DesignAgent()

    result = agent.generate_design(
        ["Requirement 1", "Requirement 2"]
    )

    assert len(result) > 0