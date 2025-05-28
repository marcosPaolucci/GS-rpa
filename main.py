from modules import coleta, processamento, analise, alerta, relatorio

def run_pipeline():
    print("🔄 Iniciando pipeline de análise de focos de incêndio...")

    # 1. Coleta dos dados
    print("📥 Carregando arquivos CSV...")
    df = coleta.carregar_csvs(diretorio='data')

    # 2. Processamento dos dados
    print("🧹 Processando e limpando os dados...")
    df_proc = processamento.tratar(df)

    # 3. Análise dos dados
    print("📊 Gerando gráficos e estatísticas...")
    graficos, resumo = analise.gerar(df_proc)

    # 4. Identificação de alertas
    print("🚨 Verificando focos críticos...")
    alertas = alerta.identificar_alertas(df_proc)

    # 5. Geração do relatório
    print("📝 Gerando relatório PDF final...")
    contexto = {
        "resumo": resumo,
        "graficos": graficos,
        "alertas": alertas,
    }
    relatorio.gerar_relatorio(contexto)

    print("✅ Pipeline finalizado com sucesso!")

if __name__ == "__main__":
    run_pipeline()
