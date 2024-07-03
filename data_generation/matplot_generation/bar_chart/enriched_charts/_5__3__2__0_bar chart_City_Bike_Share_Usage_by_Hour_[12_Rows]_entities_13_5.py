
import matplotlib.pyplot as plt

# Data
technology = [
    'Artificial Intelligence', 'Blockchain', 'Quantum Computing', 'Internet of Things', 
    '5G Networks', 'Augmented Reality', 'Virtual Reality', 'Edge Computing', 
    'Robotics', 'Autonomous Vehicles', 'Biotechnology', 'Cybersecurity'
]
user_adoption_rate = [75, 50, 30, 60, 80, 40, 55, 45, 70, 65, 35, 90]

# Colors for each bar
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#A133FF', '#33FFA1', 
          '#FF8333', '#33A1FF', '#FF33FF', '#33FF83', '#8333FF', '#A1FF33']

# Plotting the bar chart vertically
plt.figure(figsize=(14, 10))   # Change width and height of the chart
plt.bar(technology, user_adoption_rate, color=colors, edgecolor='black', width=0.6)  # Change width for bars and apply color scheme

# Chart title and labels
plt.title('User Adoption Rate of Emerging Technologies', fontsize=20)
plt.ylabel('User Adoption Rate (%)', fontsize=16)

# Setting the ylim to start from 20 to provide better clarity for user adoption rates
plt.ylim(20, 100)

# Rotating the x-axis labels for better readability
plt.xticks(rotation=45, ha='right')

# Display the chart
plt.tight_layout()
plt.show()