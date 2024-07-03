
import matplotlib.pyplot as plt

# Data points
activities = ['Running', 'Cycling', 'Yoga', 'Weightlifting', 'Swimming', 
              'Hiking', 'Tennis', 'Basketball', 'Soccer', 'Pilates', 
              'Dancing', 'Rowing']
participants = [34000, 28000, 23000, 15000, 26000, 21000, 12000, 14000, 18000, 
                11000, 19000, 13000]

# Colors for each bar
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#33FFF1', 
          '#A133FF', '#FF8633', '#33FFA1', '#A1FF33', '#3383FF', 
          '#FF3333', '#33FF83']

# Creating horizontal bar chart
plt.figure(figsize=(10, 12)) # changing the width and height of the chart
plt.barh(activities, participants, color=colors, edgecolor='black', height=0.5) # changed direction, color, and band width

# Customizing the chart
plt.ylabel('Activity', fontsize=12)
plt.xlabel('Number of Participants', fontsize=12)
plt.title('Participation in Sports & Fitness Activities for 2021', fontsize=16)
plt.xlim(10000, 35000) # Adjust the x-axis to accommodate the data range

# Display the chart
plt.tight_layout()
plt.show()