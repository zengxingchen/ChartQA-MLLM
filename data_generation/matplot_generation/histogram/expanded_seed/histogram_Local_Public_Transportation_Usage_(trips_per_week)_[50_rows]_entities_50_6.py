
import matplotlib.pyplot as plt

# Table data provided
data = [
    {'Week Number': 1, ' Public Transport Trips': 95},
    {'Week Number': 2, ' Public Transport Trips': 102},
    {'Week Number': 3, ' Public Transport Trips': 110},
    {'Week Number': 4, ' Public Transport Trips': 87},
    {'Week Number': 5, ' Public Transport Trips': 103},
    {'Week Number': 6, ' Public Transport Trips': 120},
    {'Week Number': 7, ' Public Transport Trips': 98},
    {'Week Number': 8, ' Public Transport Trips': 112},
    {'Week Number': 9, ' Public Transport Trips': 90},
    {'Week Number': 10, ' Public Transport Trips': 105},
    {'Week Number': 11, ' Public Transport Trips': 123},
    {'Week Number': 12, ' Public Transport Trips': 110},
    {'Week Number': 13, ' Public Transport Trips': 99},
    {'Week Number': 14, ' Public Transport Trips': 121},
    {'Week Number': 15, ' Public Transport Trips': 115}
]

# Extract 'Public Transport Trips' into a list
trips = [entry[' Public Transport Trips'] for entry in data]

# Calculate the mean of the trips for annotation
mean_trips = sum(trips) / len(trips)

# Create a histogram
plt.hist(trips, bins=range(min(trips), max(trips) + 10, 5), color='skyblue', edgecolor='black')

# Add a title and labels
plt.title('Distribution of Public Transport Trips')
plt.xlabel('Number of Trips')
plt.ylabel('Frequency')

# Draw a vertical line for the mean
plt.axvline(mean_trips, color='red', linestyle='dashed', linewidth=1)
# Add a text annotation for the mean
plt.text(mean_trips + 2, 1, f'Mean: {mean_trips:.2f}', color='red')

# Add a grid
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Display the plot
plt.show()