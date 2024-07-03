
import matplotlib.pyplot as plt

# Generate data points
months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]
rainfall = [3.1, 2.9, 4.3, 3.9, 4.6, 4.0, 4.3, 4.1, 4.5, 3.8, 3.7, 3.5]

plt.figure(figsize=(12, 10))  # Change the width and height of the chart

# Create a vertical bar chart with specified bar width and colors
plt.bar(months, rainfall, color=[
    '#4CAF50', '#FFEB3B', '#FFC107', '#FF9800', '#F44336',
    '#E91E63', '#9C27B0', '#673AB7', '#3F51B5', '#2196F3',
    '#03A9F4', '#00BCD4'], width=0.5)

plt.ylabel('Average Rainfall (inches)', fontsize=14)
plt.title('Average Monthly Rainfall in New York City', fontsize=16)
plt.ylim(2.5, 5)  # Adjusted to start from 2.5 for readability

plt.tight_layout()
plt.show()