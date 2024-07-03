
import matplotlib.pyplot as plt

# Data from the chart table
data = [
    {'Platform': 'Facebook', 'Time Spent (Hours)': 8.0},
    {'Platform': 'Instagram', 'Time Spent (Hours)': 6.0},
    {'Platform': 'Twitter', 'Time Spent (Hours)': 4.0},
    {'Platform': 'YouTube', 'Time Spent (Hours)': 7.0},
    {'Platform': 'TikTok', 'Time Spent (Hours)': 5.0},
    {'Platform': 'LinkedIn', 'Time Spent (Hours)': 1.0},
    {'Platform': 'Snapchat', 'Time Spent (Hours)': 2.0},
    {'Platform': 'Pinterest', 'Time Spent (Hours)': 1.5},
    {'Platform': 'Reddit', 'Time Spent (Hours)': 3.0},
    {'Platform': 'WhatsApp', 'Time Spent (Hours)': 3.5},
    {'Platform': 'Telegram', 'Time Spent (Hours)': 2.0}
]

# Prepare the data for the pie chart
platforms = [entry['Platform'] for entry in data]
time_spent = [entry['Time Spent (Hours)'] for entry in data]
colors = plt.cm.Paired(range(len(data)))  # Using a colormap for diversity in colors
explode = [0.1 if entry['Time Spent (Hours)'] == max(time_spent) else 0.0 for entry in data]  # Explode the largest slice

# Create the pie chart
plt.figure(figsize=(10, 8))  # Size of the figure
plt.pie(time_spent, labels=platforms, autopct='%1.1f%%', startangle=140, colors=colors, explode=explode, shadow=True)

# Optional: Add a title and adjust font size
plt.title('Time Spent on Various Social Media Platforms (in Hours)', fontsize=14)

# Show the pie chart
plt.show()