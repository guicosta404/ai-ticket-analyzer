from datetime import datetime
from pathlib import Path

from agent import analyze_tickets


REPORT_PATH = Path("reports/relatorio_executivo.md")


def generate_report() -> None:
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)

    analysis = analyze_tickets()
    generated_at = datetime.now().strftime("%d/%m/%Y %H:%M")

    content = f"""# Relatório Executivo — AI Ticket Analyzer

**Gerado em:** {generated_at}

---

{analysis}
"""

    REPORT_PATH.write_text(content, encoding="utf-8")

    print(f"Relatório gerado com sucesso em: {REPORT_PATH}")


if __name__ == "__main__":
    generate_report()