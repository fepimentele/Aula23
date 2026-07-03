import pandas as pd 
import polars as pl
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

pl.Config.set_fmt_float("full")

ENDERECO_DADOS = r'./../dados/'

# try:
#     print('Obtendo dados....')

#     inicio = datetime.now()


#     lista_arquivo = ['202301_AuxilioBrasil.csv',
#                      '202302_AuxilioBrasil.csv',
#                     ]
   
    
#     df_auxilio_brasil = None

#     for arquivo in lista_arquivo:
#         print(f'\nProcessando o arquivo: {arquivo}')

#         df = pl.read_csv(ENDERECO_DADOS + arquivo, separator=';', encoding='iso-8859-1')
#         print(df.head())

#         if df_auxilio_brasil is None:
#             df_auxilio_brasil = df

#         else:
#             df_auxilio_brasil = pl.concat([df_auxilio_brasil, df])

#         del df

#     print(df_auxilio_brasil.head())
#     print(df_auxilio_brasil.shape)

#     df_auxilio_brasil = df_auxilio_brasil.with_columns(
#         pl.col('VALOR PARCELA')
#         .str.replace(',','.')
#         .cast(pl.Float64)
#     )

#     final = datetime.now()

#     print(f'Tempo de execução: {final - inicio}')

#     print('\nIniciando a Gravação do Arquivo Parquet')
#     df_auxilio_brasil.write_parquet(ENDERECO_DADOS + 'auxilio_brasil.parquet')

#     print('\nArquivo salvo com sucesso...')
#     final = datetime.now()
#     print(f'\nTotal do tempo gasto {final - inicio}')


# except Exception as e:
#     print(f'Erro ao realizar a leitura dos meses: {e}')



try:
    print('Lendo arquivo Parquet')
    inicio = datetime.now()

    df_auxilio = (
        pl.scan_parquet(ENDERECO_DADOS + 'auxilio_brasil.parquet')
    
            .select(['NOME MUNICÍPIO', 'VALOR PARCELA'])
        
            .with_columns([
                pl.col('NOME MUNICÍPIO').cast(pl.Categorical)
            ])
            .group_by('NOME MUNICÍPIO')
        
            .agg(pl.col('VALOR PARCELA').sum())
        
            .sort('VALOR PARCELA', descending=True)
    )

    df_auxilio_brasil = df_auxilio.collect()

    print(df_auxilio_brasil.head(10))
    print(df_auxilio_brasil.columns)

    final = datetime.now()

    print(f'Tempo de execusão {final - inicio}')

except Exception as e:
    print(f'Erro ao ler arquivo .parquet {e}')

    









