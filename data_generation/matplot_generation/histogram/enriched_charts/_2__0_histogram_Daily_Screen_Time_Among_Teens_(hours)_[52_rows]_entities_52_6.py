
import matplotlib.pyplot as plt

# Data points
data = [
    25, 45, 67, 23, 56, 78, 49, 58, 63, 79, 85, 92, 68, 73, 80, 59, 43, 65, 87, 90, 
    54, 72, 64, 55, 62, 74, 84, 83, 76, 77, 81, 88, 91, 66, 70, 75, 89, 93, 95, 60, 
    57, 52, 69, 61, 53, 71, 50, 46, 94, 51
]

# Create histogram
plt.figure(figsize=(10, 8))
n, bins, patches = plt.hist(data, bins=10, color='#3498DB', rwidth=0.8)

# Customize appearance
plt.title('Distribution of Monthly Rainfall (mm)')
plt.xlabel('Rainfall (mm)')
plt.ylabel('Frequency')

# Show plot
plt.show()