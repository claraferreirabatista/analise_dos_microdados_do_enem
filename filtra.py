import pandas as pd
import numpy as np

df = pd.read_csv(r'MICRODADOS_ENEM_2019.csv', encoding='iso8859-1', sep = ';')
norte = df.loc[df['SG_UF_PROVA'].isin(['AM','PA','AC','RR','TO','RO','AP'])]

"""nordeste = df.loc[df['SG_UF_PROVA'].isin(['MA','PI','CE','RN','PB','PE','AL','SE','BA'])]
centroeste = df.loc[df['SG_UF_PROVA'].isin(['GO','MT','MS'])]
sudeste = df.loc[df['SG_UF_PROVA'].isin(['SP','RJ','MG','ES'])]
sul = df.loc[df['SG_UF_PROVA'].isin(['PR','SC','RS'])]"""

norte.to_csv('ENEM_2019_NORTE', sep=';')

"""print('Norte\n')
print(norte.info())
print('nordeste\n')
print(nordeste.info())
print('centroeste\n')
print(centroeste.info())
print('sudeste\n')
print(sudeste.info())
print('sul\n')
print(sul.info())"""