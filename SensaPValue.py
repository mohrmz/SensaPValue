
import pandas as pd
from scipy.stats import ttest_ind, ranksums 

df = pd.read_excel('Sensa.xlsx')

s, p = ttest_ind(df[criterion_].values, df[criterion_].values, alternative="greater")

print('end')