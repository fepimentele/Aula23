import pandas as pd 
import polars as pl
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

pl.Config.set_fmt_float("full")

ENDERECO_DADOS = r'./../dados/'

try:
    print('Lendo arquivo Parquet')
    inicio = datetime.now()

    # with pl.StringCache(): depreciado *não é mais usado*

    # Leitura Preguiçosa

    df_plano_execucao = (
        pl.scan_parquet(ENDERECO_DADOS + 'bolsa_familia.parquet') # Dados
            # Delimitar as Séries
        .select(['NOME MUNICÍPIO', 'VALOR PARCELA'])

        .with_columns([
                 # cria uma tabela de números, substituindo os nomes das cidades
                pl.col('NOME MUNICÍPIO').cast(pl.Categorical)
            ])
            # Agrupar
            .group_by('NOME MUNICÍPIO')
            # Soma
            .agg(pl.col('VALOR PARCELA').sum())
            # Ordenar
            .sort('VALOR PARCELA', descending=True)
        )

    df_bolsa_familia = df_plano_execucao.collect() # Os dados são carregados
   
    print(df_bolsa_familia.head(10))
    print(df_bolsa_familia.columns) # Mostra os nomes da séries

    final = datetime.now()

    print(f'Tempo de execução {final - inicio}')

except Exception as e:
    print(f'Erro ao ler arquivo .parquet {e}')