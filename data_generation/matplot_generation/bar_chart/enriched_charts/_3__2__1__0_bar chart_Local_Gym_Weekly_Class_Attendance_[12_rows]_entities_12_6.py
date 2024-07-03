
import matplotlib.pyplot as plt

# Data
sports = ['Soccer', 'Basketball', 'Tennis', 'Swimming', 'Baseball',
          'Golf', 'Cycling', 'Running', 'Volleyball', 'Gymnastics',
          'Rugby', 'Hiking', 'Boxing', 'Cricket', 'Skiing', 'Surfing']
participants = [3000, 2500, 1800, 1700, 1600, 
                1500, 1400, 1300, 1200, 1100, 
                1000, 900, 800, 700, 600, 500]

# Create vertical bar chart
plt.figure(figsize=(12, 6))  # Change width and height of the chart
colors = ['#4B0082', '#FFD700', '#ADFF2F', '#FF4500', '#00CED1', 
          '#20B2AA', '#FF69B4', '#A52A2A', '#5F9EA0', '#D2691E', 
          '#7FFF00', '#8A2BE2', '#DC143C', '#00FA9A', '#DA70D6', '#6495ED']

plt.bar(sports, participants, color=colors, width=0.5)  # Change direction of chart and bar width

# Customizing the plot
plt.ylabel('Number of Participants')
plt.title('Number of Participants by Sport (2023)', pad=20)
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()