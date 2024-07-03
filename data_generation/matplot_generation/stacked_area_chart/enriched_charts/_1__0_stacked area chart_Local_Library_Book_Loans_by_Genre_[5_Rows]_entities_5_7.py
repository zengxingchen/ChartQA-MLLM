
import matplotlib.pyplot as plt

# Define the data
years = list(range(2011, 2023))
running = [20000, 22000, 24000, 26000, 30000, 35000, 40000, 45000, 50000, 55000, 60000, 65000]
swimming = [15000, 16000, 17000, 18000, 20000, 22000, 25000, 28000, 32000, 35000, 37000, 39000]
cycling = [10000, 12000, 14000, 16000, 18000, 21000, 24000, 27000, 30000, 33000, 36000, 38000]

# Start plotting
fig, ax = plt.subplots(figsize=(12, 8))

# Plot stacked area chart
ax.stackplot(years, running, swimming, cycling, colors=['#1E90FF', '#32CD32', '#FFD700'])

# Annotate specific points
ax.annotate('Surge in Running Activities', xy=(2020, 55000), xytext=(2015, 70000),
            arrowprops=dict(facecolor='#1E90FF', shrink=0.05))

# Add labels and title
plt.xlabel('Year')
plt.ylabel('Number of People')
plt.title('Engagement in Physical Activities (2011-2022)', pad=20)

# Show the plot
plt.show()