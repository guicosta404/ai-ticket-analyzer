# AI Ticket Analyzer

Projeto desenvolvido para simular um pipeline completo de análise de chamados utilizando **Python, SQL e Inteligência Artificial**.

O objetivo é demonstrar um fluxo semelhante ao encontrado em empresas de tecnologia que trabalham com automação de processos e análise de dados, passando pelas etapas de ETL, armazenamento em banco de dados, consultas SQL e geração de relatórios executivos com apoio de um LLM.

---

# Tecnologias

* Python 3.12
* Pandas
* SQLite
* SQL
* Groq API (LLM)
* python-dotenv
* Requests
* Git / GitHub

---

# Funcionalidades

* Geração de base de dados fictícia de chamados.
* Pipeline de ETL para limpeza e padronização dos dados.
* Armazenamento em banco SQLite.
* Consultas SQL para geração de indicadores.
* Integração com um modelo de linguagem (LLM) via API da Groq.
* Geração automática de relatório executivo em Markdown.

---

# Estrutura do Projeto

```text
ai-ticket-analyzer/

├── data/
│   └── tickets.csv
│
├── database/
│   └── tickets.db
│
├── reports/
│   └── relatorio_executivo.md
│
├── src/
│   ├── etl.py
│   ├── database.py
│   ├── queries.py
│   ├── agent.py
│   ├── report.py
│   └── main.py
│
├── .env.example
├── requirements.txt
├── README.md
```

---

# Fluxo da Aplicação

```text
CSV
    │
    ▼
ETL (Pandas)
    │
    ▼
Limpeza e Padronização
    │
    ▼
SQLite
    │
    ▼
Consultas SQL
    │
    ▼
LLM (Groq)
    │
    ▼
Relatório Executivo
```

---

# Como executar

## 1. Clonar o repositório

```bash
git clone <url-do-repositorio>
cd ai-ticket-analyzer
```

## 2. Criar ambiente virtual

```bash
python -m venv .venv
```

## 3. Ativar ambiente

Windows

```bash
.venv\Scripts\activate
```

Linux/macOS

```bash
source .venv/bin/activate
```

## 4. Instalar dependências

```bash
pip install -r requirements.txt
```

## 5. Configurar variável de ambiente

Criar um arquivo `.env`:

```text
GROQ_API_KEY=sua_chave_aqui
```

## 6. Executar

```bash
python src/main.py
```

---

# Exemplo de saída

O projeto gera automaticamente:

* Banco SQLite contendo os chamados tratados.
* Consultas SQL para análise dos dados.
* Relatório executivo em Markdown contendo:

  * resumo dos chamados;
  * principais problemas;
  * possíveis causas;
  * sugestões de automação;
  * oportunidades de utilização de IA.

---

# Objetivos de aprendizado

Este projeto foi desenvolvido para consolidar conhecimentos em:

* Engenharia de Dados
* ETL
* SQL
* Modelagem de dados
* Integração com APIs
* Inteligência Artificial Generativa
* Prompt Engineering
* Organização de projetos Python

---

# Próximas melhorias

* Implementar um agente com Function Calling (Tools).
* Permitir consultas em linguagem natural ao banco de dados.
* Adicionar testes automatizados.
* Migrar de SQLite para PostgreSQL.
* Criar uma API com FastAPI.
* Disponibilizar interface web utilizando Streamlit.
