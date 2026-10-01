# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
from datetime import datetime
import seaborn as sns
import matplotlib.pyplot as plt

# 1- Import the data

# Read the excel files

pizza_sales_df = pd.read_excel('pizza_sales.xlsx')
pizza_size_df = pd.read_csv('pizza_size.csv')
pizza_category_df = pd.read_csv('pizza_category.csv')


# 2- Exploring the data 

# Viewing top and bottom rows in a dataframe
pizza_sales_df.head()
pizza_sales_df.head(10)

pizza_sales_df.tail()
pizza_sales_df.tail(10)

pizza_sales_df.describe()
pizza_description = pizza_sales_df.describe()


# 3- Data Cleaning

# Have a look at non-null counts per column
pizza_sales_df.info()

# count the number of null values in each column 
null_count = pizza_sales_df.isnull().sum()

# check for duplicated rows
duplicated_rows = pizza_sales_df.duplicated().sum()
print(duplicated_rows)




# To select a column 
quantity_column = pizza_sales_df['quantity']
selected_columns = pizza_sales_df[['order_id', 'quantity', 'unit_price']]

# Get the row with index label 3
row = pizza_sales_df.loc[3]

# Get two row with index label 3 and 5
rows = pizza_sales_df.loc[[3, 5]]

# Get rows between index lable 3 and 5
subset = pizza_sales_df.loc[3:5]

# Get rows between index label 3 and 5 and specific columns
subset = pizza_sales_df.loc[3:5, ['quantity', 'unit_price']]




# set an index as a column in dataframe
pizza_sales_df.set_index('order_details_id', inplace=True) # inplace will set the index without saving it into new dataframe

# Resetting an index
pizza_sales_df.reset_index(inplace = True)


# Truncate Dataframe before index 3 
truncated_before = pizza_sales_df.truncate(before=3)

# Truncate Dataframe after index 5 
truncated_after = pizza_sales_df.truncate(after=5)

# Truncating columns
quantity_series = pizza_sales_df['quantity']

# Truncating series before index 3
truncated_series_before = quantity_series.truncate(before=3)

# Truncating series after index 5
truncated_series_after = quantity_series.truncate(after=5)





# Basic Filtering 
filtered_rows = pizza_sales_df[pizza_sales_df['unit_price'] > 20]

# Filtering on date
pizza_sales_df['order_date'] = pizza_sales_df['order_date'].dt.date
date_target = datetime.strptime('2015-12-15', '%Y-%m-%d').date()
filtered_rows_by_date = pizza_sales_df[pizza_sales_df['order_date'] > date_target]


# Filtering on multiple conditions

# Using the AND condition 
bbq_chicken_rows = pizza_sales_df[(pizza_sales_df['unit_price'] > 15) 
                                  & (pizza_sales_df['pizza_name'] == 'The Barbecue Chicken Pizza')]

# Using the OR condition 

bbq_chicken_rows_or = pizza_sales_df[(pizza_sales_df['unit_price'] > 15) 
                                  | (pizza_sales_df['pizza_name'] == 'The Barbecue Chicken Pizza')]

# Filter a specific range 
high_sales = pizza_sales_df[(pizza_sales_df['unit_price'] > 15) & (pizza_sales_df['unit_price'] <= 20) ]




# Dropping Null values 
pizza_sales_null_values_dropped = pizza_sales_df.dropna()

# checking null values dropped or not 
null_count = pizza_sales_null_values_dropped.isnull().sum()

# Replace null with a value
date_na_fill = datetime.strptime('2000-01-01', '%Y-%m-%d').date()
pizza_sales_null_replaced = pizza_sales_df.fillna(date_na_fill)




# Deleting specific rows and columns in a dataframe
filtered_rows_2 = pizza_sales_df.drop(2, axis =0) # axis = 0 is for row and axis = 1 is for column

# Deleting rows 5, 7, 9
filtered_rows_5_7_9 = pizza_sales_df.drop([5,7,9], axis =0)

