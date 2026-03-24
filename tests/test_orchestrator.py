import pytest
from multiagent_ai.orchestrator import MultiAgentOrchestrator


def test_multiagent_debate_basics():
    orchestrator = MultiAgentOrchestrator()
    question = "How can we build a multi-agent debate architecture?"
    output = orchestrator.debate(question)

    assert "researcher" in output
    assert "analyst" in output
    assert "critic" in output
    assert "final" in output

    assert output["researcher"].role == "Researcher"
    assert output["final"].role == "Final Synthesizer"
    assert "multi-agent" in output["final"].issues.lower() or output["final"].issues
