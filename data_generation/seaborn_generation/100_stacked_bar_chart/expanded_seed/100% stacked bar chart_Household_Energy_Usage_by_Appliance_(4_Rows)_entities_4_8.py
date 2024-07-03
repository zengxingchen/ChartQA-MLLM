
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Given chart table data
data = [
    {'Appliance': 'Kitchen', 'Lighting (%)': 10, 'Refrigeration (%)': 20, 'Heating and Cooling (%)': 30, 'Electronics (%)': 10, 'Washing and Drying (%)': 30},
    {'Appliance': 'Living Room', 'Lighting (%)': 30, 'Refrigeration (%)': 10, 'Heating and Cooling (%)': 20, 'Electronics (%)': 30, 'Washing and Drying (%)': 10},
    {'Appliance': 'Bedroom', 'Lighting (%)': 40, 'Refrigeration (%)': 10, 'Heating and Cooling (%)': 10, 'Electronics (%)': 30, 'Washing and Drying (%)': 10},
    {'Appliance': 'Bathroom', 'Lighting (%)': 20, 'Refrigeration (%)': 10, 'Heating and Cooling (%)': 40, 'Electronics (%)': 20, 'Washing and Drying (%)': 10}
]

# Convert data to DataFrame
df = pd.DataFrame(data)
df.set_index('Appliance', inplace=True)

# Calculate the percentage of each category per appliance
df_percentage = df.div(df.sum(axis=1), axis=0) * 100

# Initialize the matplotlib figure
plt.figure(figsize=(10, 6))

# We need to plot each column one by one, adding them on top of each other
bottom = np.zeros(len(df))

# Custom colors for the stacked bars
colors = sns.color_palette('pastel')

# Loop through each column in DataFrame and plot
for i, col in enumerate(df.columns):
    plt.bar(df_percentage.index, df_percentage[col], bottom=bottom, label=col, color=colors[i])
    bottom += df_percentage[col]

# Add some customizations
plt.ylabel('Percentage')
plt.title('Appliance Energy Usage Breakdown (100% Stacked)')
plt.legend(title='Categories', bbox_to_anchor=(1.05, 1), loc='upper left')

# Display the plot
plt.tight_layout()
plt.show()