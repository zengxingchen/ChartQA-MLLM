
import matplotlib.pyplot as plt
import pandas as pd

# Your data
data = [
    {'Month': 'January', 'Espresso': 1500, 'Brewed Coffee': 2000, 'Tea': 500, 'Pastries': 800, 'Sandwiches': 600},
    {'Month': 'February', 'Espresso': 1800, 'Brewed Coffee': 1900, 'Tea': 550, 'Pastries': 760, 'Sandwiches': 650},
    {'Month': 'March', 'Espresso': 1600, 'Brewed Coffee': 2100, 'Tea': 600, 'Pastries': 850, 'Sandwiches': 700},
    {'Month': 'April', 'Espresso': 1700, 'Brewed Coffee': 2000, 'Tea': 650, 'Pastries': 900, 'Sandwiches': 750},
    {'Month': 'May', 'Espresso': 2000, 'Brewed Coffee': 2200, 'Tea': 700, 'Pastries': 950, 'Sandwiches': 800},
    {'Month': 'June', 'Espresso': 1700, 'Brewed Coffee': 2100, 'Tea': 750, 'Pastries': 870, 'Sandwiches': 850},
    {'Month': 'July', 'Espresso': 1650, 'Brewed Coffee': 2150, 'Tea': 800, 'Pastries': 830, 'Sandwiches': 900}
]

df = pd.DataFrame(data)
# Ensure the order of the months is consistent
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July']
df.set_index('Month', inplace=True)
df = df.reindex(months)

# Create the bar stacks
bottoms = df.iloc[:, 0].cumsum() - df.iloc[:, 0]
for i, col in enumerate(df.columns):
    plt.bar(
        df.index, df[col], 
        bottom=None if i == 0 else bottoms, 
        label=col
    )
    if i != 0: # Update bottoms for the next series
        bottoms += df[col]

# Adding the aesthetics
plt.title('Sales Data of the Coffee Shop (Stacked Bar Chart)')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.xticks(rotation=45) # To prevent overlapping month names

# Add grid lines for better readability
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Make sure everything fits without overlapping
plt.tight_layout()

# Legend - place it outside the axes
plt.legend(title='Product', bbox_to_anchor=(1.05, 1), loc='upper left')

# Display the plot
plt.show()