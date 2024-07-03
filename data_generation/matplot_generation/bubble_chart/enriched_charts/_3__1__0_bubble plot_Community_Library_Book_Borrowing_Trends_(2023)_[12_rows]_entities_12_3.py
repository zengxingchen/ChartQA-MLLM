
import matplotlib.pyplot as plt

# Data
sport = ['Soccer', 'Basketball', 'Cricket', 'Tennis', 'Rugby', 'Golf', 'Formula 1', 'Boxing', 
         'Athletics', 'Baseball', 'Swimming', 'Cycling', 'Hockey', 'Table Tennis', 
         'Badminton', 'Volleyball', 'Wrestling', 'Martial Arts', 'Snooker', 'Skateboarding']
global_popularity = [40.0, 30.0, 25.0, 20.0, 15.0, 10.0, 5.0, 12.0, 18.0, 22.0, 14.0, 11.0, 13.0, 16.0, 17.0, 19.0, 8.0, 6.0, 4.0, 7.0]
average_annual_revenue = [500, 350, 300, 200, 150, 100, 450, 120, 180, 220, 140, 110, 130, 160, 170, 190, 80, 60, 40, 70]
participants = [4000, 2500, 3000, 1500, 1200, 800, 300, 900, 1700, 2000, 1100, 1000, 1050, 1400, 1450, 1600, 700, 500, 350, 650]

# Bubble sizes, normalizing participants to suitable sizes for bubbles
sizes = [p/1.5 for p in participants]

# Color codes
colors = ['#FF4500', '#32CD32', '#1E90FF', '#FFD700', '#FF69B4', 
          '#4B0082', '#00FFFF', '#FF6347', '#7CFC00', '#4682B4', 
          '#FFB6C1', '#2E8B57', '#8A2BE2', '#5F9EA0', '#FF00FF', 
          '#7FFF00', '#00FA9A', '#8B4513', '#FFDAB9', '#6495ED']

# Create plot
plt.figure(figsize=(18, 12))  # Modify width and height
plt.scatter(average_annual_revenue, global_popularity, s=sizes, c=colors, alpha=0.6)
plt.title('Global Popularity and Revenue of Various Sports', fontsize=18, pad=30)
plt.xlabel('Average Annual Revenue (Million USD)', fontsize=15)
plt.ylabel('Global Popularity (%)', fontsize=15)

# Annotate sport names
for i, txt in enumerate(sport):
    plt.annotate(txt, (average_annual_revenue[i], global_popularity[i]), ha='center')

plt.grid(True)
plt.tight_layout()
plt.show()