from pathlib import Path
import sqlite3

import pandas as pd # type: ignore


DB_PATH = Path("database/tickets.db")

# Conecta com o banco
def create_connection(db_path: Path = DB_PATH):
    return sqlite3.connect(db_path)


def get_total_tickets() -> pd.DataFrame:
    query = """
    SELECT COUNT(*) AS total_chamados
    FROM tickets;
    """

    with create_connection() as conn:
        return pd.read_sql_query(query, conn)


def get_tickets_by_category() -> pd.DataFrame:
    query = """
    SELECT
        categoria,
        COUNT(*) AS total
    FROM tickets
    GROUP BY categoria
    ORDER BY total DESC;
    """

    with create_connection() as conn:
        return pd.read_sql_query(query, conn)


def get_tickets_by_status() -> pd.DataFrame:
    query = """
    SELECT status,
        COUNT(*) AS total
    FROM tickets
    GROUP BY status
    ORDER BY total DESC;    
    """
    with create_connection() as conn:
        return pd.read_sql_query(query, conn)


def get_high_priority_tickets() -> pd.DataFrame:
    query = """
    SELECT *
    FROM tickets
    WHERE prioridade = 'Alta'
    ORDER BY data_abertura DESC;
    """
    with create_connection() as conn:
        return pd.read_sql_query(query, conn)


def get_oldest_tickets(limit: int = 10) -> pd.DataFrame:
    query = """
    SELECT *
    FROM tickets
    ORDER BY data_abertura ASC
    LIMIT ?;
    """
    with create_connection() as conn:
        return pd.read_sql_query(query, conn, params=(limit,))

def main():
    print("\n=== Total de chamados ===")
    print(get_total_tickets())

    print("\n=== Chamados por categoria ===")
    print(get_tickets_by_category())

    print("\n=== Chamados por status ===")
    print(get_tickets_by_status())

    print("\n=== Chamados de alta prioridade ===")
    print(get_high_priority_tickets())

    print("\n=== Chamados mais antigos ===")
    print(get_oldest_tickets())


if __name__ == "__main__":
    main()