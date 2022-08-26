
import pandas as pd
from scipy.stats import ttest_ind, ranksums 
from decimal import Decimal

df = pd.read_excel('Sensa.xlsx')
columns = df.columns.values
matching = ['per','rec','f1']
print('->ttest_ind')
for match in matching:
    print(match)
    s1, p1 = ttest_ind(df['our('+match+')'].values, df['cod2vec('+match+')'].values, alternative="greater")
    print('cod2vec :' +str('%.2E' % Decimal(p1)))
    s2, p2 = ttest_ind(df['our('+match+')'].values, df['cod2seq('+match+')'].values, alternative="greater")
    print('cod2seq :' +str('%.2E' % Decimal(p2)))
print('->ranksums')
for match in matching:
    print(match)
    s1, p1 = ranksums(df['our('+match+')'].values, df['cod2vec('+match+')'].values, alternative="greater")
    print('cod2vec :' +str(str('%.2E' % Decimal(p1))))
    s2, p2 = ranksums(df['our('+match+')'].values, df['cod2seq('+match+')'].values, alternative="greater")
    print('cod2seq :' +str('%.2E' % Decimal(p2)))
print('end')