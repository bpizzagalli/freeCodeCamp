#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
print(pd.__version__)

df = pd.DataFrame({
    'Population': [35.467, 63.951, 80.94 , 60.665, 127.061, 64.511, 318.523],
    'GDP': [
        1785387,
        2833687,
        3874437,
        2167744,
        4602367,
        2950039,
        17348075
    ],
    'Surface Area': [
        9984670,
        640679,
        357114,
        301336,
        377930,
        242495,
        9525067
    ],
    'HDI': [
        0.913,
        0.888,
        0.916,
        0.873,
        0.891,
        0.907,
        0.915
    ],
    'Continent': [
        'America',
        'Europe',
        'Europe',
        'Europe',
        'Asia',
        'Europe',
        'America'
    ]
}, columns=['Population', 'GDP', 'Surface Area', 'HDI', 'Continent'])

df.index = [
    'Canada',
    'France',
    'Germany',
    'Italy',
    'Japan',
    'United Kingdom',
    'United States',
]

print(df)


langs= pd.Series(
    ['English', 'French', 'German', 'Italian', 'Japanese', 'English', 'English'],
    index=['Canada', 'France', 'Germany', 'Italy', 'Japan', 'United Kingdom', 'United States'],
    name='Language'
)

df['Language'] = langs

#print(df)

gdpc=df['GDP'] / df['Population']
df['GDPC'] = gdpc
#print(df)

print(df['Population'].describe())



# EJERCICIOS DATAFRAMES


### Create an empty pandas DataFrame
pd.DataFrame(
    data=[None],
    index=[None],
    columns=[None]
)

### Create a `marvel_df` pandas DataFrame with the given marvel data
marvel_data = [
    ['Spider-Man', 'male', 1962],
    ['Captain America', 'male', 1941],
    ['Wolverine', 'male', 1974],
    ['Iron Man', 'male', 1963],
    ['Thor', 'male', 1963],
    ['Thing', 'male', 1961],
    ['Mister Fantastic', 'male', 1961],
    ['Hulk', 'male', 1962],
    ['Beast', 'male', 1963],
    ['Invisible Woman', 'female', 1961],
    ['Storm', 'female', 1975],
    ['Namor', 'male', 1939],
    ['Hawkeye', 'male', 1964],
    ['Daredevil', 'male', 1964],
    ['Doctor Strange', 'male', 1963],
    ['Hank Pym', 'male', 1962],
    ['Scarlet Witch', 'female', 1964],
    ['Wasp', 'female', 1963],
    ['Black Widow', 'female', 1964],
    ['Vision', 'male', 1968]
]

marvel_df= pd.DataFrame(
    data=marvel_data
)
print(marvel_df)

### Add column names to the `marvel_df`
col_names = ['name', 'sex', 'first_appearance']
marvel_df.columns = col_names

### Add index names to the `marvel_df` (use the character name as index)
marvel_df.index=marvel_df['name']
marvel_df = marvel_df.drop(columns='name')


### Drop 'Namor' and 'Hank Pym' rows
print(marvel_df.drop(['Namor', 'Hank Pym']))

### Show the first 5 elements on `marvel_df`
print(marvel_df.head(5))

### Show the last 5 elements on `marvel_df`
print(marvel_df.tail(5))

### Show just the sex of the first 5 elements on `marvel_df`
print(marvel_df['sex'].head(5).to_frame())
print(marvel_df.head().sex.to_frame())

### Show the first_appearance of all middle elements on `marvel_df`
print(marvel_df.iloc[1:-1].first_appearance.to_frame())

### Show the first and last elements on `marvel_df`
print(marvel_df.iloc[[0, -1]])

### Modify the `first_appearance` of 'Vision' to year 1964

marvel_df.loc['Vision', 'first_appearance'] = 1964

### Add a new column to `marvel_df` called 'years_since' with the years since `first_appearance`
marvel_df['years_since'] = 2022 - marvel_df['first_appearance']

### Given the `marvel_df` pandas DataFrame, make a mask showing the female characters
mask = (marvel_df['sex'] == 'female')
print(marvel_df[mask])

### Given the `marvel_df` pandas DataFrame, get the male characters
maskm= (marvel_df['sex'] == 'male')
print(marvel_df[maskm])

### Given the `marvel_df` pandas DataFrame, get the characters with `first_appearance` after 1970
mask1970 = (marvel_df['first_appearance'] > 1970)
print(marvel_df[mask1970])

### Given the `marvel_df` pandas DataFrame, get the female characters with `first_appearance` after 1970
mask1970fem = ((marvel_df['first_appearance'] > 1970) & (marvel_df['sex'] == 'female'))
print(marvel_df[mask1970fem])

### Show basic statistics of `marvel_df`
print(marvel_df.describe())

### Given the `marvel_df` pandas DataFrame, show the mean value of `first_appearance`
print(marvel_df['first_appearance'].mean())

### Given the `marvel_df` pandas DataFrame, show the min value of `first_appearance`
print(marvel_df['first_appearance'].min())

### Given the `marvel_df` pandas DataFrame, get the characters with the min value of `first_appearance`
maskminval= (marvel_df['first_appearance'] == marvel_df['first_appearance'].min())
print(marvel_df[maskminval])

### Reset index names of `marvel_df`
marvel_df = marvel_df.reset_index()
print(marvel_df)

### Plot the values of `first_appearance`
marvel_df['first_appearance'].plot()

### Plot a histogram (plot.hist) with values of `first_appearance`
marvel_df['first_appearance'].plot.hist()
