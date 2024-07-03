
import matplotlib.pyplot as plt

# Define the data
years = list(range(2011, 2023))
meditation = [5000, 5500, 6000, 6200, 6500, 7000, 7500, 8000, 8500, 9000, 9500, 10000]
yoga = [8000, 8200, 8600, 9000, 9500, 10000, 10500, 11000, 12000, 13000, 14000, 15000]
aerobics = [10000, 12000, 14000, 16000, 18000, 20000, 22000, 24000, 26000, 28000, 30000, 32000]

# Start plotting
fig, ax = plt.subplots(figsize=(14, 10))

# Plot stacked area chart
ax.stackplot(years, meditation, yoga, aerobics, colors=['#FF6347', '#4682B4', '#8A2BE2'])

# Annotate specific points
ax.annotate('Surge in Aerobics', xy=(2020, 28000), xytext=(2015, 40000),
            arrowprops=dict(facecolor='#8A2BE2', shrink=0.05))

# Add labels and title
plt.xlabel('Year')
plt.ylabel('Number of People Engaged')
plt.title('Engagement in Health Activities (2011-2022)', pad=30)

# Add a legend
plt.legend(['Meditation', 'Yoga', 'Aerobics'], loc='upper left')

# Show the plot
plt.show()