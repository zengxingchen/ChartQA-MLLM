
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Provided data
data = [
    {'Appliance': 'Refrigerator', 'January': 150, 'Kitchen Usage': 50, 'January.1': 160, 'Living Room Usage': 55, 'February': np.nan, 'Kitchen Usage.1': np.nan, 'February.1': np.nan, 'Living Room Usage.1': np.nan},
    {'Appliance': 'Microwave', 'January': 30, 'Kitchen Usage': 0, 'January.1': 35, 'Living Room Usage': 0, 'February': np.nan, 'Kitchen Usage.1': np.nan, 'February.1': np.nan, 'Living Room Usage.1': np.nan},
    {'Appliance': 'Oven', 'January': 40, 'Kitchen Usage': 5, 'January.1': 45, 'Living Room Usage': 10, 'February': np.nan, 'Kitchen Usage.1': np.nan, 'February.1': np.nan, 'Living Room Usage.1': np.nan},
    {'Appliance': 'Television', 'January': 0, 'Kitchen Usage': 70, 'January.1': 0, 'Living Room Usage': 75, 'February': np.nan, 'Kitchen Usage.1': np.nan, 'February.1': np.nan, 'Living Room Usage.1': np.nan},
    {'Appliance': 'Washing Machine', 'January': 90, 'Kitchen Usage': 0, 'January.1': 95, 'Living Room Usage': 0, 'February': np.nan, 'Kitchen Usage.1': np.nan, 'February.1': np.nan, 'Living Room Usage.1': np.nan}
]

# Convert to DataFrame
df = pd.DataFrame(data)

# Extract relevant data
appliances = df['Appliance']
january_kitchen_usage = df['Kitchen Usage']
january_living_room_usage = df['Living Room Usage']
january_total = df['January'] + df['January.1']

# Create a figure and a set of subplots
fig, ax = plt.subplots(figsize=(10, 8))

# Define bar width
bar_width = 0.35

# Calculate positions for each appliance bar
indices = np.arange(len(january_total))

# Stack bars for kitchen and living room usage on top of each other
plt.bar(indices, january_kitchen_usage, bar_width, label='Kitchen Usage', color='skyblue', edgecolor='black')
plt.bar(indices, january_living_room_usage, bar_width, bottom=january_kitchen_usage, label='Living Room Usage', color='lightgreen', edgecolor='black')

# Add some text for labels, title, and custom x-axis tick labels, etc.
ax.set_xlabel('Appliance')
ax.set_ylabel('Usage')
ax.set_title('Appliance Usage for January')
ax.set_xticks(indices)
ax.set_xticklabels(appliances)
ax.legend()

# Add data labels above the bars
for i, v in enumerate(january_total):
    ax.text(i, v + 3, str(v), color='black', ha='center')

# Rotate the x-axis labels if needed
plt.xticks(rotation=45)

# Show the plot
plt.tight_layout()
plt.show()