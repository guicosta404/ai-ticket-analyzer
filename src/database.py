from pathlib import Path
import sqlite3

import pandas as pd # type: ignore

from etl import clean_data, load_data


DB_PATH = Path("database/tickets.db")


def create_connection(db_path: Path = DB_PATH):
    db_path.parent.mkdir(parents=True, exist_ok=True)
    return sqlite3.connect(db_path)


def save_tickets_to_db(df: pd.DataFrame, table_name: str = "tickets") -> None:
    with create_connection() as conn:
        df.to_sql(table_name, conn, if_exists="replace", index=False)


def main():
    raw_df = load_data()
    clean_df = clean_data(raw_df)

    save_tickets_to_db(clean_df)

    print("Dados salvos com sucesso no banco SQLite.")
    print(f"Total de registros: {len(clean_df)}")


if __name__ == "__main__":
    main()