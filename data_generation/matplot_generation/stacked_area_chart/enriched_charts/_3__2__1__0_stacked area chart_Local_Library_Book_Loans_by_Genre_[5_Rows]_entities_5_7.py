
import matplotlib.pyplot as plt

# Define the data
years = list(range(2011, 2023))
running = [12000, 13000, 14000, 15000, 16000, 17000, 18000, 19000, 20000, 22000, 24000, 26000]
cycling = [8000, 8200, 8500, 9000, 9500, 10000, 10500, 11000, 11500, 12500, 13500, 14500]
swimming = [6000, 6500, 7000, 7500, 8000, 8500, 9000, 9500, 10000, 11000, 12000, 13000]

# Start plotting
fig, ax = plt.subplots(figsize=(16, 8))

# Plot stacked area chart
ax.stackplot(years, running, cycling, swimming, colors=['#FFA07A', '#20B2AA', '#9370DB'])

# Annotate specific points
ax.annotate('Increase in Running', xy=(2020, 22000), xytext=(2015, 24000),
            arrowprops=dict(facecolor='#FFA07A', shrink=0.05))

# Add labels and title
plt.xlabel('Year')
plt.ylabel('Participation')
plt.title('Participation in Different Sports Over Time', pad=40)

# Add legend
plt.legend(['Running', 'Cycling', 'Swimming'], loc='upper left')

# Show the plot
plt.show()