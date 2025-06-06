# 🔥 Análise de Focos de Incêndio no Brasil

Este projeto realiza a **coleta, processamento, análise e geração automática de relatórios** sobre os focos de incêndio detectados por satélites no Brasil, com base em dados diários fornecidos pelo INPE.

## 📦 Estrutura do Projeto

```
projeto_focos_incendio/
├── data/                # Dados brutos (.csv) diários
├── output/              # Gráficos gerados automaticamente
├── reports/             # Relatórios HTML finais
├── templates/           # Template HTML Jinja2 para o relatório
├── modules/             # Módulos de processamento e análise
│   ├── coleta.py
│   ├── processamento.py
│   ├── analise.py
│   ├── alerta.py
│   └── relatorio.py
├── main.py              # Orquestra o pipeline completo
├── extrair_csvs.py      # Faz download dos arquivos CSV do INPE
├── requirements.txt     # Lista de dependências
└── README.md            # Este arquivo
```

## ⚙️ Requisitos

Instale as bibliotecas necessárias com:

```bash
pip install -r requirements.txt
```

## 🚀 Como Executar

### 1. Baixar os dados do INPE

Execute o script de extração para baixar os últimos arquivos `.csv`:

```bash
python extrair_csvs.py
```

Os arquivos serão salvos automaticamente na pasta `data/`.

### 2. Gerar relatório

Com os dados salvos, execute o pipeline completo:

```bash
python main.py
```

O relatório será salvo em:

```
reports/relatorio_final.html
```

Abra o HTML no navegador para visualizar.

## 📊 Funcionalidades

- 🔄 Coleta automática dos dados diários do INPE
- 🧼 Limpeza e padronização dos dados
- 📈 Geração de gráficos:
  - Focos por dia
  - Focos por semana
  - Focos por bioma
- 🚨 Identificação de alertas críticos com base em:
  - Risco de fogo > 0.85
  - FRP > 50
  - ≥ 10 dias sem chuva
- 📑 Relatório em HTML com resumo por estado e tabela interativa dos alertas

## ✍️ Autor

Este projeto foi desenvolvido como parte de um trabalho prático sobre monitoramento ambiental e geração automatizada de relatórios com Python.
