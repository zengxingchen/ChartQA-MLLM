
import matplotlib.pyplot as plt

# Data setup
continents = ['Europe', 'Asia', 'North America', 'South America', 'Africa', 'Oceania', 'Antarctica']
tourists_percentage = [35, 30, 15, 7, 5, 4, 4]
colors = ['#FF9999', '#66B2FF', '#99FF99', '#FFCC99', '#FFD700', '#8A2BE2', '#00FF00']

# Plotting
fig, ax = plt.subplots(figsize=(12, 7))  # width and height of the chart
ax.pie(tourists_percentage, labels=continents, autopct='%1.1f%%', colors=colors, startangle=90)
ax.set_title('Percentage of Tourists Visiting Different Continents', pad=20)

# Show plot
plt.show()