from pathlib import Path
import pandas as pd


DATA_PATH = Path("data/tickets.csv")


def load_data(path: Path = DATA_PATH) -> pd.DataFrame:
    return pd.read_csv(path)


def inspect_data(df: pd.DataFrame) -> None:
    print("\nPrimeiras linhas:")
    print(df.head())

    print("\nInformações:")
    print(df.info())

    print("\nValores nulos:")
    print(df.isnull().sum())

    print("\nDuplicatas:")
    print(df.duplicated().sum())


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df["cliente"] = df["cliente"].str.strip()
    df["categoria"] = df["categoria"].str.strip().str.title()
    df["categoria"] = df["categoria"].replace({
    "Api": "API"
})
    df["prioridade"] = df["prioridade"].str.strip().str.title()
    df["status"] = df["status"].str.strip().str.title()

    df["descricao"] = df["descricao"].fillna("Descrição não informada")
    df["data_abertura"] = pd.to_datetime(df["data_abertura"])

    df = df.drop_duplicates()

    return df


def main():
    df = load_data()
    inspect_data(df)

    df_clean = clean_data(df)

    print("\nDados limpos:")
    print(df_clean.head())

    print("\nCategorias padronizadas:")
    print(df_clean["categoria"].unique())

    print("\nPrioridades padronizadas:")
    print(df_clean["prioridade"].unique())

    print("\nStatus padronizados:")
    print(df_clean["status"].unique())


if __name__ == "__main__":
    main()