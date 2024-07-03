
import matplotlib.pyplot as plt

# Data for plotting
names = [
    'Lionel Messi', 'Cristiano Ronaldo', 'Neymar', 'LeBron James', 
    'Roger Federer', 'Tiger Woods', 'Kevin Durant', 'Stephen Curry', 
    'Lewis Hamilton', 'Tom Brady', 'Giannis Antetokounmpo', 'Kawhi Leonard', 
    'Russell Westbrook', 'James Harden', 'Anthony Joshua'
]
earnings = [
    130, 120, 110, 100, 95, 90, 85, 80, 78, 76, 74, 72, 70, 68, 65
]

# Changing figure size
plt.figure(figsize=(12, 10))

# Plotting - vertical bar chart
bar_width = 0.6
plt.bar(names, earnings, color=[
    '#FF6347', '#4682B4', '#32CD32', '#FFD700', '#FF4500',
    '#7B68EE', '#FF1493', '#8A2BE2', '#00FA9A', '#00CED1',
    '#DC143C', '#B8860B', '#FF8C00', '#9932CC', '#5F9EA0'
], width=bar_width)

# Customize chart
plt.xlabel('Athletes', fontsize=14)
plt.ylabel('Earnings (Million USD)', fontsize=14)
plt.title('Top 15 Athletes\' Earnings in 2024', fontsize=16, pad=20)
plt.ylim(50, 140)

# Rotate x-ticks for better readability
plt.xticks(rotation=45, ha='right', fontsize=10)

# Show plot
plt.show()