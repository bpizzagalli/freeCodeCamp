import numpy as np
import pandas as pd

col_names = ['Title', 'Air date', 'Production code', 'Season', 'Number in season',
             'Number in series', 'US viewers (million)', 'Views', 'IMDB rating']


simpsons = pd.read_csv('./files/simpsons-episodes.tsv',
sep='\t',
names=col_names,
skiprows=4,
usecols=['Title', 'Air date', 'Production code', 'IMDB rating'],
index_col='Production code',
na_values='no_val',
parse_dates=['Air date']
)


print(simpsons.head())
