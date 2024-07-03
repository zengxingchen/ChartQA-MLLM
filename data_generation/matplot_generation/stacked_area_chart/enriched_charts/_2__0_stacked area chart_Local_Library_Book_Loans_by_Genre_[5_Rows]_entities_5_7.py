
import matplotlib.pyplot as plt

# Define the data
years = list(range(2011, 2022))
beaches = [50000, 52000, 54000, 56000, 59000, 63000, 68000, 75000, 82000, 65000, 70000]
museums = [30000, 31000, 32000, 34000, 37000, 40000, 43000, 47000, 52000, 55000, 60000]
nature_reserves = [20000, 22000, 25000, 28000, 31000, 34000, 38000, 42000, 47000, 50000, 55000]

# Start plotting
fig, ax = plt.subplots(figsize=(12, 8))

# Plot stacked area chart
ax.stackplot(years, beaches, museums, nature_reserves, colors=['#FF5733', '#33C1FF', '#75FF33'])

# Annotate specific points
ax.annotate('Surge in Beach Visits', xy=(2019, 82000), xytext=(2015, 90000),
            arrowprops=dict(facecolor='#FF5733', shrink=0.05))

# Add labels and title
plt.xlabel('Year')
plt.ylabel('Number of Visitors')
plt.title('Tourist Visits to Attractions (2011-2021)', pad=20)

# Show the plot
plt.show()