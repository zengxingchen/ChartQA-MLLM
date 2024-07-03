
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

# Your data in a list of dictionaries
data = [
    {'Month': 'January', 'Lighting': 3200, 'Machinery': 14000, 'HVAC': 5000, 'Computers': 3000},
    {'Month': 'February', 'Lighting': 2800, 'Machinery': 13000, 'HVAC': 4000, 'Computers': 2800},
    {'Month': 'March', 'Lighting': 2700, 'Machinery': 14500, 'HVAC': 4200, 'Computers': 2900},
    {'Month': 'April', 'Lighting': 2600, 'Machinery': 15000, 'HVAC': 4700, 'Computers': 2850},
    {'Month': 'May', 'Lighting': 2650, 'Machinery': 15500, 'HVAC': 5200, 'Computers': 2950},
    {'Month': 'June', 'Lighting': 2700, 'Machinery': 16000, 'HVAC': 5600, 'Computers': 3100},
    {'Month': 'July', 'Lighting': 2800, 'Machinery': 16500, 'HVAC': 6000, 'Computers': 3200},
    {'Month': 'August', 'Lighting': 2850, 'Machinery': 17000, 'HVAC': 6200, 'Computers': 3250}
]

# Converting list of dictionaries to a pandas DataFrame
df = pd.DataFrame(data)

# Set the index to 'Month' for better plotting
df.set_index('Month', inplace=True)

# Cumulative sum across rows to stack the areas
cumulative = df.cumsum(axis=1)

# Initialize the matplotlib figure
f, ax = plt.subplots(figsize=(10, 6))

# Variables for upcoming loop to build the stacked plot
colormap = sns.color_palette("husl", 4)  # Using a color palette for distinct colors
prev_data = np.zeros(len(df))

# Loop over columns to create stacked plots
for i, column in enumerate(df.columns):
    plt.fill_between(df.index, prev_data, cumulative[column], color=colormap[i], label=column)
    plt.plot(df.index, cumulative[column], color=colormap[i])
    prev_data = cumulative[column]

# Customize the plot
ax.set_ylabel('Usage')
ax.set_title('Monthly Utility Usage')
sns.despine(left=True, bottom=True)
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.legend(loc='upper left')  # Place legend in the upper left corner

plt.show()