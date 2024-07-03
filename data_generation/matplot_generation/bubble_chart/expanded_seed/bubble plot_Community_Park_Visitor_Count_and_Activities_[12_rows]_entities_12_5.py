
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
from datetime import datetime

# Data provided
data = [
    {'Date': '2023-01-01', 'Park Name': 'Lakeview Park', 'Visitor Count': 500, 'Percentage Attending Events': '5%', 'Percentage Using Playground': '20%', 'Percentage Picnicking': '35%'},
    # ... (other data points)
    {'Date': '2023-01-12', 'Park Name': 'Maplewood Park', 'Visitor Count': 550, 'Percentage Attending Events': '6%', 'Percentage Using Playground': '25%', 'Percentage Picnicking': '38%'}
]

# Convert data into a DataFrame
df = pd.DataFrame(data)

# Convert Date to datetime and percentages to floats
df['Date'] = pd.to_datetime(df['Date'])
df['Percentage Attending Events'] = df['Percentage Attending Events'].str.rstrip('%').astype('float') / 100
df['Percentage Using Playground'] = df['Percentage Using Playground'].str.rstrip('%').astype('float')
df['Percentage Picnicking'] = df['Percentage Picnicking'].str.rstrip('%').astype('float')

# Create bubble chart
fig, ax = plt.subplots(figsize=(15, 8))

# Sort by Date to prevent any misalignment
df = df.sort_values(by='Date')

# List of unique parks to assign unique y-coordinates
parks = df['Park Name'].unique()
y_positions = range(len(parks))

# Dictionary to map park names to y-coordinates
park_to_y = dict(zip(parks, y_positions))

# Plot each data point
for i, row in df.iterrows():
    x = row['Date']
    y = park_to_y[row['Park Name']]
    size = row['Visitor Count']  # Adjust the size scaling factor as needed
    color = row['Percentage Picnicking']  # The color value can be scaled differently if required

    ax.scatter(x, y, s=size, alpha=0.5, cmap='viridis', c=color, label=f"{row['Park Name']}: {row['Percentage Picnicking']}% Picnicking")

# Formatting
ax.set_yticks(y_positions)
ax.set_yticklabels(parks)
ax.xaxis.set_major_locator(mdates.DayLocator(interval=1))  # One day interval
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.xticks(rotation=45)
plt.xlabel('Date')
plt.ylabel('Park Name')
plt.title('Visitor Counts and Picnicking Percentage at Different Parks over Time')
plt.grid(True)
plt.colorbar(plt.cm.ScalarMappable(cmap='viridis'), ax=ax, label='Percentage Picnicking')
plt.show()