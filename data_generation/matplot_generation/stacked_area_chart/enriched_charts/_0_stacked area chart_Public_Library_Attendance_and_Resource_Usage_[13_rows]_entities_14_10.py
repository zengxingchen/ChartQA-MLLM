
import matplotlib.pyplot as plt
import pandas as pd

# Data
data = {
    'Quarter': ['Q1-2021', 'Q2-2021', 'Q3-2021', 'Q4-2021', 'Q1-2022', 'Q2-2022', 'Q3-2022', 'Q4-2022'],
    'Electronics': [15000, 20000, 18000, 22000, 16000, 21000, 19000, 23000],
    'Clothing': [10000, 15000, 12000, 17000, 11000, 16000, 13000, 18000],
    'Home Goods': [5000, 10000, 8000, 9000, 7000, 12000, 11000, 13000]
}

df = pd.DataFrame(data)

# Figure and Plot
fig, ax = plt.subplots(figsize=(10, 6))
ax.stackplot(df['Quarter'], df['Electronics'], df['Clothing'], df['Home Goods'],
             labels=['Electronics', 'Clothing', 'Home Goods'],
             colors=['#1f77b4', '#2ca02c', '#ff7f0e'])

# Title and labels
plt.title('Quarterly Sales Data')
plt.xlabel('Quarter')
plt.ylabel('Sales (in USD)')
plt.legend(loc='upper left')

# Annotations
for i, (quarter, electronics, clothing, home_goods) in enumerate(zip(df['Quarter'], df['Electronics'], df['Clothing'], df['Home Goods'])):
    total_sales = electronics + clothing + home_goods
    ax.annotate(f'Total: {total_sales}', (quarter, total_sales), textcoords="offset points", xytext=(0,10), ha='center')

# Show plot
plt.tight_layout()
plt.show()