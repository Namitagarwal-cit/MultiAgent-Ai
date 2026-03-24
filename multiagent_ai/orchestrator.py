from typing import Dict
from .agents import AgentResponse, Researcher, Analyst, Critic, FinalSynthesizer


class MultiAgentOrchestrator:
    def __init__(self):
        self.researcher = Researcher()
        self.analyst = Analyst()
        self.critic = Critic()
        self.synthesizer = FinalSynthesizer()

    def debate(self, question: str) -> Dict[str, AgentResponse]:
        context = {}

        researcher_output = self.researcher.analyze(question, context)
        context["researcher"] = researcher_output

        analyst_output = self.analyst.analyze(question, context)
        context["analyst"] = analyst_output

        critic_output = self.critic.analyze(question, context)
        context["critic"] = critic_output

        synthesizer_output = self.synthesizer.analyze(question, context)

        return {
            "researcher": researcher_output,
            "analyst": analyst_output,
            "critic": critic_output,
            "final": synthesizer_output,
        }

    def format_report(self, debate_results: Dict[str, AgentResponse]) -> str:
        lines = ["--- Multi-Agent Debate Report ---"]
        for role, result in debate_results.items():
            lines.append(f"\\n[{result.role}] Summary:")
            lines.append(result.summary)
            lines.append("Details:")
            lines.append(result.details)
            if result.issues:
                lines.append("Issues / Final Answer:")
                lines.append(result.issues)

        return "\n".join(lines)