# Delete column by column name
filtered_unit_price = pizza_sales_df.drop('unit_price', axis = 1)

# Delete multiples columns
filtered_unit_price_and_order_id = pizza_sales_df.drop(['unit_price', 'order_id'], axis = 1)




# Sorting a dataframe in pandas 

# Sorting in asc order
sorted_df = pizza_sales_df.sort_values('total_price')

# Sorting in desc order
sorted_df = pizza_sales_df.sort_values('total_price', ascending =False) 

# Sorting by multiple columns
sorted_df = pizza_sales_df.sort_values(['pizza_category_id', 'total_price'], ascending = [True, False])




# Group by pizza size id and get the count of sales (row count)
grouped_df_pizza_size = pizza_sales_df.groupby(['pizza_size_id']).count()

# Group by pizza size id and get the sum 
grouped_df_pizza_size_by_sum = pizza_sales_df.groupby(['pizza_size_id'])['total_price'].sum()

# Group by pizza size id and sum total_price and quantity
grouped_df_pizza_size_sales_quantity = pizza_sales_df.groupby(['pizza_size_id'])[['total_price', 'quantity']].sum()

# Looking at different aggregation functions

#count(): Counts the number of non-NA/null values in each group.
#sum(): Sums the values in each group.
#mean(): Calculates the mean of values in each group.
#std(): Computes the standard deviation in each group.
#var(): Computes the standard variance in each group.
#min(): Finds the minimum values in each group.
#max(): Finds the maximum values in each group.
#prod(): Computes the product of values in each group.
#first(), last(): Gets the first and last values in each group.
#size(): Returns the size of each group (including NaN/NA values).
#nunique(): Counts the number of unique values in each group.

grouped_df_agg = pizza_sales_df.groupby(['pizza_size_id'])[['total_price', 'quantity']].mean()

# Using agg function to perform different aggregation on different columns 
aggregated_date = pizza_sales_df.groupby(['pizza_size_id']).agg({'quantity' : 'sum', 'total_price' : 'mean'})



# Merging pizza sales df and pizza size df
merged_df = pd.merge(pizza_sales_df, pizza_size_df, on='pizza_size_id')

# Add pizza category information from pizza category df
merged_df = pd.merge(merged_df, pizza_category_df, on='pizza_category_id')

# Concatenate two dataframes - appending rows to a dataframe - vertically
another_pizza_sales_df = pd.read_excel('another_pizza_sales.xlsx')
concatenate_vertically = pd.concat([pizza_sales_df, another_pizza_sales_df])
concatenate_vertically = concatenate_vertically.reset_index()

# Concatenate two dataframes - appending columns to a dataframe - horizontally
pizza_sales_voucher_df = pd.read_excel('pizza_sales_voucher.xlsx')
concatenate_horizontally = pd.concat([pizza_sales_df, pizza_sales_voucher_df], axis =1)




# Converting to lower case 
lower_text = pizza_sales_df['pizza_ingredients'].str.lower()
pizza_sales_df['pizza_ingredients'] = pizza_sales_df['pizza_ingredients'].str.lower()

# Converting to upper case 
pizza_sales_df['pizza_ingredients'] = pizza_sales_df['pizza_ingredients'].str.upper()

# Converting to Title case 
pizza_sales_df['pizza_ingredients'] = pizza_sales_df['pizza_ingredients'].str.title()




# Replacing text in dataframe
replaced_text = pizza_sales_df['pizza_ingredients'].str.replace('Feta Cheese', 'Mozzarella')
pizza_sales_df['pizza_ingredients'] = pizza_sales_df['pizza_ingredients'].str.replace('Feta Cheese', 'Mozzarella')




# Removing whitespaces from dataframes
pizza_sales_df['pizza_name'] = pizza_sales_df['pizza_name'].str.strip()




# Generating a Box Plot
sns.boxplot(x='category', y='total_price', data = merged_df)
plt.xlabel('pizza category')
plt.ylabel('Total Sale')
plt.title('Boxplot showing distribution of sales by category')
plt.show()

































































