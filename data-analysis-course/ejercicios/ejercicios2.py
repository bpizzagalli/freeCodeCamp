# %%
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sqlite3


conn = sqlite3.connect('data/sakila.db')

df = pd.read_sql('''
    SELECT
        rental.rental_id, rental.rental_date, rental.return_date,
        customer.last_name AS customer_lastname,
        store.store_id,
        city.city AS rental_store_city,
        film.title AS film_title, film.rental_duration AS film_rental_duration,
        film.rental_rate AS film_rental_rate, film.replacement_cost AS film_replacement_cost,
        film.rating AS film_rating
    FROM rental
    INNER JOIN customer ON rental.customer_id == customer.customer_id
    INNER JOIN inventory ON rental.inventory_id == inventory.inventory_id
    INNER JOIN store ON inventory.store_id == store.store_id
    INNER JOIN address ON store.address_id == address.address_id
    INNER JOIN city ON address.city_id == city.city_id
    INNER JOIN film ON inventory.film_id == film.film_id
    ;
''', conn, index_col='rental_id', parse_dates=['rental_date', 'return_date'])



#df.shape

#df.info()

#df.describe()



#Whats the mean of film_rental_duration?
df['film_rental_duration'].mean()

#Whats the most common rental duration?
df['film_rental_duration'].value_counts().plot(kind='bar', figsize=(14,6))

#What is the most common rental rate?

#Show a pie plot with all possible rental rates
df['film_rental_rate'].value_counts().plot(kind='pie', figsize=(14,6))
#Show a bar plot with all possible rental rates
df['film_rental_rate'].value_counts().plot(kind='bar', figsize=(14,6))
#Which plot you think fits the best in this case? Why?
#I think the bar plot fits the best in this case because you can see whats the most common rental rate more clearly


#How is the replacement cost distributed?

#Show a box plot of the replacement costs.
df['film_replacement_cost'].value_counts().plot(kind='box', vert=False, figsize=(14,6))
#Show a density plot of the replacement costs.
df['film_replacement_cost'].value_counts().plot(kind='density', figsize=(14,6))

#Add a red line on the mean.
ax = df['film_replacement_cost'].plot(kind='density', figsize=(14,6))
ax.axvline(df['film_replacement_cost'].mean(), color='red')
#Add a green line on the median median.
ax.axvline(df['film_replacement_cost'].median(), color='green')


#How many films of each rating do we have?

#Show the raw count of each film rating.
df['film_rating'].value_counts()
#Show a bar plot with all possible film ratings.
df['film_rating'].value_counts().plot(kind='bar', figsize=(14,6))


#Does the film replacement cost vary depending on film rating?
#In the United States, film classification is a voluntary process with the 
#ratings issued by the Motion Picture Association of America (MPAA)
#via the Classification and Rating Administration (CARA).

#G (General Audiences): All Ages are Admitted.
#PG (Parental Guidance Suggested): Some Material May Not Be Suitable for Children.
#PG-13 (Parents Strongly Cautioned): Some Material May Be Inappropriate for Children Under 13.
#R (Restricted): Under 17 Requires Accompanying Parent or Adult Guardian.
#NC-17 (Adults Only): No One 17 and Under Admitted.
#Show a grouped box plot per film rating with the film replacement costs.
df[['film_rating', 'film_replacement_cost']].boxplot(by='film_rating', figsize=(14,6))


#Add and calculate a new rental_days column
#This numeric column should have the count of days between rental_date and return_date.

df['rental_days'] = df[['rental_date', 'return_date']].apply(lambda x: (x[1] - x[0]).days, axis=1)
df['rental_days'].head()

#Analyze the distribution of rental_days
#Calculate the mean of rental_days.
df['rental_days'].mean()
#Show a density (KDE) of rental_days.
ax= df['rental_days'].plot(kind='density', figsize=(14,6))
ax.axvline(df['rental_days'].mean(), color='red')

#Add and calculate a new film_daily_rental_rate column
#This value should be the division of film_rental_rate by film_rental_duration.
df['film_daily_rental_rate'] = df['film_rental_rate'] / df['film_rental_duration']
df['film_daily_rental_rate'].head()

#Analyze the distribution of film_daily_rental_rate
#Calculate the mean of film_daily_rental_rate.
df['film_daily_rental_rate'].mean()
#Show a density (KDE) of film_daily_rental_rate.
ax= df['film_daily_rental_rate'].plot(kind='density', figsize=(14,6))
ax.axvline(df['film_daily_rental_rate'].mean(), color='red')


#List 10 films with the lowest daily rental rate
df.loc[df['film_daily_rental_rate'] == df['film_daily_rental_rate'].min()].head(10)












# %%
