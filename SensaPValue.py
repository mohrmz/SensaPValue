
import pandas as pd
from scipy.stats import ttest_ind, ranksums 

df = pd.read_excel('Sensa.xlsx')
columns = df.columns.values
matching = ['per','rec','f1']
for match in matching:
    print(match)
    s1, p1 = ttest_ind(df['our('+match+')'].values, df['cod2vec('+match+')'].values, alternative="greater")
    print('cod2vec :' +str(p1))
    s2, p2 = ttest_ind(df['our('+match+')'].values, df['cod2seq('+match+')'].values, alternative="greater")
    print('cod2seq :' +str(p2))

print('end')