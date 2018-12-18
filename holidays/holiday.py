# Wydruk polskich świąt z datami - z pliku csv.

import pandas as pd
import numpy as np
from tabulate import tabulate


path = ('holidays_csv.csv')

df = pd.read_csv(path)
# kasuj kolumnę province code
df.__delitem__('Province Code')
#print(df.loc[0:3, lambda x: ['Country Code']])
#print(df.loc[0:3, ['Country Code', 'Holiday Name']])

print('Kolumny w pliku csv:',list(df))
#  tylko PL z kolumny Country Code:
pl = df.loc[df['Country Code'] == 'PL']
# ilosc wierszy w zbiorze PL = ilosc swiat :
print('Ilosc swiat w PL:', pl.shape[0])

# sprawdzamy jakie sa typy swiat:
print('Typy swiat:', ((df['Type of Holiday']).unique()))

# ilosc swiat posortowane:
#print(df['Country Code'].value_counts())
#  ilosc swiat nieposortowane:
#print(df.groupby('Country Code').size())
wydruk = df.groupby('Country Code').size()

# święta - tylko public:
swieta_optional  = df.loc[(df['Country Code'] == 'PL') & (df['Type of Holiday'] == 'public')]

swieta_optional.drop_duplicates('Holiday Name',  keep='last')
polskie_swieta = swieta_optional.loc[:, ['Date','Type of Holiday','Holiday Name']]
sq = pd.DataFrame(polskie_swieta)

rok_2019 = sq['Date']>'2019-00-00 00:00:00'
print(tabulate(sq[rok_2019],headers='keys',tablefmt='psql'))