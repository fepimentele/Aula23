import pandas as pd 
import polars as pl
from datetime import datetime
# pip install fastparquet

ENDERECO_DADOS = r'./../dados/'

try: 
    print('Lendo arquivo Parquet')
    inicio = datetime.now()

    # Leitura Preguiçosa
    df_plano_execucao = pl.scan_parquet(ENDERECO_DADOS + 'bolsa_familia.parquet')

    df_bolsa_familia = df_plano_execucao.collect()
    print(df_bolsa_familia.head())

    # Leitura Direta

    # df_bolsa_familia = pd.read_parquet(ENDERECO_DADOS + 'bolsa_familia.parquet')
    df_bolsa_familia = pd.read_parquet(ENDERECO_DADOS + 'bolsa_familia.parquet')
    # print(df_bolsa_familia.head())

    df_filtrado = df_bolsa_familia.filter(pl.col('VALOR PARCELA')) > 2500
    # print(filtrado.shape)

    # Ordenando e mostrando os 20 primeiros
    # print(df_bolsa_familia.sort('VALOR PARCELA', descending=True).head(20))

    final = datetime.now()
    print(f'\nTotal do tempo gasto {final - inicio}')

except Exception as e:
    print(f'Erro ao ler arquivo .parquet {e}')

try: 
    #Array
    array_valor_parcela = np.array(df_bolsa_familia)
except Exception as e:
    print(f'Erro ao obter o Array {e}')

try:
    import matplotlib.pyplot as plt
    # pip install matplotlib
    plt.boxplot(array_valor_parcela, vert=False)
    plt.title('Distribuição Bolsa Família')