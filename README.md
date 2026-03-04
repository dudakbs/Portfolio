# Portfolio
Este projeto é uma aplicação web desenvolvida em Django para centralizar meus projetos acadêmicos e profissionais.

URL Pública: https://portfolio-wl3q.onrender.com
---
## Tecnologias Utilizadas
* Linguagem: Python 3.12
* Framework Web: Django 5.2
* Banco de Dados: PostgreSQL (Hospedado via Neon.tech)
* Servidor de Produção: Gunicorn & WhiteNoise (Arquivos estáticos)
* Hospedagem: Render
---
## Guia de execução

### Clone o repositório:
git clone https://github.com/dudakbs/Portfolio
cd Portfolio/WebPortfolio

### Crie e ative um ambiente virtual:
python -m venv venv

### Instale as dependências:
pip install -r requirements.txt

### Configure as variáveis de ambiente:
Crie um arquivo .env e adicione sua DATABASE_URL do Neon.

### Rode as migrações e o servidor:
python manage.py migrate
python manage.py runserver