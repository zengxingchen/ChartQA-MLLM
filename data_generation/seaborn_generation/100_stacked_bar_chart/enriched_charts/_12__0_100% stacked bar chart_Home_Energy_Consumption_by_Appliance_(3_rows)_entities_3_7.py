
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

# Prepare the data in a DataFrame
data = {
    'Category': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'],
    'Stress': [0.5, 0.2, 0.3, 0.4, 0.6, 0.1, 0.2, 0.3, 0.4, 0.5],
    'Anxiety': [0.3, 0.4, 0.3, 0.2, 0.2, 0.5, 0.1, 0.4, 0.3, 0.2],
    'Depression': [0.2, 0.4, 0.4, 0.4, 0.2, 0.4, 0.7, 0.3, 0.3, 0.3],
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
plt.title('Prevalence of Mental Health Issues by Category', fontsize=16)
plt.xlabel('Category', fontsize=14)
plt.ylabel('Percentage', fontsize=14)

# Adjust legend
plt.legend(title='Mental Health Issues', bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)

plt.tight_layout()
plt.show()