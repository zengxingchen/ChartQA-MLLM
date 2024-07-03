
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Original data in a list of dictionaries
data = [
    {'Vegetable': 'Tomatoes', 'Price per lb - Jan': 1.89, 'Price per lb - Feb': 2.05, 'Price per lb - Mar': 1.75, 'Price per lb - Apr': 1.99},
    {'Vegetable': 'Cucumbers', 'Price per lb - Jan': 0.99, 'Price per lb - Feb': 1.1, 'Price per lb - Mar': 0.85, 'Price per lb - Apr': 0.95},
    {'Vegetable': 'Bell Peppers', 'Price per lb - Jan': 2.5, 'Price per lb - Feb': 2.75, 'Price per lb - Mar': 2.4, 'Price per lb - Apr': 2.6},
    {'Vegetable': 'Carrots', 'Price per lb - Jan': 1.2, 'Price per lb - Feb': 1.25, 'Price per lb - Mar': 1.15, 'Price per lb - Apr': 1.22},
    {'Vegetable': 'Onions', 'Price per lb - Jan': 0.7, 'Price per lb - Feb': 0.85, 'Price per lb - Mar': 0.65, 'Price per lb - Apr': 0.75},
    {'Vegetable': 'Zucchini', 'Price per lb - Jan': 1.3, 'Price per lb - Feb': 1.45, 'Price per lb - Mar': 1.25, 'Price per lb - Apr': 1.35},
    {'Vegetable': 'Lettuce', 'Price per lb - Jan': 1.0, 'Price per lb - Feb': 1.15, 'Price per lb - Mar': 0.95, 'Price per lb - Apr': 1.05}
]

# Convert the list of dictionaries to a pandas DataFrame
df = pd.DataFrame(data)

# Melt the DataFrame to long format
df_long = df.melt(id_vars='Vegetable', var_name='Month', value_name='Price')

# Now we can plot the bar chart
sns.set_theme(style="whitegrid")  # Set the theme for Seaborn

plt.figure(figsize=(12, 8))  # Set the figure size
bar_plot = sns.barplot(
    x='Vegetable', 
    y='Price', 
    hue='Month',  # Include different bars for each month
    data=df_long, 
    palette='muted',  # Set the color palette
    edgecolor='black'  # Add edge color to each bar for better distinction
)

# Enhance the visualization with labels and title
plt.xlabel('Vegetable', fontdict={'size': 14})
plt.ylabel('Price per lb', fontdict={'size': 14})
plt.title('Vegetable Prices per Pound Over Four Months', fontdict={'size': 16})

# Display the plot
plt.show()