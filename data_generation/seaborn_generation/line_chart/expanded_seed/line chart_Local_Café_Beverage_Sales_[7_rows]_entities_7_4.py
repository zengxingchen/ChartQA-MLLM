
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Given data
data = [
    {'Date': '2023-02-01', 'Americano': 35, 'Latte': 42, 'Cappuccino': 30, 'Espresso': 25},
    {'Date': '2023-02-02', 'Americano': 40, 'Latte': 45, 'Cappuccino': 25, 'Espresso': 20},
    {'Date': '2023-02-03', 'Americano': 50, 'Latte': 55, 'Cappuccino': 33, 'Espresso': 22},
    {'Date': '2023-02-04', 'Americano': 60, 'Latte': 60, 'Cappuccino': 40, 'Espresso': 30},
    {'Date': '2023-02-05', 'Americano': 55, 'Latte': 65, 'Cappuccino': 35, 'Espresso': 28},
    {'Date': '2023-02-06', 'Americano': 45, 'Latte': 40, 'Cappuccino': 32, 'Espresso': 27},
    {'Date': '2023-02-07', 'Americano': 47, 'Latte': 39, 'Cappuccino': 34, 'Espresso': 26}
]

# Convert to DataFrame
df = pd.DataFrame(data)

# Convert DataFrame to long format
df_long = df.melt(id_vars='Date', var_name='CoffeeType', value_name='Sales')

# Convert Date to datetime
df_long['Date'] = pd.to_datetime(df_long['Date'])

# Set plot style
sns.set_theme(style="whitegrid")

# Create the lineplot
plt.figure(figsize=(12, 6))
lineplot = sns.lineplot(
    x='Date',
    y='Sales',
    hue='CoffeeType',
    style='CoffeeType',
    markers=True,
    dashes=False,
    data=df_long
)

# Customize the plot with title and labels
plt.title('Coffee Sales Over Time')
plt.xlabel('Date')
plt.ylabel('Number of Coffees Sold')
plt.legend(title='Coffee Type')

# Show the plot
plt.show()