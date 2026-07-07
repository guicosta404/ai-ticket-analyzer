from database import main as run_database_pipeline
from report import generate_report


def main() -> None:
    print("=" * 50)
    print("AI Ticket Analyzer")
    print("=" * 50)

    print("\n1. Executando ETL e carregando dados no SQLite...")
    run_database_pipeline()

    print("\n2. Gerando relatório executivo com IA...")
    generate_report()

    print("\nProcesso concluído com sucesso!")


if __name__ == "__main__":
    main()