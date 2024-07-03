
import matplotlib.pyplot as plt

# Data
energy_sources = ['Solar Power', 'Wind Energy', 'Hydropower', 'Geothermal', 'Biomass', 'Other']
market_share = [35, 25, 20, 10, 5, 5]
colors = ['#FFD700', '#00BFFF', '#7FFFD4', '#FF69B4', '#8A2BE2', '#FF4500']

# Plotting the pie chart
fig, ax = plt.subplots(figsize=(10, 8))
ax.pie(market_share, labels=energy_sources, autopct='%1.1f%%', startangle=90, colors=colors)
ax.axis('equal')

# Setting the title
plt.title("Renewable Energy Source Market Share in 2023", y=1.05)

# Display the chart
plt.show()