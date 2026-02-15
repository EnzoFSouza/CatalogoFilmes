# 🎬 Catálogo de Filmes

Projeto **Fullstack** de um **Catálogo de Filmes** desenvolvido para consolidar o aprendizado na criação de APIs utilizando **Fast API** do Python.
A aplicação permite o gerenciamento de um acervo pessoal de filmes, com persistência em banco de dados.

## 🛠️ Tecnologias Utilizadas
Backend:
- FastAPI
- Pydantic
- SQLite
- SQLAlchemy

Frontend:
- HTML
- CSS
- JavaScript

## 📁 Estrutura do Projeto
`server.py`: Ponto de entrada da aplicação, definições de rotas e lógica.  
`models.py`: Definição das tabelas do banco de dados (SQLAlchemy).  
`database.py`: Configuração da conexão e motor do banco de dados.  
`script.js`: Lógica de consumo da API e manipulação dinâmica do DOM.  
`style.css`: Estilização personalizada com foco em experiência do usuário (UX).

## 🚀 Diferenciais Técnicos e Arquitetura
  - Injeção de Dependência: Utilização do sistema de dependências do FastAPI para gerenciar sessões de banco de dados (get_db), garantindo que conexões sejam abertas e fechadas corretamente.
  - Schemas e Tipagem: Separação clara entre modelos de banco de dados (models.py) e modelos de entrada/saída de dados (server.py via Pydantic), prevenindo exposição indevida de dados.
  - Configuração do CORS: Configuração de segurança para permitir que o frontend consuma a API de forma controlada.
  - Código organizado em múltiplos arquivos para facilitar a manutenção e escalabilidade.
  - Documentação Automática: A API gera documentação interativa via Swagger UI (acessível em /docs)
<img width="1860" height="826" alt="Captura de tela 2026-02-15 191553" src="https://github.com/user-attachments/assets/bc1cc96f-7e88-4f10-96fd-cfe040a815ed" />

## 📥 Como executar o projeto
1. Configuração do Backend
  - Instale as dependências:
    `pip install fastapi uvicorn sqlalchemy pydantic`
  - Inicie o servidor:
    `uvicorn server:app --reload`
    
2. Execução do Frontend
  - Abrir o arquivo `index.html` no navegador (recomenda-se o uso da extensão Live Server no VS Code para rodar na porta 5500, conforme configurado no CORS).
