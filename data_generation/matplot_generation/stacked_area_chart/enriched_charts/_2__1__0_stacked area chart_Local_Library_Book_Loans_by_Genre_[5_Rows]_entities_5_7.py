
import matplotlib.pyplot as plt

# Define the data
years = list(range(2011, 2023))
technology = [50000, 52000, 55000, 60000, 65000, 70000, 75000, 80000, 85000, 90000, 95000, 100000]
healthcare = [30000, 32000, 35000, 38000, 42000, 46000, 50000, 55000, 60000, 65000, 70000, 75000]
energy = [20000, 21000, 23000, 25000, 28000, 30000, 32000, 35000, 38000, 40000, 43000, 45000]

# Start plotting
fig, ax = plt.subplots(figsize=(14, 10))

# Plot stacked area chart
ax.stackplot(years, technology, healthcare, energy, colors=['#FF6347', '#4682B4', '#3CB371'])

# Annotate specific points
ax.annotate('Surge in Technology Investment', xy=(2020, 90000), xytext=(2015, 105000),
            arrowprops=dict(facecolor='#FF6347', shrink=0.05))

# Add labels and title
plt.xlabel('Year')
plt.ylabel('Investment (in millions)')
plt.title('Investment in Different Sectors Over Time', pad=40)

# Show the plot
plt.show()