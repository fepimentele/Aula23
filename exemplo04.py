import pandas as pd 
import polars as pl
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

ENDERECO_DADOS = r'./../dados/'

try:
    print('Lendo arquivo Parquet')
    inicio = datetime.now()

# Leitura Preguiçosa
    df_plano_execucao = (
        pl.scan_parquet(
            ENDERECO_DADOS + 'bolsa_familia.parquet'
            # Dados
            # Delimitar as Séries
            # --- Técnica
            # Agrupar
            # Soma
            # Ordenar
        )
    )

    df_bolsa_familia = df_plano_execucao.collect()
    print(df_bolsa_familia.head(10))

except Exception as e:
    print(f'Erro ao ler arquivo parquet {e}')