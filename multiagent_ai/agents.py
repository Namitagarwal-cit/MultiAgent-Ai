from dataclasses import dataclass
from typing import Any, Dict


@dataclass
class AgentResponse:
    role: str
    summary: str
    details: str
    issues: str = ""


class Agent:
    def __init__(self, name: str):
        self.name = name

    def analyze(self, question: str, context: Dict[str, Any]) -> AgentResponse:
        raise NotImplementedError


class Researcher(Agent):
    def __init__(self):
        super().__init__("Researcher")

    def analyze(self, question: str, context: Dict[str, Any]) -> AgentResponse:
        # Placeholder analysis; replace with real retrieval/LLM calls.
        summary = "Collect key concepts, definitions, and evidence relevant to the question."
        details = (
            "1) Identify core terms.\n"
            "2) Gather supporting facts, references, and known approaches.\n"
            "3) Check for edge cases and constraints.\n"
            f"Question processed: {question}"
        )
        return AgentResponse(role=self.name, summary=summary, details=details)


class Analyst(Agent):
    def __init__(self):
        super().__init__("Analyst")

    def analyze(self, question: str, context: Dict[str, Any]) -> AgentResponse:
        researcher_output: AgentResponse = context.get("researcher")
        summary = "Break down requirements and produce intermediate reasoning steps."
        details = (
            f"Received researcher context:\n{researcher_output.details}\n\n"
            "4) Decompose the problem into subproblems.\n"
            "5) Evaluate tradeoffs and method selections.\n"
            f"Interpreting the question: {question}"
        )
        return AgentResponse(role=self.name, summary=summary, details=details)


class Critic(Agent):
    def __init__(self):
        super().__init__("Critic")

    def analyze(self, question: str, context: Dict[str, Any]) -> AgentResponse:
        researcher_output: AgentResponse = context.get("researcher")
        analyst_output: AgentResponse = context.get("analyst")
        summary = "Review reasoning, challenge assumptions, and find gaps."
        details = (
            "6) Validate the Researcher and Analyst conclusions.\n"
            "7) Highlight conflicting or unsupported assertions.\n"
            "8) Propose corrections and additional queries.\n"
        )
        issues = (
            "- Verify that factual claims are accurate.\n"
            "- Check if problem decomposition missed edge cases.\n"
            "- Ensure the synthesis path is logically consistent."
        )
        return AgentResponse(role=self.name, summary=summary, details=details, issues=issues)


class FinalSynthesizer(Agent):
    def __init__(self):
        super().__init__("Final Synthesizer")

    def analyze(self, question: str, context: Dict[str, Any]) -> AgentResponse:
        researcher_output: AgentResponse = context.get("researcher")
        analyst_output: AgentResponse = context.get("analyst")
        critic_output: AgentResponse = context.get("critic")

        summary = "Combine validated insights into a coherent final response."
        details = (
            "9) Integrate evidence, analysis, and criticism.\n"
            "10) Generate a concise answer with next step recommendations.\n\n"
            f"Researcher: {researcher_output.summary}\n"
            f"Analyst: {analyst_output.summary}\n"
            f"Critic: {critic_output.issues}\n"
        )

        final_answer = (
            f"Final response for: '{question}'\n"
            "- Start with research-backed facts and definitions.\n"
            "- Include structured solution steps from the analyst.\n"
            "- Add critic caveats and validation notes.\n"
            "- State final recommendation clearly.\n"
        )

        return AgentResponse(role=self.name, summary=summary, details=details, issues=final_answer)
