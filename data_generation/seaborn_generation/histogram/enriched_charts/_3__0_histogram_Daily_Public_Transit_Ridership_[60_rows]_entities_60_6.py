
import seaborn as sns
import matplotlib.pyplot as plt

# Data: Distance covered by athletes in kilometers
distance_data = [2.1, 3.3, 1.5, 4.0, 2.7, 3.8, 4.5, 5.2, 2.6, 4.1, 3.9, 4.8, 5.5, 6.3, 
                 1.8, 2.9, 3.7, 4.6, 5.0, 6.2, 2.1, 4.4, 5.1, 6.1, 6.9, 2.4, 3.8, 4.9, 
                 5.3, 6.0, 2.5, 3.9, 4.5, 5.7, 6.4, 2.7, 3.1, 4.0, 5.2, 6.6, 2.8, 3.6, 
                 4.3, 5.1, 6.5, 3.0, 3.2, 4.6, 5.4, 6.7, 6.8, 5.9, 6.6, 7.1, 1.9, 2.0, 
                 1.7]

# Set the size of the chart
plt.figure(figsize=(10, 8))

# Create a histogram with vertical orientation
sns.histplot(data=distance_data, kde=False, color="#ff5733", binwidth=0.5, orientation='vertical')

# Set chart title and labels
plt.title('Distance Covered by Athletes')
plt.ylabel('Frequency')
plt.xlabel('Distance (km)')

# Show the plot
plt.show()