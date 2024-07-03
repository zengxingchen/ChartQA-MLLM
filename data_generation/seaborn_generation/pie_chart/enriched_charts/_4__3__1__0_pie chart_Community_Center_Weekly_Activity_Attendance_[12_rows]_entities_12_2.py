
import matplotlib.pyplot as plt

# Data setup
categories = ['Renewable Energy', 'Non-Renewable Energy', 'Nuclear Energy', 'Hydropower', 'Geothermal']
percentages = [40, 30, 10, 15, 5]
colors = ['#ff6347', '#4682b4', '#32cd32', '#ff7f50', '#dda0dd']

# Plotting
fig, ax = plt.subplots(figsize=(12, 8))  # width and height of the chart
ax.pie(percentages, labels=categories, autopct='%1.1f%%', colors=colors, startangle=140)
ax.set_title('Energy Sources Distribution in 2024', pad=20)

# Show plot
plt.show()