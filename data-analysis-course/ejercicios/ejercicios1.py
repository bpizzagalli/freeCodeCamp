# %%
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

sales = pd.read_csv(
    'data/sales_data.csv',
    parse_dates=['Date'])

print(sales.head())


# What's the mean of Customers_Age?
print(sales['Customer_Age'].mean())

# What's the mean of Order_Quantity?
print(sales['Order_Quantity'].mean())


# How many sales per year do we have?
print(sales['Year'].value_counts())

# How many sales per month do we have?
print(sales['Month'].value_counts())

# Which country has the most sales quantity of sales?
print(sales['Country'].value_counts().head(1))

# Create a list of every product sold
print(sales['Product'].unique())

# Create a bar plot showing the 10 most sold products (best sellers):
print(sales['Product'].value_counts().head(10).plot(kind='bar', figsize=(14,6)))

# Can you see any relationship between Unit_Cost and Unit_Price?
sales.plot(kind='scatter', x='Unit_Cost', y='Unit_Price', figsize=(6,6))

# Can you see any relationship between Order_Quantity and Profit?
sales.plot(kind='scatter', x='Order_Quantity', y='Profit', figsize=(10,6))

#Can you see any relationship between Profit per Country?
sales[['Profit', 'Country']].boxplot(by='Country', figsize=(10,6))

#Can you see any relationship between the Customer_Age per Country?
sales[['Customer_Age', 'Country']].boxplot(by='Country', figsize=(10,6))

#Add and calculate a new Calculated_Date column
sales['Calculated_Date'] = sales[['Day', 'Month', 'Year']].apply(lambda x:'{}-{}-{}'.format(x[0],x[1],x[2]), axis=1)
print(sales['Calculated_Date'].head(10))

#Parse your Calculated_Date column into a datetime object
sales['Calculated_Date'] = pd.to_datetime(sales['Calculated_Date'])
print(sales['Calculated_Date'].head(5))

#How did sales evolve through the years?
sales['Calculated_Date'].value_counts().plot(kind='line', figsize=(14,6))

#Increase 50 U$S revenue to every sale
sales['Revenue'] += 50

#How many orders were made in Canada or France?
sales.loc[(sales['Country'] == 'Canada') | (sales['Country'] == 'France')].shape[0]

#How many Bike Racks orders were made from Canada?
sales.loc[(sales['Country'] == 'Canada') & (sales['Sub_Category'] == 'Bike_Racks')].shape[0]

#How many orders were made in each region (state) of France?
france_states = sales.loc[sales['Country'] == 'France', 'State'].value_counts()
#Go ahead and show a bar plot with the results:
france_states.plot(kind='bar', figsize = (14,6))

#How many sales were made per category?
sales_category = sales['Product_Category'].value_counts()
#Go ahead and show a pie plot with the results:
sales_category.plot(kind='pie', figsize = (14,6))

#How many orders were made per accessory sub-categories?
accessories = sales.loc[sales['Product_Category'] == 'Accessories', 'Sub_Category'].value_counts()
#Go ahead and show a bar plot with the results:
accessories.plot(kind='bar', figsize = (14,6))

#How many orders were made per bike sub-categories?
bikes = sales.loc[sales['Product_Category'] == 'Bikes', 'Sub_Category'].value_counts()
#Go ahead and show a pie plot with the results:
bikes.plot(kind='pie', figsize = (14,6))

#Which gender has the most amount of sales?
sales['Customer_Gender'].value_counts()
#Go ahead and show a bar plot with the results:
sales['Customer_Gender'].value_counts().plot(kind='bar')

#How many sales with more than 500 in Revenue were made by men?
sales.loc[(sales['Revenue'] >= 500) & (sales['Customer_Gender'] == 'M')].shape[0]

#Get the top-5 sales with the highest revenue
sales.sort_values(['Revenue'], ascending=False).head(5)

#Get the sale with the highest Revenue
sales.sort_values(['Revenue'], ascending=False).head(1)

#What is the mean Order_Quantity of orders with more than 10K in revenue?
moreThan10k = sales['Revenue'] > 10000
sales.loc[moreThan10k, 'Order_Quantity'].mean()

#What is the mean Order_Quantity of orders with less than 10K in revenue?
lessThan10k = sales['Revenue'] < 10000
sales.loc[lessThan10k, 'Order_Quantity'].mean()

#How many orders were made in May of 2016?

may2016 = (sales['Month'] == 'May') & (sales['Year'] == 2016)
sales.loc[may2016].shape[0]

#How many orders were made between May and July of 2016?
betweenMonths = (sales['Year'] == 2016) & (sales['Month'].isin(['May','June','July']))
sales.loc[betweenMonths].shape[0]
#Show a grouped box plot per month with the profit values.
profit_2016 = sales.loc[sales['Year'] == 2016, ['Profit', 'Month']]
profit_2016.boxplot(by='Month', figsize=(14,6))

#Add 7.2% TAX on every sale Unit_Price within United States
sales.loc[sales['Country'] == 'United States', 'Unit_Price'] *= 1.072

# %%
