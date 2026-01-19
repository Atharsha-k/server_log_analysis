import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

from tools.file_finder import find_log_file
from tools.log_parser import parse_logs
from tools.error_filter import filter_errors
from tools.error_clusterer import cluster_errors
from tools.frequency_analyzer import analyze_frequency
from tools.impact_assessor import assess_impact
from tools.report_generator import generate_report


load_dotenv()


class LogAnalysisAgent:
    MAX_CHARS = 3500

    def __init__(self, log_path: str):
        print("🔍 Initializing agentic AI system")

        self.log_path = log_path
        self.memory = {}
        self.goal = "Analyze server logs and generate executive insights"

        self.llm = ChatGroq(
            model="llama-3.1-8b-instant",
            temperature=0
        )

    def decide_next_action(self):
        if "log_file" not in self.memory:
            return "FIND_LOG"
        if "parsed_logs" not in self.memory:
            return "PARSE"
        if "errors" not in self.memory:
            return "FILTER"
        if "clusters" not in self.memory:
            return "CLUSTER"
        if "frequency" not in self.memory:
            return "FREQUENCY"
        if "impact" not in self.memory:
            return "IMPACT"
        if "summary" not in self.memory:
            return "SUMMARY"
        return "REPORT"

    def _safe_text(self, text: str):
        return text[: self.MAX_CHARS]

    def _compact_for_llm(self):
        clusters = self.memory["clusters"]
        frequency = self.memory["frequency"]
        impact = self.memory["impact"]

        cluster_summary = [
            f"Cluster {cid}: {len(items)} occurrences"
            for cid, items in list(clusters.items())[:3]
        ]

        freq_summary = []
        if isinstance(frequency, dict):
            for k, v in list(frequency.items())[:5]:
                freq_summary.append(f"{k}: {v}")
        else:
            for item in frequency[:5]:
                freq_summary.append(str(item))

        return {
            "cluster_summary": "\n".join(cluster_summary),
            "frequency_summary": "\n".join(freq_summary),
            "impact_summary": str(impact)
        }

    def run(self):
        print("🎯 Agent started")

        while True:
            action = self.decide_next_action()

            if action == "FIND_LOG":
                print("📂 Log file located")
                self.memory["log_file"] = find_log_file(self.log_path)

            elif action == "PARSE":
                print("🔍 Log parsing completed")
                self.memory["parsed_logs"] = parse_logs(self.memory["log_file"])

            elif action == "FILTER":
                print("🚨 Error extraction completed")
                self.memory["errors"] = filter_errors(self.memory["parsed_logs"])

            elif action == "CLUSTER":
                print("🧩 Error clustering completed")
                self.memory["clusters"] = cluster_errors(self.memory["errors"])

            elif action == "FREQUENCY":
                print("⏱ Frequency analysis completed")
                self.memory["frequency"] = analyze_frequency(self.memory["clusters"])

            elif action == "IMPACT":
                print("⚠ Impact assessment completed")
                self.memory["impact"] = assess_impact(self.memory)

            elif action == "SUMMARY":
                print("🧠 Executive summary generated")

                compact = self._compact_for_llm()
                prompt = f"""
You are a senior Site Reliability Engineer.

Error overview:
{compact['cluster_summary']}

Frequency patterns:
{compact['frequency_summary']}

Impact assessment:
{compact['impact_summary']}
"""

                try:
                    self.memory["summary"] = self.llm.invoke(
                        self._safe_text(prompt)
                    ).content
                except Exception:
                    self.memory["summary"] = "Summary unavailable."

            elif action == "REPORT":
                print("📊 Report generated successfully")
                report_path = generate_report(self.memory)
                print(f"📄 Report generated: {report_path}")
                print("✅ Agent execution completed")
                return
