import matplotlib.pyplot as plt

# Data
categories = ['Yoga', 'Meditation', 'Running', 'Cycling', 'Strength Training', 'Pilates', 'Swimming', 'Hiking', 'Dancing', 'Tai Chi', 'Boxing', 'Aerobics', 'Rock Climbing', 'Crossfit', 'Zumba', 'Jump Rope', 'Soccer', 'Basketball', 'Tennis', 'Badminton', 'Volleyball', 'Table Tennis', 'Martial Arts', 'Gymnastics', 'Surfing', 'Skating', 'Skiing', 'Snowboarding', 'Fishing', 'Hunting']
average_hours = [5, 4, 6, 5, 4, 3, 4, 7, 5, 4, 3, 4, 6, 4, 5, 3, 6, 5, 4, 3, 4, 3, 4, 5, 6, 4, 5, 5, 4, 5]
participants = [12000, 10000, 15000, 13000, 11000, 8000, 9000, 14000, 11000, 7000, 6000, 8500, 7500, 9500, 10000, 5000, 16000, 15000, 13000, 12000, 14000, 11000, 10500, 9500, 8000, 8500, 7000, 6500, 7500, 6000]

# Colors
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6', '#ff6666', '#c4e17f', '#ff9a8b', '#bde0fe', '#6fffe9', '#a9c4eb', '#fdcbf1', '#fc8eac', '#89ffdc', '#ff5050', '#aaffc3', '#ffd8b1', '#e6beff', '#ffdfba', '#ff6f61', '#9b9b9b', '#bada55', '#ffb347', '#ff6347', '#b0e0e6', '#fa8072', '#ffb6c1', '#98fb98', '#dda0dd']

# Set the figure size
plt.figure(figsize=(16, 12))

# Scatter plot with bubble sizes
bubble_sizes = [p / 50 for p in participants]  # Scaling the number of participants for bubble size
plt.scatter(categories, average_hours, s=bubble_sizes, c=colors, alpha=0.6)

# Labels and title
plt.xlabel('Activity')
plt.ylabel('Average Weekly Hours Spent')
plt.title('Average Weekly Hours Spent on Health & Fitness Activities')

# Rotate category labels for better readability
plt.xticks(rotation=45, ha='right')

# Show plot
plt.show()