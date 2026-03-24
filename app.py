import argparse
from multiagent_ai.orchestrator import MultiAgentOrchestrator


def main():
    parser = argparse.ArgumentParser(description="Multi-Agent AI Debate System")
    parser.add_argument("question", type=str, nargs="+", help="User question to analyze")
    args = parser.parse_args()

    question = " ".join(args.question)
    orchestrator = MultiAgentOrchestrator()

    result = orchestrator.debate(question)
    report = orchestrator.format_report(result)

    print(report)


if __name__ == "__main__":
    main()
