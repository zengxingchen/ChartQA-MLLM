
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Data preparation
data = {
    'Date': pd.date_range(start='2020-01-01', periods=24, freq='M'),
    'Investment': [15000, 17000, 16500, 18000, 20000, 21000, 19500, 22000, 23000, 25000, 24000, 26000,
                   28000, 27000, 29000, 30000, 32000, 31000, 33000, 35000, 34000, 36000, 37000, 38000]
}

df = pd.DataFrame(data)

# Plotting
plt.figure(figsize=(12, 8))
sns.set(style="whitegrid")

# Create the area chart
area_plot = sns.lineplot(x='Date', y='Investment', data=df, color='#1f77b4', linewidth=2)
area_plot.fill_between(df['Date'], df['Investment'], color='#1f77b4', alpha=0.3)

# Adding title and labels
plt.title('Investment Over Time in Future Technologies', fontsize=16, loc='left')
plt.xlabel('Date', fontsize=14)
plt.ylabel('Investment Amount ($)', fontsize=14)

# Adding annotation
max_investment_date = df.loc[df['Investment'].idxmax(), 'Date']
max_investment_value = df['Investment'].max()
plt.annotate('Highest Investment', xy=(max_investment_date, max_investment_value),
             xytext=(max_investment_date, max_investment_value + 5000),
             arrowprops=dict(facecolor='black', arrowstyle='->'),
             fontsize=12, color='black')

plt.tight_layout()
plt.show()