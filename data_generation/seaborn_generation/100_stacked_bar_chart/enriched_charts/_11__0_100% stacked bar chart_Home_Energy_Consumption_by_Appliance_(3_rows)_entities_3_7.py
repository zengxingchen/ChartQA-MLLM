
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

# Prepare the data in a DataFrame
data = {
    'Category': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'],
    'Drama': [0.45, 0.25, 0.35, 0.2, 0.4, 0.6, 0.5, 0.3, 0.4, 0.35],
    'Comedy': [0.35, 0.55, 0.3, 0.5, 0.4, 0.2, 0.25, 0.4, 0.35, 0.4],
    'Action': [0.2, 0.2, 0.35, 0.3, 0.2, 0.2, 0.25, 0.3, 0.25, 0.25],
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
plt.title('Genre Distribution Across Categories', fontsize=18)
plt.xlabel('Category', fontsize=14)
plt.ylabel('Percentage', fontsize=14)

# Adjust legend
plt.legend(title='Genres', bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)

plt.tight_layout()
plt.show()