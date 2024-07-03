
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data preparation
data = {
    'Category': ['Education', 'Healthcare', 'Transport', 'Entertainment', 'Food', 'Clothing', 'Housing', 'Utilities', 'Savings', 'Miscellaneous'],
    'Average_Expenditure': [1500, 1200, 800, 500, 900, 600, 1300, 400, 700, 300]
}

df = pd.DataFrame(data)

# Plotting
plt.figure(figsize=(12, 8))
sns.barplot(x='Category', y='Average_Expenditure', data=df, palette=["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b", "#e377c2", "#7f7f7f", "#bcbd22", "#17becf"], linewidth=1.2)

# Customize the chart
plt.title('Average Monthly Expenditure by Category', fontsize=18, pad=20)
plt.xlabel('Category', fontsize=14)
plt.ylabel('Average Expenditure (USD)', fontsize=14)
plt.xticks(rotation=45)
plt.grid(axis='x')

# Show the plot
plt.show()