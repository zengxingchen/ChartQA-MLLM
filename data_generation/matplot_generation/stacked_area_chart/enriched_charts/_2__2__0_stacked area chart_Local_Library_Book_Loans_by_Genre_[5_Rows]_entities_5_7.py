
import matplotlib.pyplot as plt

# Define the data
years = list(range(2011, 2022))
running = [50, 60, 70, 80, 90, 110, 130, 150, 170, 200, 230]
cycling = [80, 85, 90, 95, 100, 105, 110, 120, 135, 150, 170]
swimming = [40, 45, 50, 55, 60, 65, 70, 80, 95, 110, 130]

# Start plotting
fig, ax = plt.subplots(figsize=(14, 8))

# Plot stacked area chart
ax.stackplot(years, running, cycling, swimming, colors=['#1f77b4', '#ff7f0e', '#2ca02c'])

# Annotate specific points
ax.annotate('Significant increase in Running', xy=(2020, 200), xytext=(2015, 150),
            arrowprops=dict(facecolor='#1f77b4', shrink=0.05))
ax.annotate('Gradual rise in Cycling', xy=(2020, 150), xytext=(2016, 190),
            arrowprops=dict(facecolor='#ff7f0e', shrink=0.05))

# Add labels and title
plt.xlabel('Year')
plt.ylabel('Participants (in thousands)')
plt.title('Annual Participation in Sports Activities (2011-2021)', pad=20)

# Show the plot
plt.show()