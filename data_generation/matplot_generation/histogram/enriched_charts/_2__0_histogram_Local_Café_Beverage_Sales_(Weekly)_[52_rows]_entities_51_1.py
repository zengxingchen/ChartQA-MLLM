import matplotlib.pyplot as plt

# Data points
distances = [
    102, 56, 89, 134, 189, 78, 123, 45, 67, 98, 156, 189, 172, 93, 134, 56, 143,
    187, 167, 78, 102, 156, 189, 167, 93, 124, 57, 143, 178, 134, 56, 102, 189,
    189, 78, 123, 167, 142, 67, 89, 134, 167, 156, 124, 189, 123, 56, 134, 143,
    189, 124, 78, 123, 167, 187, 145, 98, 156, 167, 145, 123, 189, 124, 167, 98,
    56, 187, 143, 124, 123, 78, 143, 167, 134, 123, 145, 156, 167, 102, 123, 124,
    167, 143, 156, 189, 124, 145, 167, 78, 134, 143, 156, 167, 124, 145, 167, 124,
    78, 98, 145
]

# Set up the figure size and resolution
plt.figure(figsize=(12, 8), dpi=100)

# Create histogram, switch to vertical bar
plt.hist(distances, bins=20, color='#FF6347', rwidth=0.85)

# Customize the histogram
plt.title('Distribution of Running Distances in a Marathon', fontsize=14, pad=20)
plt.xlabel('Distance (km)', fontsize=12)
plt.ylabel('Frequency', fontsize=12)

# Show the histogram
plt.show()