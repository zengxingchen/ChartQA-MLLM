
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

# Prepare the data in a DataFrame
data = {
    'Region': ['North America', 'South America', 'Europe', 'Africa', 'Asia', 'Australia', 'Antarctica'],
    'Renewable Energy': [40, 50, 60, 55, 45, 50, 30],
    'Non-Renewable Energy': [35, 30, 25, 35, 40, 35, 50],
    'Nuclear Energy': [25, 20, 15, 10, 15, 15, 20],
}
df = pd.DataFrame(data)
df.set_index('Region', inplace=True)

# Calculate the percentage
df_percentage = df.div(df.sum(axis=1), axis=0)

# Start the stacked bar plot
sns.set(style="whitegrid")

# Define the figure size
plt.figure(figsize=(14, 10))

# Create the vertical bar chart
df_percentage.plot(kind='bar', stacked=True, color=["#2E8B57", "#8B0000", "#4682B4"], width=0.5)

# Modify the y-axis labels to display as percentages
formatter = FuncFormatter(lambda y, pos: "%d%%" % (y * 100))
plt.gca().yaxis.set_major_formatter(formatter)

# Customizing the plot (title, labels, legend)
plt.title('Energy Sources Distribution by Region', fontsize=20, pad=20)
plt.xlabel('Region', fontsize=16)
plt.ylabel('Percentage', fontsize=16)

# Adjust legend
plt.legend(title='Energy Sources', bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)

plt.tight_layout()
plt.show()