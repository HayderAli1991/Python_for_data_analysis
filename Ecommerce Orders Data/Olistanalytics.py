# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 18:21:03 2026

@author: Dell
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set the working directory
os.chdir('D:\Python for Data Analysis Udemy D Naidoo\My Practice\Ecommerce Orders Project')

# Check the current working directory
print(os.getcwd())

# =============================================================================
# Loading files 
# =============================================================================

# Load the orders data
orders_data = pd.read_excel('orders.xlsx')

# Load the payment data
payment_data = pd.read_excel('order_payment.xlsx')

# Load the customers data
customers_data = pd.read_excel('customers.xlsx')


# =============================================================================
# Describing the data
# =============================================================================

orders_data.info()
payment_data.info()
customers_data.info()

""" 
We check the null/missing values by comparing the Non-Null 
value and the Size of table in Variable Explorer

"""
# =============================================================================
# Handling Missing data
# =============================================================================

# Check for missing data in the orders data
orders_data.isnull().sum()
payment_data.isnull().sum()
customers_data.isnull().sum()

# Filling in missing values in orders data with a default value
orders_data2 = orders_data.fillna('N/A')
# Check if there are null values in orders_data2
orders_data2.isnull().sum()

# Drop rows with missing values in payment data
payment_data = payment_data.dropna()
# Check if there are null values in payment data
payment_data.isnull().sum()


# =============================================================================
# Removing Duplicate Data
# =============================================================================

# Check for duplicates in our orders data 
orders_data.duplicated().sum()

# Remove duplicates from orders data
orders_data = orders_data.drop_duplicates()

# Check for duplicates in our payment data 
payment_data.duplicated().sum()

# Remove duplicates from payment data
payment_data = payment_data.drop_duplicates()



# =============================================================================
# Filtering the data
# =============================================================================

# Select a subset of orders data based on the order status
invoiced_order_data = orders_data[orders_data['order_status'] == 'invoiced']
# Reset the Index
invoiced_order_data = invoiced_order_data.reset_index(drop=True) 

# Selet a subset of payment data where payment type = credit card and payment value > 1000
credit_card_payments_data = payment_data[
    (payment_data['payment_type'] == 'credit_card') & 
    (payment_data['payment_value'] > 1000)
    ]

# Select a subset of customers based on customer state = SP
customer_data_state = customers_data[customers_data['customer_state'] == 'SP']


# =============================================================================
# Merge and Join Dataframes
# =============================================================================

# Merge orders data with payment data on order_id column 
merged_data = pd.merge(orders_data, payment_data, on = 'order_id')

# Join the merged data with our customer data on the customer_id column
joined_data = pd.merge(merged_data, customers_data, on='customer_id')


# =============================================================================
# Data Visualization
# =============================================================================

# Create a field called month_year from order_purchase_timestamp
joined_data['month_year'] = joined_data['order_purchase_timestamp'].dt.to_period('M')
joined_data['week_year'] = joined_data['order_purchase_timestamp'].dt.to_period('W')
joined_data['year'] = joined_data['order_purchase_timestamp'].dt.to_period('Y')

grouped_data = joined_data.groupby('month_year')['payment_value'].sum()
grouped_data = grouped_data.reset_index()

# Convert month_year data type from period to string otherwise plot function will give an error
# TypeError: float() argument must be a string or a real number, not 'Period'
grouped_data['month_year'] = grouped_data['month_year'].astype(str)


# Creating a plot
plt.plot(grouped_data['month_year'], grouped_data['payment_value'], color='red', marker='o')
plt.ticklabel_format(useOffset=False, style='plain', axis='y')
plt.xlabel('Month and Year')    
plt.ylabel('payment value')
plt.title('Payment value by month and year')
plt.xticks(rotation=90, fontsize =8)
plt.yticks(fontsize=8)


# Scatter Plot

# we are aggregating payment value and payment installment by customer id to 
# check how much customer has paid (high payment values) in how many installments 
  
# Create the Dataframe
scatter_df = joined_data.groupby('customer_id').agg({'payment_value': 'sum', 'payment_installments': 'sum'})

plt.scatter(scatter_df['payment_value'], scatter_df['payment_installments'])
plt.xlabel('Payment Value')
plt.ylabel('Payment Installments')
plt.title('Payment Value vs Installments by customer')
plt.show()

# Seaborn plot is more aesthetic than matplotlib plot and seaborn is built on
# matplotlib and it gives more formatting options than matplotlib 

# Using seaborn to create a scatter plot 

sns.set_theme(style='darkgrid') # whitegrid, darkgrid, dark, white

sns.scatterplot(data = scatter_df, x='payment_value', y='payment_installments')
plt.xlabel('Payment Value')
plt.ylabel('Payment Installments')
plt.title('Payment Value vs Installments by customer')
plt.show()

# To visualize the payment value by payment type for each month 
# we are using Bar Chart and will use groupby and pivot function 
# so that each payment type is a column and each month is a row 

# Creating a Bar chart

bar_chart_df = joined_data.groupby(['payment_type', 'month_year'])['payment_value'].sum()
bar_chart_df = bar_chart_df.reset_index()

pivot_data = bar_chart_df.pivot(index='month_year', columns='payment_type', values='payment_value')

pivot_data.plot(kind='bar', stacked='True')
plt.ticklabel_format(useOffset=False, style='plain', axis='y')
plt.xlabel('month of payment')
plt.ylabel('Payment Value')
plt.title('payment per payment type by month ')


# To visualize the range of payment value by payment type we will use Box Plot

# Creating a Box Plot

payment_values = joined_data['payment_value']
payment_types = joined_data['payment_type']

# Creating a separate box plot per payment type
plt.boxplot(
            [payment_values[payment_types == 'credit_card'],
             payment_values[payment_types == 'boleto'],
             payment_values[payment_types == 'voucher'],
             payment_values[payment_types == 'debit_card']],
             labels = ['Credit card', 'Boleto', 'Voucher', 'Debit card']   
             )

# Set labels and titles

plt.xlabel('Payment Type')
plt.ylabel('payment Value')
plt.title('Box plot showing payment value range by payment type')

plt.show()


# To place all plots in one place we will use subplot

# Creating a subplot (3 plots in one)

fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10,10))

# ax1 which is Boxplot
ax1.boxplot(
            [payment_values[payment_types == 'credit_card'],
             payment_values[payment_types == 'boleto'],
             payment_values[payment_types == 'voucher'],
             payment_values[payment_types == 'debit_card']],
             labels = ['Credit card', 'Boleto', 'Voucher', 'Debit card']   
             )

# Set labels and titles

ax1.set_xlabel('Payment Type')
ax1.set_ylabel('payment Value')
ax1.set_title('Box plot showing payment value range by payment type')

# ax2 is the stacked bar chart

pivot_data.plot(kind='bar', stacked='True', ax=ax2)
ax2.ticklabel_format(useOffset=False, style='plain', axis='y')

# Set labels and titles
ax2.set_xlabel('month of payment')
ax2.set_ylabel('Payment Value')
ax2.set_title('payment per payment type by month ')

# ax3 is a scatter plot
ax3.scatter(scatter_df['payment_value'], scatter_df['payment_installments'])

# Set labels and titles
ax3.set_xlabel('Payment Value')
ax3.set_ylabel('Payment Installments')
ax3.set_title('Payment Value vs Installments by customer')

fig.tight_layout()

plt.savefig('my_plot.png')






























































































































































































































