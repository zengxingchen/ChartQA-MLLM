
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

# Prepare the data in a DataFrame
data = {
    'Topic': ['Romanticism', 'Modernism', 'Postmodernism', 'Realism', 'Surrealism', 'Expressionism', 'Classicism', 'Impressionism', 'Renaissance', 'Baroque'],
    'Value1': [0.5, 0.4, 0.3, 0.2, 0.4, 0.3, 0.6, 0.3, 0.2, 0.4],
    'Value2': [0.3, 0.4, 0.4, 0.5, 0.2, 0.3, 0.2, 0.4, 0.4, 0.3],
    'Value3': [0.2, 0.2, 0.3, 0.3, 0.4, 0.4, 0.2, 0.3, 0.4, 0.3],
}
df = pd.DataFrame(data)
df.set_index('Topic', inplace=True)

# Calculate the percentage
df_percentage = df.div(df.sum(axis=1), axis=0)

# Start the stacked bar plot
sns.set(style="whitegrid")

# Define the figure size
plt.figure(figsize=(12, 10))

# Create the vertical bar chart
df_percentage.plot(kind='bar', stacked=True, color=["#4CAF50", "#FF9800", "#2196F3"], width=0.6)

# Modify the y-axis labels to display as percentages
formatter = FuncFormatter(lambda y, pos: "%d%%" % (y * 100))
plt.gca().yaxis.set_major_formatter(formatter)

# Customizing the plot (title, labels, legend)
plt.title('Distribution of Art Movements Across Different Topics', fontsize=16)
plt.xlabel('Art Movement', fontsize=14)
plt.ylabel('Percentage', fontsize=14)

# Adjust legend
plt.legend(title='Values', bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)

plt.tight_layout()
plt.show()