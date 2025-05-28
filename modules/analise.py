import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style='whitegrid')


def gerar(df):
    """
    Gera gráficos e resumos estatísticos principais a partir dos dados processados.
    """
    graficos = []
    resumo = {}

    # Focos por estado
    resumo['focos_por_estado'] = df['estado'].value_counts()

    # Focos por dia
    focos_dia = df['data_coleta'].value_counts().sort_index()
    plt.figure(figsize=(10, 4))
    focos_dia.plot(marker='o', title='Focos por dia')
    plt.tight_layout()
    plt.savefig('output/focos_por_dia.png')
    graficos.append('output/focos_por_dia.png')

       # Focos por semana
    focos_semana = df.groupby('semana').size()
    plt.figure(figsize=(8, 4))
    focos_semana.plot(kind='bar', title='Focos por semana')
    plt.tight_layout()
    plt.savefig('output/focos_por_semana.png')
    graficos.append('output/focos_por_semana.png')

    # Focos por bioma
    plt.figure(figsize=(8, 4))
    df['bioma'].value_counts().plot(kind='bar', title='Distribuição por Bioma')
    plt.tight_layout()
    plt.savefig('output/focos_por_bioma.png')
    graficos.append('output/focos_por_bioma.png')

    return graficos, resumo