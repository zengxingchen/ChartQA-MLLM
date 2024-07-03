
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

# Prepare the data in a DataFrame
data = {
    'Category': ['Asia', 'Europe', 'Africa', 'North America', 'South America', 'Australia', 'Antarctica', 'Arctic', 'Oceania', 'Middle East'],
    'Value1': [0.6, 0.5, 0.4, 0.3, 0.4, 0.5, 0.2, 0.3, 0.4, 0.5],
    'Value2': [0.2, 0.3, 0.4, 0.5, 0.3, 0.2, 0.4, 0.3, 0.2, 0.3],
    'Value3': [0.2, 0.2, 0.2, 0.2, 0.3, 0.3, 0.4, 0.4, 0.4, 0.2],
}
df = pd.DataFrame(data)
df.set_index('Category', inplace=True)

# Calculate the percentage
df_percentage = df.div(df.sum(axis=1), axis=0)

# Start the stacked bar plot
sns.set(style="whitegrid")

# Define the figure size
plt.figure(figsize=(10, 8))

# Create the vertical bar chart
df_percentage.plot(kind='bar', stacked=True, color=["#FF5733", "#33FF57", "#3357FF"], width=0.7)

# Modify the y-axis labels to display as percentages
formatter = FuncFormatter(lambda y, pos: "%d%%" % (y * 100))
plt.gca().yaxis.set_major_formatter(formatter)

# Customizing the plot (title, labels, legend)
plt.title('Distribution of Travel Destinations by Region', fontsize=16, pad=20)
plt.xlabel('Region', fontsize=14)
plt.ylabel('Percentage', fontsize=14)

# Adjust legend
plt.legend(title='Preferences', bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)

plt.tight_layout()
plt.show()