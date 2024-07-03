
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

# Prepare the data in a DataFrame
data = {
    'Category': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'],
    'Revenue': [1500, 1800, 2000, 2200, 2500, 2700, 3000, 3200, 3400, 3600],
    'Expenses': [300, 500, 600, 800, 900, 1000, 1100, 1200, 1300, 1400],
    'Profit': [1200, 1300, 1400, 1400, 1600, 1700, 1900, 2000, 2100, 2200],
}
df = pd.DataFrame(data)
df.set_index('Category', inplace=True)

# Calculate the percentage
df_percentage = df.div(df.sum(axis=1), axis=0)

# Start the stacked bar plot
sns.set(style="whitegrid")

# Define the figure size
plt.figure(figsize=(12, 8))

# Create the vertical bar chart
df_percentage.plot(kind='bar', stacked=True, color=["#1f77b4", "#ff7f0e", "#2ca02c"], width=0.6)

# Modify the y-axis labels to display as percentages
formatter = FuncFormatter(lambda y, pos: "%d%%" % (y * 100))
plt.gca().yaxis.set_major_formatter(formatter)

# Customizing the plot (title, labels, legend)
plt.title('Financial Overview by Category', fontsize=18)
plt.xlabel('Category', fontsize=14)
plt.ylabel('Percentage', fontsize=14)

# Adjust legend
plt.legend(title='Financial Metrics', bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)

plt.tight_layout()
plt.show()