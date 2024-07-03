
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

# Prepare the data in a DataFrame
data = {
    'Category': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'],
    'Value1': [0.4, 0.2, 0.4, 0.3, 0.6, 0.5, 0.1, 0.2, 0.3, 0.1],
    'Value2': [0.3, 0.1, 0.5, 0.3, 0.2, 0.6, 0.4, 0.2, 0.1, 0.5],
    'Value3': [0.1, 0.4, 0.3, 0.2, 0.5, 0.1, 0.2, 0.6, 0.5, 0.4],
}
df = pd.DataFrame(data)
df.set_index('Category', inplace=True)

# Calculate the percentage
df_percentage = df.div(df.sum(axis=1), axis=0)

# Start the stacked bar plot
sns.set(style="whitegrid")

# Define the figure size
plt.figure(figsize=(14, 8))

# Create the horizontal bar chart
df_percentage.plot(kind='barh', stacked=True, color=["#FFA07A", "#20B2AA", "#778899"], width=0.8)

# Modify the y-axis labels to display as percentages
formatter = FuncFormatter(lambda y, pos: "%d%%" % (y * 100))
plt.gca().xaxis.set_major_formatter(formatter)

# Customizing the plot (title, labels, legend)
plt.title('Distribution of Values Across Different Categories', fontsize=16)
plt.xlabel('Percentage', fontsize=14)
plt.ylabel('Category', fontsize=14)

# Adjust legend
plt.legend(title='Values', bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)

plt.tight_layout()
plt.show()