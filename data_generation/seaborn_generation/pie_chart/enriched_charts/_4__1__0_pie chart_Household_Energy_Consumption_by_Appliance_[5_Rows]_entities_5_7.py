
import matplotlib.pyplot as plt

# Data
sources = ['Solar', 'Wind', 'Hydropower', 'Geothermal', 'Biomass', 'Ocean', 'Others']
percentages = [28.7, 25.4, 22.1, 9.3, 7.8, 4.2, 2.5]

# Colors
colors = ['#FF6347', '#4682B4', '#32CD32', '#FFD700', '#8A2BE2', '#FF7F50', '#B22222']

# Plot
plt.figure(figsize=(10, 7))  # Width and height of the chart
plt.pie(percentages, labels=sources, colors=colors, startangle=140, autopct='%1.1f%%')

plt.title("Sources of Renewable Energy in 2023", y=1.05)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()