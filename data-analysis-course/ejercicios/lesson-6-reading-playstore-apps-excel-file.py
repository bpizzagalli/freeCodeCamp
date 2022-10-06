import numpy as np
import pandas as pd

data_url = 'https://github.com/ine-rmotr-projects/project-files/files/4086772/playstore.xlsx'

playstore_df = pd.read_excel(data_url,
usecols=['App', 'Rating', 'Installs', 'Rating', 'Genres', 'Last_Updated'],
parse_dates=['Last_Updated'])

print(playstore_df['Rating'].sort_values(ascending=False).head(25))