import os
import pandas as pd
from datetime import datetime

def carregar_csvs(diretorio='data'):
    """
    Lê todos os arquivos com o padrão 'focos_diario_br_YYYYMMDD.csv' do diretório indicado
    e adiciona uma coluna com a data extraída do nome do arquivo.
    """
    arquivos = [f for f in os.listdir(diretorio) if f.startswith('focos_diario_br_') and f.endswith('.csv')]
    df_total = pd.DataFrame()

    for arq in arquivos:
        data_str = arq.split('_')[-1].replace('.csv', '')
        data = datetime.strptime(data_str, "%Y%m%d").date()

        df = pd.read_csv(os.path.join(diretorio, arq))
        df['data_coleta'] = data
        df_total = pd.concat([df_total, df], ignore_index=True)

    return df_total


