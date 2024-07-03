
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Your provided data
data = [
    {'Date': '2023-03-01', 'Espresso': 34, 'Cappuccino': 45, 'Latte': 72},
    {'Date': '2023-03-02', 'Espresso': 30, 'Cappuccino': 40, 'Latte': 65},
    {'Date': '2023-03-03', 'Espresso': 25, 'Cappuccino': 35, 'Latte': 55},
    {'Date': '2023-03-04', 'Espresso': 50, 'Cappuccino': 60, 'Latte': 95},
    {'Date': '2023-03-05', 'Espresso': 45, 'Cappuccino': 55, 'Latte': 85},
    {'Date': '2023-03-06', 'Espresso': 20, 'Cappuccino': 30, 'Latte': 40},
    {'Date': '2023-03-07', 'Espresso': 55, 'Cappuccino': 65, 'Latte': 110},
    {'Date': '2023-03-08', 'Espresso': 60, 'Cappuccino': 70, 'Latte': 120},
    {'Date': '2023-03-09', 'Espresso': 65, 'Cappuccino': 75, 'Latte': 130}
]

# Convert the dictionary to a pandas DataFrame
df = pd.DataFrame(data)

# Convert 'Date' column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Melt the DataFrame to have 'coffee type' and 'amount' in separate columns
df_melted = df.melt(id_vars='Date', var_name='CoffeeType', value_name='Amount')

# Create a scatterplot
plt.figure(figsize=(10, 6))
scatterplot = sns.scatterplot(
    data=df_melted,
    x='Date',
    y='Amount',
    hue='CoffeeType',    # Different colors for different coffee types
    style='CoffeeType',  # Different markers for different coffee types
    size='Amount',       # Vary the size of points by amount
    sizes=(50, 200),     # Specify the range of sizes
    palette='viridis',   # Color palette used for hue
)

# Rotates and aligns the tick labels so they look better
plt.xticks(rotation=45)
plt.title('Coffee Sales Scatterplot')

# Show the plot
plt.show()