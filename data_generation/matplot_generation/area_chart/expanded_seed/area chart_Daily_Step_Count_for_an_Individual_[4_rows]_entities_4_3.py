
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.dates import DateFormatter

# Data
data = [
    {'Date': '2023-04-01', 'Steps': 7500},
    {'Date': '2023-04-02', 'Steps': 5300},
    {'Date': '2023-04-03', 'Steps': 9200},
    {'Date': '2023-04-04', 'Steps': 11000}
]

# Convert the data into a pandas DataFrame
df = pd.DataFrame(data)

# Convert 'Date' column to datetime type
df['Date'] = pd.to_datetime(df['Date'])

# Sort the DataFrame by date to ensure correct plotting
df.sort_values('Date', inplace=True)

# Set 'Date' column as the index of the DataFrame
df.set_index('Date', inplace=True)

# Create an area chart
fig, ax = plt.subplots(figsize=(10, 6))  # Create a figure and axis with a custom figure size

# Plot the 'Steps' column as an area chart
ax.fill_between(df.index, df['Steps'], step='mid', color='skyblue', alpha=0.4)  # Define the color and opacity

# Enhance formatting and style
ax.set_title('Daily Steps Over Time', fontsize=16)  # Title of the plot
ax.set_xlabel('Date', fontsize=12)  # X-axis label
ax.set_ylabel('Number of Steps', fontsize=12)  # Y-axis label
ax.grid(True, which='major', linestyle='--', linewidth=0.5)  # Add gridlines for readability
ax.tick_params(axis='both', which='major', labelsize=10)  # Format the tick labels

# Rotate and align the x-axis tick labels
fig.autofmt_xdate()

# Set date format on x-axis
date_form = DateFormatter("%Y-%m-%d")
ax.xaxis.set_major_formatter(date_form)

plt.tight_layout()  # Adjust the plot to ensure everything fits without overlapping
plt.show()  # Display the plot