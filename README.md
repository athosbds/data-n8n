# Automated PDF Report Backend

[![Python](https://img.shields.io/badge/python-3.11-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

## Overview

Este projeto é um **backend em Python** para geração automatizada de relatórios em PDF, integração com Dropbox e envio por email usando n8n.  
O workflow inclui:

- Extração de dados de arquivos CSV (`data/data.csv`)
- Geração de relatórios PDF (`reports/report.pdf`)
- Upload para Dropbox
- Envio automático por email via Gmail
- Integração com n8n para automação e agendamento

---

## Setup

1. **Clone o repositório**

```bash
git clone https://github.com/SEU_USUARIO/data-n8n.git
cd data-n8n

python -m venv venv
# Windows
venv\Scripts\activate
# Linux/macOS
source venv/bin/activate

pip install -r backend/requirements.txt

Configurar credenciais
Coloque o token da Dropbox em credentials/dropbox_token.txt.
Configure variáveis de ambiente se necessário para Gmail OAuth2 ou n8n.

## Usage
python backend/main.py
```
# Workflow n8n

Importe o arquivo n8n/n8n-flow.json no n8n Cloud ou local.

Configure os nós de autenticação (Gmail, Dropbox).

Agende o trigger para execução automática (ex: diariamente às 9h).

GitHub Actions (opcional)

Você pode configurar CI/CD para automatizar geração de relatórios e push de PDFs para Dropbox/email.

