import pandas as pd

def tratar(df):
    """
    Realiza limpeza, normalização de colunas e conversões de tipos.
    """
    # Corrigir nomes de colunas (remover espaços)
    df.columns = [col.strip() for col in df.columns]

    # Conversão de tipos
    df['data_hora_gmt'] = pd.to_datetime(df['data_hora_gmt'], errors='coerce')
    df['hora'] = df['data_hora_gmt'].dt.hour
    df['semana'] = df['data_coleta'].apply(lambda x: x.isocalendar()[1])

    # Preenchimento de dados ausentes, se necessário
    df.fillna({
        'risco_fogo': 0,
        'frp': 0,
        'numero_dias_sem_chuva': 0,
        'precipitacao': 0
    }, inplace=True)

    return df