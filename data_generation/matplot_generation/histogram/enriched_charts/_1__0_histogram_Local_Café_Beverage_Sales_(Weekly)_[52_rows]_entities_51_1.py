import matplotlib.pyplot as plt

# Data points
weights = [
    70, 80, 75, 85, 90, 95, 100, 60, 65, 70, 75, 80, 85, 90, 95, 100, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 
    50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 
    40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 
    30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 
    20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 
    10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 
    1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100
]

# Set up the figure size and resolution
plt.figure(figsize=(12, 8), dpi=100)

# Create histogram with vertical bars
plt.hist(weights, bins=20, color='#FF6347', orientation='vertical', rwidth=0.85)

# Customize the histogram
plt.title('Weight Distribution of a Sample Population')
plt.xlabel('Weight')
plt.ylabel('Frequency')

# Show the histogram
plt.show()