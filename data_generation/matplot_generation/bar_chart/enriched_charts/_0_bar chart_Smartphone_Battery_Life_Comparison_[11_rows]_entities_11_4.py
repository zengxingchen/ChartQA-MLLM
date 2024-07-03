
import matplotlib.pyplot as plt

# Monthly average temperature data
months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]
avg_temperature_c = [-2, 0, 5, 11, 16, 20, 22, 21, 17, 11, 5, -1]

# Color scheme using specific color codes for each month
colors = [
    '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
    '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf',
    '#1f77b4', '#ff7f0e'
]

# Create horizontal bar chart
plt.figure(figsize=(10, 8))  # Width and height of the chart
plt.barh(months, avg_temperature_c, color=colors, height=0.6)  # Bar color and band height

# Set the title and labels
plt.title('Average Monthly Temperatures')
plt.xlabel('Temperature (°C)')
plt.ylabel('Month')

# Display the bar chart
plt.show()