from agent.orchestrator import LogAnalysisAgent

def main():
    print("=" * 60)
    print("🤖 AGENTIC SERVER LOG ANALYSIS SYSTEM")
    print("=" * 60)

    log_path = r"C:\Users\amuth\Downloads\industry_server_access.log"

    agent = LogAnalysisAgent(log_path)
    agent.run()   # ✅ no printing of summary or result

if __name__ == "__main__":
    main()
