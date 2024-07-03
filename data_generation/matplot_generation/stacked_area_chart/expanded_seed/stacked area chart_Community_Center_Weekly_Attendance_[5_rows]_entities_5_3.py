
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.dates import DateFormatter

# Your data
data = [
    {'Date': '2023-03-01', 'Yoga Class': 25, 'Cooking Workshop': 10, 'Tech Support Hour': 15, 'Art Club': 8, 'Book Reading Event': 12},
    {'Date': '2023-03-08', 'Yoga Class': 22, 'Cooking Workshop': 15, 'Tech Support Hour': 17, 'Art Club': 11, 'Book Reading Event': 9},
    {'Date': '2023-03-15', 'Yoga Class': 30, 'Cooking Workshop': 12, 'Tech Support Hour': 14, 'Art Club': 14, 'Book Reading Event': 15},
    {'Date': '2023-03-22', 'Yoga Class': 28, 'Cooking Workshop': 18, 'Tech Support Hour': 20, 'Art Club': 7, 'Book Reading Event': 13},
    {'Date': '2023-03-29', 'Yoga Class': 35, 'Cooking Workshop': 20, 'Tech Support Hour': 22, 'Art Club': 10, 'Book Reading Event': 11}
]

# Convert the data into a Pandas DataFrame
df = pd.DataFrame(data)

# Convert the 'Date' column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Set the 'Date' column as the index of the DataFrame
df.set_index('Date', inplace=True)

# Plotting the stacked area chart
fig, ax = plt.subplots(figsize=(10, 6))

activities = ['Yoga Class', 'Cooking Workshop', 'Tech Support Hour', 'Art Club', 'Book Reading Event']
colors = ['#ff9999','#66b3ff','#99ff99','#ffd700','#c2c2f0']  # Different color for each activity

# Create the stacked area plot
df.plot(kind='area', stacked=True, ax=ax, color=colors)

# Set the title and labels
ax.set_title('Attendance of Events Over Time', fontdict={'fontsize': 16})
ax.set_xlabel('Date')
ax.set_ylabel('Number of Attendees')

# Improve formatting of the x-axis dates
date_form = DateFormatter("%b %d")
ax.xaxis.set_major_formatter(date_form)

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Add a legend to the plot
ax.legend(activities, loc='upper left')

# Show the plot
plt.tight_layout()
plt.show()