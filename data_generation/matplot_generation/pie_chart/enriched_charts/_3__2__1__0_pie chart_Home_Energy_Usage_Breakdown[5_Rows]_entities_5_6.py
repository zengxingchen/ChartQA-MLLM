
import matplotlib.pyplot as plt

# Data
sports = ['Soccer', 'Basketball', 'Tennis', 'Running', 'Swimming', 'Cycling', 
          'Yoga', 'Weightlifting', 'Martial Arts', 'Gymnastics', 'Golf', 
          'Skiing', 'Boxing', 'Rock Climbing', 'Dancing']
participation_rates = [24.3, 17.8, 12.6, 15.1, 14.2, 10.7, 5.3, 4.0, 2.6, 1.4, 
                       4.8, 3.2, 2.0, 1.0, 7.0]

# Colors
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#A133FF', 
          '#33FFA1', '#FF8A33', '#33A1FF', '#8A33FF', '#33FF8A', 
          '#A1FF33', '#FF3333', '#33FF33', '#3333FF', '#FF33FF']

# Pie chart
fig, ax = plt.subplots(figsize=(14, 10))  # Width, Height of the chart
ax.pie(participation_rates, labels=sports, colors=colors, autopct='%1.1f%%', startangle=140)
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.title('Sports Participation Rates', pad=40)
plt.show()