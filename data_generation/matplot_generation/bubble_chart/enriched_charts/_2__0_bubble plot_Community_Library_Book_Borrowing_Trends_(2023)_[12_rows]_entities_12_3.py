
import matplotlib.pyplot as plt

# Data
sport = ['Soccer', 'Basketball', 'Cricket', 'Tennis', 'Golf', 'Baseball', 'Swimming', 'Cycling', 'Running', 'Boxing', 'Martial Arts', 'Volleyball', 'Badminton', 'Rugby', 'Table Tennis']
participation_rate = [25, 15, 10, 8, 5, 6, 7, 9, 20, 3, 4, 12, 14, 2, 16]
average_cost = [100, 200, 150, 300, 500, 250, 80, 200, 50, 100, 120, 70, 40, 220, 30]
popularity_index = [400, 300, 250, 220, 180, 160, 140, 130, 400, 90, 70, 150, 180, 60, 170]

# Bubble sizes, normalizing popularity_index to suitable sizes for bubbles
sizes = [index / 1.5 for index in popularity_index]

# Color codes
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A6', '#FF8C33', '#33FFF3', '#A633FF', '#FF3364', '#33FFBD', '#C7FF33', '#5733FF', '#FF9E33', '#33FFF5', '#C733FF', '#FF3370']

# Create plot
plt.figure(figsize=(16, 9))  # Modify width and height
plt.scatter(average_cost, participation_rate, s=sizes, c=colors, alpha=0.6)
plt.title('Global Sports Participation Rates and Average Costs')
plt.xlabel('Average Cost (USD)')
plt.ylabel('Participation Rate (%)')

# Annotate sport names
for i, txt in enumerate(sport):
    plt.annotate(txt, (average_cost[i], participation_rate[i]), ha='center')

plt.grid(True)
plt.tight_layout()
plt.show()