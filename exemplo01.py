import pandas as pd 
import polars as pl 

from datetime import datetime 

import os

ENDERECO_DADOS = r'./../dados/'

try: 
    print('Obtendo os dados')
    inicio = datetime.now()

    # LISTA PARA GUARDAR CADA ARQUIVO QUE TERMINA COM CSV
    # UTILIZAREMOS ESTÁ LISTA.

    lista_arquivos = []

    df_bolsa_familia = None

    # LISTAR OS NOMES DOS ARQUIVOS DA PASTA DADOS
    lista_dir_arquivos = os.listdir(ENDERECO_DADOS)
    # print(lista_dir_arquivos)


    # VERIFICAR SE TODOS SÃO CSVs
    for arquivo in lista_dir_arquivos:
        if arquivo.endswith('.csv'):
            lista_arquivos.append(arquivo)

    # print(lista_arquivos)
    
    # leitura dos aquivos
    for arquivo in lista_arquivos:
        df = pl.read_csv(ENDERECO_DADOS + arquivo, separator=';', encoding='iso-8859-1')
        print(df.head())

        # Contatenar (Juntas os Datafraemes)
        if df_bolsa_familia is None:
            df_bolsa_familia = df
        else:
            df_bolsa_familia = pl.concat([df_bolsa_familia, df])
        
        del df

        print(f'\nArquivo {arquivo} processado com sucesso!')
        print(df_bolsa_familia.shape)
        
    df_bolsa_familia = df_bolsa_familia.with_columns(
        pl.col('VALOR PARCELA').str.replace(',','.').cast(pl.Float64)
    )

    # Salvando em arquivo Parquet
    print('\nIniciando a Gravação do Arquivo Parquet')
    df_bolsa_familia.write_parquet(ENDERECO_DADOS + 'bolsa_familia.parquet')

    print('\nArquivo salvo com sucesso...')
    final = datetime.now()
    print(f'\nTotal do tempo gasto {final - inicio}')

except Exception as e:
    print(f'Erro ao obter os dados {e}')


