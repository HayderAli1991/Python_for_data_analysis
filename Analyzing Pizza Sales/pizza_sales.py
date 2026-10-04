#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Converted from Jupyter Notebook: notebook.ipynb
Conversion Date: 2025-11-27T06:13:55.712Z
"""

# # Pizza Sales Analysis


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
import plotly.express as px


# ## Import Raw Data


data =pd.read_csv("C:path/pizza_sales.csv")
df =pd.DataFrame(data)
print(df)

# ## Meta Data of Raw Data


df =pd.DataFrame(data)
print(df)

df.head(5)

print(df.isnull().sum())

print("The metadata of the dataset : " ,df.shape)

print("The rows of the dataset : " ,df.shape[0])

print("The columns of the dataset : " ,df.shape[1])

df.columns

df.info()

# ## Data Types In Raw Data


df.dtypes

df.describe()

# ## KPIs


total_revenue = df['total_price'].sum()
total_pizzas_sold = df['quantity'].sum()
total_orders = df['order_id'].nunique()
avg_order_value = total_revenue / total_orders
avg_pizzas_per_order = total_pizzas_sold / total_orders
print(f"Total Revenue : ${total_revenue:,.2f}")
print(f"Total Pizzas Sold : {total_pizzas_sold:,}")
print(f"Total Orders : {total_orders:,}")
print(f"Average Order Value : ${avg_order_value:,.2f}")
print(f"Average Pizzas Per Order : {avg_pizzas_per_order:.2f}")


# ## Charts


# #### Ingredient Analysis


df['pizza_ingredients'] = df['pizza_ingredients'].astype(str)

ingredient = (
    df['pizza_ingredients']
    .str.split(',')
    .explode()
    .str.strip()
    .value_counts()
    .reset_index()
    .rename(columns={'index': 'Count', 'pizza_ingredients': 'Ingredients'})
)



print(ingredient)


# ## Daily Trends


# #### Daily Trends - Total Orders


import pandas as pd
import matplotlib.pyplot as plt


df["order_date"] = pd.to_datetime(df["order_date"], dayfirst=True)

df["day_name"] = df["order_date"].dt.day_name()

daily_orders = (
    df.groupby("day_name")["order_id"]
    .nunique()
    .reset_index()
    .rename(columns={"order_id": "Total_Orders"})
)

day_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

daily_orders["day_name"] = pd.Categorical(
    daily_orders["day_name"],
    categories=day_order,
    ordered=True
)

daily_orders = daily_orders.sort_values("day_name")

plt.figure(figsize=(12, 5))
bars = plt.bar(daily_orders["day_name"], daily_orders["Total_Orders"], color='green')

for i, val in enumerate(daily_orders["Total_Orders"]):
    plt.text(i, val + 20, str(val), ha='center', va='bottom', fontsize=9, fontweight='bold')

plt.title("Total Orders by Day of Week")
plt.xlabel("Day of Week")
plt.ylabel("Number of Orders")
plt.xticks(rotation=45)

plt.show()


# #### Daily Trends - Total Revenue


import pandas as pd
import matplotlib.pyplot as plt


df["order_date"] = pd.to_datetime(df["order_date"], dayfirst=True)

df["day_name"] = df["order_date"].dt.day_name()

daily_orders = (
    df.groupby("day_name")["total_price"].sum()
    .reset_index()
    .rename(columns={"total_price": "Total_Revenue"})
)

day_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

daily_orders["day_name"] = pd.Categorical(
    daily_orders["day_name"],
    categories=day_order,
    ordered=True
)

daily_orders = daily_orders.sort_values("day_name")

plt.figure(figsize=(12, 5))
bars = plt.bar(daily_orders["day_name"], daily_orders["Total_Revenue"], color='purple')

for i, val in enumerate(daily_orders["Total_Revenue"]):
    label = f"${val:,.0f}" 
    plt.text(i, val + 20, label, ha='center', va='bottom', fontsize=9, fontweight='bold', )

plt.title("Total Revenue by Day of Week")
plt.xlabel("Day of Week")
plt.ylabel("Total of Revenue")
plt.xticks(rotation=45)

plt.show()

# #### Daily Trends - Total Quantity


import pandas as pd
import matplotlib.pyplot as plt


df["order_date"] = pd.to_datetime(df["order_date"], dayfirst=True)

df["day_name"] = df["order_date"].dt.day_name()

daily_orders = (
    df.groupby("day_name")["quantity"]
    .sum()
    .reset_index()
    .rename(columns={"quantity": "Total_Quantity"})
)

day_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

daily_orders["day_name"] = pd.Categorical(
    daily_orders["day_name"],
    categories=day_order,
    ordered=True
)

daily_orders = daily_orders.sort_values("day_name")

plt.figure(figsize=(12, 5))
bars = plt.bar(daily_orders["day_name"], daily_orders["Total_Quantity"], color='blue')

for i, val in enumerate(daily_orders["Total_Quantity"]):
    plt.text(i, val + 20, str(val), ha='center', va='bottom', fontsize=9, fontweight='bold')

plt.title("Total Quantity by Day of Week")
plt.xlabel("Day of Week")
plt.ylabel("Number of Quantity")
plt.xticks(rotation=45)

plt.show()


# ## Hourly Trends


# #### Hourly Trends - Total Orders


import pandas as pd
import matplotlib.pyplot as plt

df["order_time"] = pd.to_datetime(df["order_time"], format='%H:%M:%S')

df["hour"] = df["order_time"].dt.strftime("%I %p")

hourly_orders = (
    df.groupby("hour")["order_id"]
    .nunique()
    .reset_index()
    .rename(columns={"order_id": "Total_Orders"})
)


plt.figure(figsize=(12, 5))
bars = plt.bar(hourly_orders["hour"], hourly_orders["Total_Orders"], color='maroon')

for i, val in enumerate(hourly_orders["Total_Orders"]):
    plt.text(i, val + 5, str(val),
             ha='center', va='bottom', fontsize=9, fontweight='bold')

plt.title("Total Orders by Hour of Day")
plt.xlabel("Hour (24-Hour Format)")
plt.ylabel("Number of Orders")
plt.xticks(rotation=0)

plt.show()

# print(hourly_orders)

# #### Hourly Trends - Total Quantity


import pandas as pd
import matplotlib.pyplot as plt

df["order_time"] = pd.to_datetime(df["order_time"], format='%H:%M:%S')

df["hour"] = df["order_time"].dt.strftime("%I %p")

hourly_quantity = (
    df.groupby("hour")["quantity"]
    .sum()
    .reset_index()
    .rename(columns={"quantity": "Total_Quantity"})
)


plt.figure(figsize=(12, 5))
bars = plt.bar(hourly_quantity["hour"], hourly_quantity["Total_Quantity"], color='Yellow')

for i, val in enumerate(hourly_quantity["Total_Quantity"]):
    plt.text(i, val + 5, str(val),
             ha='center', va='bottom', fontsize=9, fontweight='bold')

plt.title("Total Quantity by Hour of Day")
plt.xlabel("Hour (24-Hour Format)")
plt.ylabel("Total Quantity")
plt.xticks(rotation=0)

plt.show()

# print(hourly_orders)

# ## Monthly Trends


# #### Monthly Trends - Total Orders


import pandas as pd
import matplotlib.pyplot as plt


df["order_date"] = pd.to_datetime(df["order_date"], dayfirst=True)

df["month_name"] = df["order_date"].dt.month_name()

month_order = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

df["month_name"] = pd.Categorical(
    df["month_name"],
    categories=month_order,
    ordered=True
)
monthly_orders = (
    df.groupby("month_name", observed = False)["order_id"]
    .nunique()
    .reset_index()
    .rename(columns={"order_id": "Total_Orders"})
)

# print(monthly_orders)

plt.figure(figsize=(15, 6))
bars = plt.plot(monthly_orders["month_name"], monthly_orders["Total_Orders"], color='black', linewidth = 2, marker = "o")
plt.fill_between(
    monthly_orders["month_name"],
    monthly_orders["Total_Orders"],
    color='lightgreen',
    alpha=0.4
)

for i, val in enumerate(monthly_orders["Total_Orders"]):
    plt.text(i, val + 5, str(val), ha='center', va='bottom', fontsize=9, fontweight='bold')

plt.title("Total Orders by Month")
plt.xlabel("Months")
plt.ylabel("Number of Orders")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()


# ## Percentage % of Sales By category


category_sales = (
    df.groupby("pizza_category", observed=False)["total_price"]
    .sum()
    .reset_index()
    .rename(columns={"total_price": "Total_Sales"})
)

category_sales["Percentage"] = (
    category_sales["Total_Sales"] / category_sales["Total_Sales"].sum()
) * 100

category_sales = category_sales.sort_values("Percentage", ascending=False).reset_index(drop=True)

print(category_sales)


import matplotlib.pyplot as plt

plt.figure(figsize=(8,6))
plt.pie(
    category_sales["Percentage"],
    labels=category_sales["pizza_category"],
    autopct='%1.1f%%',
    startangle=90,
    colors=plt.cm.Set3.colors,
    wedgeprops= {'edgecolor':'black', 'width':0.5}
)
plt.title("Percentage of Total Sales by Pizza Category", fontsize=14, fontweight='bold')
plt.show()


# ## Percentage % Sales By Pizza Size & category


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df["order_date"] = pd.to_datetime(df["order_date"], dayfirst=True)

df["month_name"] = df["order_date"].dt.month_name()

heatmap_data = df.pivot_table(
    index="pizza_category",        
    columns="pizza_size",      
    values="total_price",           
    aggfunc="sum",
    fill_value = 0
)
sales_pct = heatmap_data / heatmap_data.sum().sum()*100

plt.figure(figsize=(14, 6))
sns.heatmap(
    sales_pct,
    annot=True,
    fmt='.1f',
    cmap="YlGnBu",
    linewidths=.5
)

plt.title("Percentage % Sales By Pizza Size & category", fontsize=14)
plt.xlabel("Pizza Size")
plt.ylabel("Pizza Category")

plt.tight_layout()
plt.show()


# ## Total pizza sold by pizza category


import pandas as pd
import matplotlib.pyplot as plt

category_sales = df.groupby("pizza_category")["quantity"].sum().reset_index()
category_sales = category_sales.rename(columns={"quantity": "Total_Pizzas_Sold"})

plt.figure(figsize=(7, 5))
plt.bar(category_sales["pizza_category"], category_sales["Total_Pizzas_Sold"])

plt.title("Total Pizzas Sold by Category")
plt.xlabel("Pizza Category")
plt.ylabel("Total Pizzas Sold")

for i, val in enumerate(category_sales["Total_Pizzas_Sold"]):
    plt.text(i, val + 5, str(val),
             ha='center', va='bottom', fontsize=9, fontweight='bold')

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# ## Top 5 Best-Selling Pizzas - Total Quantity


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

top_pizzas = (
    df.groupby("pizza_name")["quantity"]
    .sum()                
    .reset_index()
    .rename(columns={"quantity": "Total_Orders"})
    .sort_values(by="Total_Orders", ascending=False)
    .head(5)                  
)

plt.figure(figsize=(10, 5))
sns.barplot(
    data=top_pizzas,
    x="pizza_name",
    y="Total_Orders",
    hue="pizza_name",          
    palette="YlGnBu",
    legend=False
)

plt.title("Top 5 Best-Selling Pizzas (Total Quantity)")
plt.xlabel("Pizza Name")
plt.ylabel("Total Quantity sold")
plt.xticks(rotation=45, ha="right")

for i, val in enumerate(top_pizzas["Total_Orders"]):
    plt.text(i, val + 5, str(val),
             ha='center', va='bottom', fontsize=9, fontweight='bold')

plt.tight_layout()
plt.show()


# ## Top 5 Pizzas-Ordered - Total Orders


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

top_pizzas = (
    df.groupby("pizza_name")["order_id"]
    .nunique()                
    .reset_index()
    .rename(columns={"order_id": "Total_Orders"})
    .sort_values(by="Total_Orders", ascending=False)
    .head(5)                  
)

plt.figure(figsize=(10, 5))
sns.barplot(
    data=top_pizzas,
    x="pizza_name",
    y="Total_Orders",         
    color = "grey",
    legend=False
)

plt.title("Top 5 Pizzas-Ordered (Total Orders)")
plt.xlabel("Pizza Name")
plt.ylabel("Total Orders")
plt.xticks(rotation=45, ha="right")

for i, val in enumerate(top_pizzas["Total_Orders"]):
    plt.text(i, val + 5, str(val),
             ha='center', va='bottom', fontsize=9, fontweight='bold')

plt.tight_layout()
plt.show()


# ## Top 5 Best-Selling Pizzas - Total Sales


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

top_pizzas = (
    df.groupby("pizza_name")["total_price"]
    .sum()                
    .reset_index()
    .rename(columns={"total_price": "Total_Orders"})
    .sort_values(by="Total_Orders", ascending=False)
    .head(5)                  
)

plt.figure(figsize=(10, 5))
sns.barplot(
    data=top_pizzas,
    x="pizza_name",
    y="Total_Orders",         
    color="pink",
    legend=False
)

plt.title("Top 5 Best-Selling Pizzas (Total Sales)")
plt.xlabel("Pizza Name")
plt.ylabel("Total Orders")
plt.xticks(rotation=45, ha="right")

for i, val in enumerate(top_pizzas["Total_Orders"]):
    plt.text(i, val + 5, str(val),
             ha='center', va='bottom', fontsize=9, fontweight='bold')

plt.tight_layout()
plt.show()


# ## Bottom 5 Least-Selling Pizzas (Total Quantity)


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

bottom_pizzas = (
    df.groupby("pizza_name")["quantity"]
    .sum()
    .reset_index()
    .rename(columns={"quantity": "Total_Orders"})
    .sort_values(by="Total_Orders", ascending=True)
    .head(5)
)

plt.figure(figsize=(10, 5))
sns.barplot(
    data=bottom_pizzas,
    x="pizza_name",
    y="Total_Orders",
    hue="pizza_name",
    palette="YlGnBu",
    legend=False
)

plt.title("Bottom 5 Least-Selling Pizzas (Total Quantity)")
plt.xlabel("Pizza Name")
plt.ylabel("Total Quantity Sold")
plt.xticks(rotation=45, ha="right")

for i, val in enumerate(bottom_pizzas["Total_Orders"]):
    plt.text(i, val + 2, str(val),
             ha='center', va='bottom',
             fontsize=9, fontweight='bold')

plt.tight_layout()
plt.show()


# ## Bottom 5 Pizzas (Total Orders)


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

bottom_pizzas = (
    df.groupby("pizza_name")["order_id"]
    .nunique()
    .reset_index()
    .rename(columns={"order_id": "Total_Orders"})
    .sort_values(by="Total_Orders", ascending=True)
    .head(5)
)

plt.figure(figsize=(10, 5))
sns.barplot(
    data=bottom_pizzas,
    x="pizza_name",
    y="Total_Orders",
    color="grey",
    legend=False
)

plt.title("Bottom 5 Pizzas-Ordered (Total Orders)")
plt.xlabel("Pizza Name")
plt.ylabel("Total Orders")
plt.xticks(rotation=45, ha="right")

for i, val in enumerate(bottom_pizzas["Total_Orders"]):
    plt.text(i, val + 1, str(val),
             ha='center', va='bottom',
             fontsize=9, fontweight='bold')

plt.tight_layout()
plt.show()


# ## Bottom 5 Least-Selling Pizzas - Total Sales


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

bottom_pizzas = (
    df.groupby("pizza_name")["total_price"]
    .sum()                
    .reset_index()
    .rename(columns={"total_price": "Total_Orders"})
    .sort_values(by="Total_Orders", ascending=True)
    .head(5)                  
)

plt.figure(figsize=(10, 5))
sns.barplot(
    data=bottom_pizzas,
    x="pizza_name",
    y="Total_Orders",         
    color="pink",
    legend=False
)

plt.title("Bottom 5 Best-Selling Pizzas (Total Sales)")
plt.xlabel("Pizza Name")
plt.ylabel("Total Orders")
plt.xticks(rotation=45, ha="right")

for i, val in enumerate(bottom_pizzas["Total_Orders"]):
    plt.text(i, val + 5, str(val),
             ha='center', va='bottom', fontsize=9, fontweight='bold')

plt.tight_layout()
plt.show()