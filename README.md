# Relatórios Automáticos com Python + n8n

## Descrição
Projeto que gera relatórios em PDF a partir de dados CSV usando Python e envia automaticamente via n8n Cloud.

## Estrutura
- backend/main.py → Script que gera PDF com gráficos
- data/data.csv → Dados de exemplo
- reports/report.pdf → PDF gerado
- n8n/n8n-flow.json → Workflow do n8n

## Como rodar
1. Instalar dependências: `pip install -r backend/requirements.txt`
2. Rodar script Python: `python backend/main.py`
3. Configurar link público do PDF no n8n Cloud
4. Executar workflow n8n → PDF enviado por e-mail
