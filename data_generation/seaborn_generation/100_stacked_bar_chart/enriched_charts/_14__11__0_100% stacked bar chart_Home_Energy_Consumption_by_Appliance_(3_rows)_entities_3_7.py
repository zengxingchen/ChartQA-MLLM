
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

# Prepare the data in a DataFrame
data = {
    'Food': ['Apple', 'Banana', 'Chicken', 'Beef', 'Broccoli', 'Rice', 'Almonds', 'Eggs', 'Milk', 'Yogurt'],
    'Carbohydrates': [0.52, 0.23, 0.0, 0.0, 0.07, 0.28, 0.22, 0.01, 0.05, 0.07],
    'Proteins': [0.03, 0.03, 0.27, 0.26, 0.03, 0.03, 0.21, 0.13, 0.03, 0.1],
    'Fats': [0.02, 0.01, 0.14, 0.15, 0.0, 0.01, 0.5, 0.11, 0.03, 0.04],
}
df = pd.DataFrame(data)
df.set_index('Food', inplace=True)

# Calculate the percentage
df_percentage = df.div(df.sum(axis=1), axis=0)

# Start the stacked bar plot
sns.set(style="whitegrid")

# Define the figure size
plt.figure(figsize=(12, 10))

# Create the vertical bar chart
df_percentage.plot(kind='bar', stacked=True, color=["#FF4500", "#1E90FF", "#FFD700"], width=0.8)

# Modify the y-axis labels to display as percentages
formatter = FuncFormatter(lambda y, pos: "%d%%" % (y * 100))
plt.gca().yaxis.set_major_formatter(formatter)

# Customizing the plot (title, labels, legend)
plt.title('Nutritional Distribution Across Different Foods', fontsize=18)
plt.xlabel('Food', fontsize=14)
plt.ylabel('Percentage', fontsize=14)

# Adjust legend
plt.legend(title='Nutrients', bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)

plt.tight_layout()
plt.show()