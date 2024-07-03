
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.dates import DateFormatter

# Given chart table data
data = [
    {'Date': '2023-01-01', 'Adult Fiction': 120, 'Adult Non-Fiction': 150, 'Young Adult': 80, "Children's Books": 200},
    {'Date': '2023-01-02', 'Adult Fiction': 115, 'Adult Non-Fiction': 145, 'Young Adult': 85, "Children's Books": 190},
    # ... (include all data points)
    {'Date': '2023-01-12', 'Adult Fiction': 135, 'Adult Non-Fiction': 165, 'Young Adult': 85, "Children's Books": 220}
]

# Create a DataFrame
df = pd.DataFrame(data)

# Convert the 'Date' column to a datetime object
df['Date'] = pd.to_datetime(df['Date'])

# Plotting
fig, ax = plt.subplots(figsize=(12, 6))

# Plot each category with distinct styles
ax.plot(df['Date'], df['Adult Fiction'], label='Adult Fiction', marker='o', linestyle='-', color='blue')
ax.plot(df['Date'], df['Adult Non-Fiction'], label='Adult Non-Fiction', marker='^', linestyle='--', color='green')
ax.plot(df['Date'], df['Young Adult'], label='Young Adult', marker='x', linestyle='-.', color='red')
ax.plot(df['Date'], df["Children's Books"], label="Children's Books", marker='s', linestyle=':', color='purple')

# Setting the date format on the x-axis
date_form = DateFormatter("%m-%d")
ax.xaxis.set_major_formatter(date_form)

# Adding titles and labels
plt.title('Book Sales Data Over Time')
plt.xlabel('Date')
plt.ylabel('Number of Books Sold')

# Enabling the legend
plt.legend()

# Display grid
plt.grid(True)

# Rotate x-axis labels for readability
plt.xticks(rotation=45)

# Tight layout for padding
plt.tight_layout()

# Show the plot
plt.show()