import numpy as np
import pandas as pd

artists = pd.read_json('./files/artists.json')

print(artists.keys())
artists = artists.drop('bio', axis=1)
artists = artists.set_index('name')


artists.to_csv('./files/artists.csv')