
import matplotlib.pyplot as plt

# Data
cities = ['Tokyo', 'Delhi', 'Shanghai', 'São Paulo', 'Mumbai', 'Beijing', 'Mexico City', 'Osaka', 'Cairo', 'Dhaka']
internet_users = [37.8, 30.9, 26.3, 21.8, 20.7, 20.5, 20.1, 19.3, 19.1, 18.9]
broadband_speed = [50.2, 45.3, 48.7, 35.6, 39.8, 55.2, 28.4, 49.9, 22.1, 20.5]
mobile_penetration = [98.5, 96.7, 95.2, 94.0, 93.1, 92.8, 91.3, 90.5, 89.7, 88.9]
colors = ['#1F77B4', '#FF7F0E', '#2CA02C', '#D62728', '#9467BD', '#8C564B', '#E377C2', '#7F7F7F', '#BCBD22', '#17BECF']

# Bubble chart
plt.figure(figsize=(16, 12))
for idx, city in enumerate(cities):
    plt.scatter(internet_users[idx], broadband_speed[idx], s=mobile_penetration[idx]*20, c=colors[idx], label=city, alpha=0.6, edgecolors='w')

# Add titles and labels
plt.title('Internet Usage and Broadband Speed in Major Cities', fontsize=18)
plt.xlabel('Internet Users (Millions)', fontsize=14)
plt.ylabel('Broadband Speed (Mbps)', fontsize=14)

# Additional settings
plt.grid(True)
plt.legend(loc='upper right', title='Cities')
plt.xlim(15, 40)
plt.ylim(20, 60)

# Show plot
plt.tight_layout()
plt.show()