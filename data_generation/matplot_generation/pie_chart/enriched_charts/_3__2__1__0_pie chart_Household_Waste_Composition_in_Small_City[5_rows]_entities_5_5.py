
import matplotlib.pyplot as plt

# Data to plot
labels = ['Innovation', 'Startups', 'Funding', 'Marketing', 'Management', 'Networking', 'Other']
sizes = [35.0, 20.0, 15.0, 10.0, 8.0, 7.0, 5.0]
colors = ['#ff6f69', '#ffcc5c', '#88d8b0', '#6b5b95', '#d64161', '#feb236', '#4f6457']

# Plot
fig1, ax1 = plt.subplots(figsize=(10, 6))
ax1.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)

ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('Distribution of Business & Entrepreneurship Topics in 2023', pad=20)
plt.show()