
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

# Prepare the data in a DataFrame
data = {
    'Category': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'],
    'Temperature': [0.25, 0.1, 0.4, 0.35, 0.2, 0.5, 0.15, 0.3, 0.4, 0.25],
    'Precipitation': [0.5, 0.6, 0.2, 0.4, 0.5, 0.3, 0.7, 0.3, 0.4, 0.35],
    'Humidity': [0.25, 0.3, 0.4, 0.25, 0.3, 0.2, 0.15, 0.4, 0.2, 0.4],
}
df = pd.DataFrame(data)
df.set_index('Category', inplace=True)

# Calculate the percentage
df_percentage = df.div(df.sum(axis=1), axis=0)

# Start the stacked bar plot
sns.set(style="whitegrid")

# Define the figure size
plt.figure(figsize=(12, 10))

# Create the vertical bar chart
df_percentage.plot(kind='bar', stacked=True, color=["#1f77b4", "#ff7f0e", "#2ca02c"], width=0.6)

# Modify the y-axis labels to display as percentages
formatter = FuncFormatter(lambda y, pos: "%d%%" % (y * 100))
plt.gca().yaxis.set_major_formatter(formatter)

# Customizing the plot (title, labels, legend)
plt.title('Climate Parameters by Category', fontsize=16)
plt.xlabel('Category', fontsize=14)
plt.ylabel('Percentage', fontsize=14)

# Adjust legend
plt.legend(title='Climate Parameters', bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)

plt.tight_layout()
plt.show()