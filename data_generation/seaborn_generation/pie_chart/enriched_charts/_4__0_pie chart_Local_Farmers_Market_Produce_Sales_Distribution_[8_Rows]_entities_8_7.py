
import matplotlib.pyplot as plt

# Data
activities = ["Sleeping", "Working", "Exercise", "Leisure", "Household Chores", "Commuting", "Eating", "Other"]
hours_per_week = [56, 40, 7, 14, 10, 5, 10, 6]

# Colors
colors = [
    "#1f77b4",  # Sleeping
    "#ff7f0e",  # Working
    "#2ca02c",  # Exercise
    "#d62728",  # Leisure
    "#9467bd",  # Household Chores
    "#8c564b",  # Commuting
    "#e377c2",  # Eating
    "#7f7f7f",  # Other
]

# Create pie chart
plt.figure(figsize=(10, 8))  # width and height in inches
plt.pie(hours_per_week, labels=activities, colors=colors, autopct='%1.1f%%', startangle=140)

# Chart title
plt.title('Weekly Time Allocation for Various Activities', pad=30)

# Show plot
plt.show()