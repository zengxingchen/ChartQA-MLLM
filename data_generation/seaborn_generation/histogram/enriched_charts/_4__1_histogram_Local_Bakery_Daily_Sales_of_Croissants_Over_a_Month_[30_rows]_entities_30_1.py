
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data
distance_data = {'Distance': [5, 7, 10, 12, 15, 20, 22, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 
                              80, 85, 90, 95, 100, 3, 6, 8, 9, 11, 13, 18, 21, 24, 27, 28, 32, 34, 
                              38, 41, 43, 46, 48, 51, 53, 57, 59, 62, 64, 67, 69, 72, 74, 78, 81, 
                              83, 86, 89, 92, 94, 97, 99]}
df = pd.DataFrame(distance_data)

# Set size of the figure
plt.figure(figsize=(12, 8))

# Plotting the histogram
sns.histplot(data=df, y='Distance', binwidth=7, color='#FF5733', edgecolor='#2A2A2A')

# Additional customizations
plt.title('Distribution of Running Distances', fontsize=16, pad=20)
plt.xlabel('Frequency', fontsize=14)
plt.ylabel('Distance (km)', fontsize=14)
plt.grid(True)

# Show the plot
plt.show()