
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Given chart table data
data = [
    {'Month': 'January', 'Tomatoes': 0, 'Lettuce': 12, 'Carrots': 15, 'Strawberries': 0},
    {'Month': 'February', 'Tomatoes': 0, 'Lettuce': 15, 'Carrots': 10, 'Strawberries': 0},
    {'Month': 'March', 'Tomatoes': 0, 'Lettuce': 20, 'Carrots': 13, 'Strawberries': 0},
    {'Month': 'April', 'Tomatoes': 8, 'Lettuce': 25, 'Carrots': 0, 'Strawberries': 2},
    {'Month': 'May', 'Tomatoes': 12, 'Lettuce': 30, 'Carrots': 0, 'Strawberries': 8},
    {'Month': 'June', 'Tomatoes': 20, 'Lettuce': 35, 'Carrots': 0, 'Strawberries': 15},
    {'Month': 'July', 'Tomatoes': 30, 'Lettuce': 40, 'Carrots': 0, 'Strawberries': 25}
]

# Create a DataFrame
df = pd.DataFrame(data)

# Melt the DataFrame to long format
df_melted = df.melt(id_vars=['Month'], var_name='Type', value_name='Amount')

# Initialize the figure
plt.figure(figsize=(10, 6))

# Define a dictionary that maps types to markers
marker_dict = {'Tomatoes': 'o', 'Lettuce': 'X', 'Carrots': '^', 'Strawberries': 's'}

# Define a list of unique types to set hue order
type_order = df_melted['Type'].unique()

# Create a scatterplot
sns.scatterplot(
    data=df_melted,
    x='Month',
    y='Amount',
    hue='Type',        # Different colors for different types
    style='Type',      # Different markers for different types
    markers=marker_dict,    # The actual marker styles
    hue_order=type_order,    # Order of appearance in the legend
    palette='deep',    # Color palette to use
    s=100              # Size of the markers
)

# Customize the axes and title
plt.title('Monthly Amount of Different Vegetables/Fruits')
plt.xlabel('Month')
plt.ylabel('Amount')

# Adjust legend
plt.legend(title='Type')

# Show the plot
plt.show()