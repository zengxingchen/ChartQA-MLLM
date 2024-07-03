
import matplotlib.pyplot as plt

# Data setup
regions = ['Asia', 'Europe', 'Africa', 'North America', 'South America', 'Oceania', 'Middle East']
users = [50, 15, 11, 10, 8, 1, 5]
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2']

# Plotting
fig, ax = plt.subplots(figsize=(10, 6))  # width and height of the chart
ax.pie(users, labels=regions, autopct='%1.1f%%', colors=colors, startangle=140)
ax.set_title('Global Internet Usage Share by Region')

# Show plot
plt.show()