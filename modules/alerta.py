def identificar_alertas(df):
    """
    Identifica registros que atendem a TODAS as condições críticas.
    """
    alertas = df[
        (df['risco_fogo'] > 0.8) &
        (df['frp'] > 50) &
        (df['numero_dias_sem_chuva'] >= 10)
    ].copy()

    alertas['motivo_alerta'] = 'Atende todos os critérios: risco alto, FRP alto e estiagem prolongada'

    return alertas
