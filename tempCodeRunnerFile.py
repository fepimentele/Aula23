import pandas as pd 
import polars as pl
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

pl.Config.set_fmt_float("full")

ENDERECO_DADOS = r'./../dados/'


try:
    print('Obtendo dados....')

    inicio = datetime.now()

    lista_arquivo = ['202301_AuxilioBrasil.csv',
                     '202302_AuxilioBrasil.csv',
                    ]
   # print('Lendo arquivo Parquet')
   # inicio = datetime.now()
    
    df_plano_execucao = (pl.scan_parquet(ENDERECO_DADOS + '202301_AuxilioBrasil.csv', '202302_AuxilioBrasil.csv'))