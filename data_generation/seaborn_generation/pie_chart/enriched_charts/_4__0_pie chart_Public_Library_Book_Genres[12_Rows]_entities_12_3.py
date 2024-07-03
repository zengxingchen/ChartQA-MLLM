
import matplotlib.pyplot as plt

# Data for the chart
instruments = ['Piano', 'Guitar', 'Violin', 'Drums', 'Flute', 'Other']
percentages = [35, 25, 15, 10, 8, 7]
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#33FFF5', '#A133FF']

# Create a pie chart
plt.figure(figsize=(10, 6)) # Set the width and height of the chart
plt.pie(percentages, labels=instruments, autopct='%1.1f%%', colors=colors, startangle=140)

plt.title('Popularity of Musical Instruments in 2023', pad=20) # Change the headline to match the topic
plt.axis('equal') # Equal aspect ratio ensures that pie is drawn as a circle.

# Display the chart
plt.show()