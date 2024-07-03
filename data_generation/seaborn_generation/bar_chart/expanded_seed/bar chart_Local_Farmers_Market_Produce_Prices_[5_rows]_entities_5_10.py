
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data
data = [
  {'Produce': 'Tomatoes', 'Price per lb ($)': 1.5, 'Market': "Farmer's Market A"},
  {'Produce': 'Cucumbers', 'Price per lb ($)': 1.0, 'Market': "Farmer's Market B"},
  {'Produce': 'Carrots', 'Price per lb ($)': 0.75, 'Market': "Farmer's Market A"},
  {'Produce': 'Apples', 'Price per lb ($)': 1.4, 'Market': "Farmer's Market C"},
  {'Produce': 'Berries', 'Price per lb ($)': 3.0, 'Market': "Farmer's Market B"}
]

# Convert data into a pandas DataFrame
df = pd.DataFrame(data)

# Start plotting
sns.set(style='whitegrid')  # Set the seaborn style

# Create the bar chart
# Diversifying by using 'hue' for different markets and a palette for colors
# Also adding error bars to demonstrate possible data variability
plt.figure(figsize=(10, 6))  # Optional: Adjusting the figure size
barplot = sns.barplot(
    x='Produce',
    y='Price per lb ($)',
    hue='Market',
    data=df,
    palette='muted',  # Change palette for a diverse color range
    ci='sd'           # Show standard deviation as error bars
)

# Customizing the plot
# Optional: Add a title and labels
plt.title('Price per Pound of Produce by Market', fontsize=16)
plt.xlabel('Produce', fontsize=14)
plt.ylabel('Price per lb ($)', fontsize=14)

# Optional: Customize legend
plt.legend(title='Market', title_fontsize='13', fontsize='11')

# Show the values on the bars for better readability
for p in barplot.patches:
    barplot.annotate(
        format(p.get_height(), '.2f'), 
        (p.get_x() + p.get_width() / 2., p.get_height()), 
        ha = 'center', 
        va = 'center', 
        xytext = (0, 9), 
        textcoords = 'offset points',
        fontsize=10
    )

# Optional: Rotate x-axis labels if they are too long
plt.xticks(rotation=45)

# Show the plot
plt.tight_layout()
plt.show()