
import matplotlib.pyplot as plt

# Monthly average rainfall data
months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]
avg_rainfall_mm = [78, 72, 85, 92, 102, 110, 120, 115, 105, 98, 90, 80]

# Color scheme using specific color codes for each month
colors = [
    '#ff6347', '#4682b4', '#3cb371', '#ffa500', '#8a2be2',
    '#5f9ea0', '#ff69b4', '#d2691e', '#6495ed', '#daa520',
    '#ff4500', '#2e8b57'
]

# Create vertical bar chart
plt.figure(figsize=(12, 6))  # Width and height of the chart
plt.bar(months, avg_rainfall_mm, color=colors, width=0.5)  # Bar color and band width

# Set the title and labels
plt.title('Average Monthly Rainfall', pad=20)
plt.xlabel('Month')
plt.ylabel('Rainfall (mm)')
plt.ylim(60, 130)  # Set y-axis limits to start from 60

# Display the bar chart
plt.show()