
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Prepare the data
data = [
    {'Date': '2023-01-01', 'Espresso': 45, 'Americano': 30, 'Latte': 60, 'Cappuccino': 25},
    {'Date': '2023-01-02', 'Espresso': 50, 'Americano': 25, 'Latte': 65, 'Cappuccino': 30},
    {'Date': '2023-01-03', 'Espresso': 55, 'Americano': 35, 'Latte': 70, 'Cappuccino': 20},
    {'Date': '2023-01-04', 'Espresso': 60, 'Americano': 40, 'Latte': 80, 'Cappuccino': 25},
    {'Date': '2023-01-05', 'Espresso': 65, 'Americano': 30, 'Latte': 75, 'Cappuccino': 27}
]
df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])

# Melt the dataframe to work with seaborn's lineplot
df_melted = df.melt('Date', var_name='Coffee', value_name='Sales')

# Plotting
sns.set_theme(style="whitegrid")
plt.figure(figsize=(10, 6))
lineplot = sns.lineplot(x='Date', y='Sales', hue='Coffee', style='Coffee', markers=True, dashes=False, data=df_melted)

# Beautify the plot
plt.title('Coffee Sales over Time')
plt.xlabel('Date')
plt.ylabel('Number of Coffees Sold')
plt.legend(title='Coffee Type')
lineplot.set_xticklabels(df['Date'].dt.strftime('%Y-%m-%d'), rotation=45)
sns.despine()

# Show the plot
plt.show()