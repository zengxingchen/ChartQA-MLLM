
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

# Prepare the data in a DataFrame
data = {
    'Category': ['Category1', 'Category2', 'Category3', 'Category4', 'Category5', 'Category6', 'Category7', 'Category8', 'Category9', 'Category10'],
    'Value1': [0.25, 0.35, 0.4, 0.2, 0.5, 0.3, 0.2, 0.4, 0.3, 0.25],
    'Value2': [0.45, 0.25, 0.3, 0.5, 0.2, 0.4, 0.3, 0.4, 0.2, 0.35],
    'Value3': [0.3, 0.4, 0.3, 0.3, 0.3, 0.3, 0.5, 0.2, 0.5, 0.4],
}
df = pd.DataFrame(data)
df.set_index('Category', inplace=True)

# Calculate the percentage
df_percentage = df.div(df.sum(axis=1), axis=0)

# Start the stacked bar plot
sns.set(style="whitegrid")

# Define the figure size
plt.figure(figsize=(10, 12))

# Create the vertical bar chart
df_percentage.plot(kind='bar', stacked=True, color=["#FF6347", "#4682B4", "#32CD32"], width=0.7)

# Modify the y-axis labels to display as percentages
formatter = FuncFormatter(lambda y, pos: "%d%%" % (y * 100))
plt.gca().yaxis.set_major_formatter(formatter)

# Customizing the plot (title, labels, legend)
plt.title('Distribution of Responses Across Categories', fontsize=16)
plt.ylabel('Percentage', fontsize=14)
plt.xlabel('Category', fontsize=14)

# Adjust legend
plt.legend(title='Responses', bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)

plt.tight_layout()
plt.show()