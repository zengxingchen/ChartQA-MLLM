
import matplotlib.pyplot as plt

# Data
categories = ['Adventure Travel', 'Beach Holidays', 'Cultural Tours', 'Cruise Holidays', 
              'Safari', 'Skiing', 'City Breaks', 'Other']
percentages = [25, 20, 15, 10, 8, 5, 12, 5]
colors = ['#ff6347', '#4682b4', '#32cd32', '#ffd700', '#8a2be2', '#ff4500', '#40e0d0', '#da70d6']

# Plotting the pie chart
fig, ax = plt.subplots(figsize=(12, 9))
ax.pie(percentages, labels=categories, autopct='%1.1f%%', startangle=140, colors=colors)
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Setting the title
plt.title("Distribution of Travel Preferences in 2022", pad=30)

# Display the chart
plt.show()