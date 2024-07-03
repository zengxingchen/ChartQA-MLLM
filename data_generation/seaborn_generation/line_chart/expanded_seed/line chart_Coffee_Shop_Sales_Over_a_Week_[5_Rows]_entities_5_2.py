
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Your data in a list of dicts, as provided
data = [
    {'Day': 'Monday', 'Espresso': 95, 'Americano': 123, 'Caramel Latte': 58},
    {'Day': 'Tuesday', 'Espresso': 108, 'Americano': 135, 'Caramel Latte': 64},
    {'Day': 'Wednesday', 'Espresso': 120, 'Americano': 140, 'Caramel Latte': 75},
    {'Day': 'Thursday', 'Espresso': 122, 'Americano': 145, 'Caramel Latte': 60},
    {'Day': 'Friday', 'Espresso': 130, 'Americano': 160, 'Caramel Latte': 85}
]

# Convert the list of dictionaries into a pandas DataFrame
df = pd.DataFrame(data)

# Melt the DataFrame so it's in 'tidy' format
df_melted = pd.melt(df, id_vars='Day', var_name='Coffee_Type', value_name='Sales')

# Create a lineplot using Seaborn
plt.figure(figsize=(10, 6))  # Set the figure size
sns.lineplot(data=df_melted, x='Day', y='Sales', hue='Coffee_Type', marker='o')  # Lineplot with markers

# Additional plot details
plt.title('Coffee Sales Throughout the Week')
plt.xlabel('Day of the Week')
plt.ylabel('Number of Cups Sold')
plt.xticks(rotation=45)  # Rotate x-axis labels if needed
plt.legend(title='Coffee Type')
plt.tight_layout()  # Adjust layout to avoid clipping of tick-labels

# Show/save the figure
plt.show()
# plt.savefig('coffee_sales.png')  # Uncomment to save the figure as 'coffee_sales.png'