
import matplotlib.pyplot as plt

# Define the data
years = list(range(2011, 2023))
gdp = [15000, 15500, 16000, 17000, 17500, 18000, 18500, 19000, 19500, 20000, 20500, 21000]
growth = [2000, 2100, 2200, 2300, 2400, 2500, 2600, 2700, 2800, 2900, 3000, 3100]
inflation = [300, 320, 340, 360, 380, 400, 420, 440, 460, 480, 500, 520]

# Start plotting
fig, ax = plt.subplots(figsize=(14, 10))

# Plot stacked area chart
ax.stackplot(years, gdp, growth, inflation, colors=['#1f77b4', '#ff7f0e', '#2ca02c'], labels=['GDP', 'Growth', 'Inflation'])

# Annotate specific points
ax.annotate('Inflation Peak', xy=(2022, 520), xytext=(2017, 700),
            arrowprops=dict(facecolor='#2ca02c', shrink=0.05))

# Add labels and title
plt.xlabel('Year')
plt.ylabel('Economic Indicators')
plt.title('Economic Indicators (2011-2022)', pad=40)
plt.legend(loc='upper left')

# Show the plot
plt.show()