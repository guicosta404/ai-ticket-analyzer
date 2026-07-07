import os

from dotenv import load_dotenv # type: ignore
from openai import OpenAI # type: ignore

from queries import (
    get_total_tickets,
    get_tickets_by_category,
    get_tickets_by_status,
    get_high_priority_tickets,
    get_oldest_tickets,
)


load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1",
)


def dataframe_to_text(title, df):
    return f"\n## {title}\n{df.to_string(index=False)}"


def build_context():
    context = ""
    context += dataframe_to_text("Total de chamados", get_total_tickets())
    context += dataframe_to_text("Chamados por categoria", get_tickets_by_category())
    context += dataframe_to_text("Chamados por status", get_tickets_by_status())
    context += dataframe_to_text("Chamados de prioridade alta", get_high_priority_tickets().head(10))
    context += dataframe_to_text("Chamados mais antigos", get_oldest_tickets())
    return context


def analyze_tickets():
    context = build_context()

    prompt = f"""
Você é um analista de automações e IA.

Analise os dados abaixo e gere um relatório executivo com:

1. Resumo geral
2. Principais problemas identificados
3. Possíveis causas
4. Recomendações de automação
5. Como um agente de IA poderia ajudar nesse cenário

Dados:
{context}
"""

    response = client.responses.create(
        model="llama-3.3-70b-versatile",
        input=prompt,
    )

    return response.output_text


def main():
    print(analyze_tickets())


if __name__ == "__main__":
    main()