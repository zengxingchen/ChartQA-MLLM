
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data given in the form of a list of dictionaries
data = [
    {'Day': 'Monday', 'Espresso': 45, 'Americano': 30, 'Cappuccino': 25, 'Latte': 50},
    {'Day': 'Tuesday', 'Espresso': 50, 'Americano': 45, 'Cappuccino': 20, 'Latte': 60},
    {'Day': 'Wednesday', 'Espresso': 60, 'Americano': 50, 'Cappuccino': 30, 'Latte': 70},
    {'Day': 'Thursday', 'Espresso': 55, 'Americano': 35, 'Cappuccino': 40, 'Latte': 65},
    {'Day': 'Friday', 'Espresso': 70, 'Americano': 60, 'Cappuccino': 50, 'Latte': 80}
]

# Converting the list of dictionaries to a pandas DataFrame
df = pd.DataFrame(data)

# Reshape the data so that it's in long form for Seaborn
df_long = pd.melt(df, id_vars='Day', var_name='Coffee_Type', value_name='Sales')

# Create a line plot with Seaborn
plt.figure(figsize=(10, 6))
sns.lineplot(data=df_long, x='Day', y='Sales', hue='Coffee_Type', style='Coffee_Type', markers=True, dashes=False)

# Customize the plot with titles and labels
plt.title('Coffee Sales Throughout the Week')
plt.xlabel('Day of the Week')
plt.ylabel('Number of Coffees Sold')
plt.legend(title='Coffee Type')

# Show the plot
plt.show()