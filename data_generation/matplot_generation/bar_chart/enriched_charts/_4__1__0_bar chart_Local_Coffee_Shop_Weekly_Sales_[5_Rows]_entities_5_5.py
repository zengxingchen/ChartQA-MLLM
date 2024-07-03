
import matplotlib.pyplot as plt

# Generate data points
categories = [
    "Reading", "Fitness", "Music", "Gaming", "Travel",
    "Cooking", "Photography", "Art", "Crafting"
]
percentages = [5.0, 10.0, 15.0, 12.0, 8.0, 7.0, 6.0, 3.0, 2.0]

plt.figure(figsize=(14, 8))  # Change the width and height of the chart

# Create a horizontal bar chart with specified bar width and colors
plt.barh(categories, percentages, color=[
    '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
    '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22'], height=0.6)

plt.xlabel('Percentage of Time Spent', fontsize=14)
plt.title('Distribution of Leisure Activities', fontsize=18, pad=20)
plt.xlim(0, 20)  # Adjusted to give some space for readability

plt.tight_layout()
plt.show()