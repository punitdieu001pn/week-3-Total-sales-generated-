# ------------------------------
# SALES DATA ANALYSIS PROJECT
# ------------------------------

import pandas as pd
import os

# Step 1: Load Data
df = pd.read_csv('Data/sales_data.csv')
print("Dataset Preview:\n", df.head())

# Step 2: Clean Data
df = df.drop_duplicates()

if 'Total_Sales' not in df.columns:
    df['Total_Sales'] = df['Quantity'] * df['Price']
else:
    df['Total_Sales'] = df['Total_Sales'].fillna(df['Quantity'] * df['Price'])

# Step 3: Sales Analysis
total_revenue = df['Total_Sales'].sum()
best_product = df.groupby('Product')['Total_Sales'].sum().idxmax()
avg_order_value = df['Total_Sales'].mean()
sales_count = df['Product'].value_counts()
revenue_by_product = df.groupby('Product')['Total_Sales'].sum()

# Step 4: Generate Report
report = f"""
📊 SALES REPORT
-----------------------------
💰 Total Revenue: ₹{total_revenue:,.2f}
🏆 Best Selling Product: {best_product}
📎 Average Order Value: ₹{avg_order_value:,.2f}

Sales Count By Product:
{sales_count.to_string()}

Revenue By Product:
{revenue_by_product.to_string()}
"""

# Step 5: Save Report
os.makedirs('output', exist_ok=True)

with open('output/sales_report.txt', 'w', encoding='utf-8') as f:
    f.write(report)

print(report)
print("✅ Report Saved Successfully!")
